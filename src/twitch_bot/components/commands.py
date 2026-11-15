from twitchio.ext import commands

from ..config import YT_URL, TG_URL, INSTAGRAM_URL, DISCORD_URL, STEAM_URL, DONATE_URL, WISHLIST_URL


class CommandsComponent(commands.Component):

    @commands.command(name="yt", aliases=["ют", "ютуб"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def telegram_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"YouTube: {YT_URL}")

    @commands.command(name="tg", aliases=["тг", "телеграм"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def telegram_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Telegram: {TG_URL}")

    @commands.command(name="inst", aliases=["инст", "инстаграм"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def discord_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Instagram: {INSTAGRAM_URL}")

    @commands.command(name="ds", aliases=["дс", "дискорд"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def discord_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Discord: {DISCORD_URL}")

    @commands.command(name="steam", aliases=["стим"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def discord_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Steam: {STEAM_URL}")

   # @commands.command(name="wish", aliases=["вишлист"])
   # @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
   # async def donate_cmd(self, ctx: commands.Context) -> None:
   #     await ctx.reply(f"Wishlist(Fetta): {WISHLIST_URL}")

    @commands.command(name="donate", aliases=["донат"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def donate_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Donation: {DONATE_URL}")
