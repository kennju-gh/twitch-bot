import asyncio
import logging

from twitchio.ext import commands

from ..config import BOT_ID, OWNER_ID, PERIODIC_LINKS


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
        sender = self.bot.create_partialuser(BOT_ID)

        i = 0
        while True:
            await asyncio.sleep(1200)
            try:
                await channel.send_message(sender=sender, message=PERIODIC_LINKS[i % len(PERIODIC_LINKS)])
                logging.info("Timer message sent successfully")
            except Exception as e:
                logging.error(f"Failed to send timer message: {e}")
            i += 1
