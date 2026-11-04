import asyncio

import asqlite

from .bot import Bot


async def main() -> None:
    async with asqlite.create_pool("tokens.db") as pool:
        bot = Bot(token_database=pool)
        await bot.start(with_adapter=False)


if __name__ == "__main__":
    asyncio.run(main())
