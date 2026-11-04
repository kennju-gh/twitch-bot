from twitchio.ext import commands

from ..config import DISCORD_URL, DONATE_URL, TG_URL


class CommandsComponent(commands.Component):
    @commands.command(name="tg", aliases=["тг", "телеграм"])
    async def telegram_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Telegram: {TG_URL}")

    @commands.command(name="ds", aliases=["дс", "дискорд"])
    async def discord_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Discord: {DISCORD_URL}")

    @commands.command(name="donate", aliases=["донат"])
    async def donate_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Поддержать стрим: {DONATE_URL}")
