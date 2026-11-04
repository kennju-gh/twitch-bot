import asyncio
import logging
import os

import asqlite

from .bot import Bot

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

async def main() -> None:
    db_exists = os.path.exists("tokens.db")

    async with asqlite.create_pool("tokens.db") as pool:
        bot = Bot(token_database=pool)
        await bot.start(with_adapter=not db_exists)

if __name__ == "__main__":
    asyncio.run(main())
