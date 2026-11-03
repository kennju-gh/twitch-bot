import asyncio

import asqlite
from twitchio import eventsub

from .bot import Bot
from .config import BOT_ID, OWNER_ID


async def main() -> None:
    subs = [
        eventsub.ChatMessageSubscription(broadcaster_user_id=OWNER_ID, user_id=BOT_ID),
        eventsub.FollowSubscription(broadcaster_user_id=OWNER_ID),
    ]
    async with asqlite.create_pool("tokens.db") as pool:
        bot = Bot(token_database=pool, subs=subs)
        await bot.start()


if __name__ == "__main__":
    asyncio.run(main())
