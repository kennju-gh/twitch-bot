import asyncio

from twitchio.ext import commands

from ..config import OWNER_ID, PERIODIC_LINKS


class TimerComponent(commands.Component):
    def __init__(self, bot):
        self.bot = bot
        self._task = None

    async def component_load(self) -> None:
        self._task = asyncio.create_task(self._periodic_links())

    async def component_teardown(self) -> None:
        if self._task:
            self._task.cancel()

    async def _periodic_links(self) -> None:
        channel = self.bot.create_partialuser(OWNER_ID)
        i = 0
        while True:
            await asyncio.sleep(1800)
            await channel.send_message(PERIODIC_LINKS[i % len(PERIODIC_LINKS)])
            i += 1
