from twitchio import eventsub
from twitchio.ext import commands


class FollowComponent(commands.Component):
    def __init__(self, bot):
        self.bot = bot

    @commands.Component.listener()
    async def event_follow(self, payload: eventsub.FollowEvent) -> None:
        channel = self.bot.create_partialuser(payload.broadcaster.id)
        await channel.send_message(f"Спасибо за фоллов, {payload.user.name}!")
