import asyncio
import logging

from twitchio.ext import commands

from ..config import BOT_ID, OWNER_ID, PERIODIC_LINKS


class TimerComponent(commands.Component):
    def __init__(self, bot):
        self.bot = bot
        self._task = None
        self.message_count = 0

    async def component_load(self) -> None:
        self._task = asyncio.create_task(self._periodic_links())

    async def component_teardown(self) -> None:
        if self._task:
            self._task.cancel()

    @commands.Component.listener()
    async def event_message(self, payload) -> None:
        if payload.chatter and payload.chatter.id == BOT_ID:
            return
        self.message_count += 1
        logging.debug(f"Message count: {self.message_count}")

    async def _periodic_links(self) -> None:
        channel = self.bot.create_partialuser(OWNER_ID)
        sender = self.bot.create_partialuser(BOT_ID)

        i = 0
        while True:
            await asyncio.sleep(600)

            if self.message_count >= 5:
                try:
                    await channel.send_message(sender=sender, message=PERIODIC_LINKS[i % len(PERIODIC_LINKS)])
                    logging.info(f"Timer message sent (messages before: {self.message_count})")
                    i += 1
                except Exception as e:
                    logging.error(f"Failed to send timer message: {e}")
                self.message_count = 0
            else:
                logging.info(f"Skipped timer: only {self.message_count} messages in chat")
