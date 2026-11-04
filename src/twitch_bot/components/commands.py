from twitchio.ext import commands

from ..config import DISCORD_URL, DONATE_URL, TG_URL


class CommandsComponent(commands.Component):
    @commands.command(name="телеграм", aliases=["тг", "tg"])
    async def telegram_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Telegram: {TG_URL}")

    @commands.command(name="дискорд", aliases=["дс", "ds"])
    async def discord_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Discord: {DISCORD_URL}")

    @commands.command(name="донат", aliases=["donate"])
    async def donate_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Поддержать стрим: {DONATE_URL}")
