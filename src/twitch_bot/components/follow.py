from twitchio import eventsub
from twitchio.ext import commands

from ..config import BOT_ID


class FollowComponent(commands.Component):
    def __init__(self, bot):
        self.bot = bot

    @commands.Component.listener()
    async def event_follow(self, payload: eventsub.FollowEvent) -> None:
        channel = self.bot.create_partialuser(payload.broadcaster.id)
        sender = self.bot.create_partialuser(BOT_ID)

        await channel.send_message(sender=sender, message=f"Спасибо за фоллоу, {payload.user.name}!")
