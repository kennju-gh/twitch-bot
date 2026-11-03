import asqlite
import twitchio
from twitchio import eventsub
from twitchio.ext import commands

from .components.follow import FollowComponent
from .components.timer import TimerComponent
from .config import BOT_ID, CLIENT_ID, CLIENT_SECRET, OWNER_ID


class Bot(commands.AutoBot):
    def __init__(self, *, token_database: asqlite.Pool, subs: list[eventsub.SubscriptionPayload]) -> None:
        self.token_database = token_database
        super().__init__(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            bot_id=BOT_ID,
            owner_id=OWNER_ID,
            subscriptions=subs,
            force_subscribe=True,
        )

    async def setup_hook(self) -> None:
        await self.add_component(FollowComponent(self))
        await self.add_component(TimerComponent(self))

    async def event_oauth_authorized(self, payload: twitchio.authentication.UserTokenPayload) -> None:
        await self.add_token(payload.access_token, payload.refresh_token)
