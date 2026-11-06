import logging

import asqlite
import twitchio
from twitchio import eventsub
from twitchio.ext import commands

from .components.commands import CommandsComponent
from .components.follow import FollowComponent
from .components.timer import TimerComponent
from .config import BOT_ID, CLIENT_ID, CLIENT_SECRET, OWNER_ID


class Bot(commands.AutoBot):
    def __init__(self, *, token_database: asqlite.Pool) -> None:
        self.token_database = token_database
        super().__init__(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            bot_id=BOT_ID,
            owner_id=OWNER_ID,
            prefix="!",
        )

    async def setup_hook(self) -> None:
        await self.add_component(FollowComponent(self))
        await self.add_component(TimerComponent(self))
        await self.add_component(CommandsComponent(self))

    async def event_oauth_authorized(self, payload: twitchio.authentication.UserTokenPayload) -> None:
        await self.add_token(payload.access_token, payload.refresh_token)
        try:
            await self.attempt_subscribe()
        except Exception as e:
            logging.warning(f"Subscription attempt after auth: {e}")

    async def attempt_subscribe(self) -> None:
        subs = [
            eventsub.ChatMessageSubscription(broadcaster_user_id=OWNER_ID, user_id=BOT_ID),
            eventsub.ChannelFollowSubscription(
                broadcaster_user_id=OWNER_ID,
                moderator_user_id=BOT_ID
            ),
        ]
        resp = await self.multi_subscribe(subs)
        if resp.errors:
            for error in resp.errors:
                if "409" in str(error) or "Conflict" in str(error):
                    logging.info("Subscription already exists, skipping.")
                else:
                    logging.warning(f"Failed to subscribe: {error}")
        else:
            logging.info("Subscribed successfully")

    async def event_ready(self) -> None:
        logging.info(f"Bot is ready! Listeners count: {len(self._listeners)}")

    async def event_command_error(self, payload) -> None:
        if isinstance(payload.exception, commands.CommandOnCooldown):
            user_name = payload.context.author.name if payload.context.author else "Unknown"
            command_name = payload.context.command.name
            logging.info(
                f"Cooldown triggered: {user_name} tried to use !{command_name}."
                f"Wait {payload.exception.retry_after:.1f}s."
            )
            return

        logging.error(f"Command error: {payload.exception}")
