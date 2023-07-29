import discord
from discord.ext import commands

from .wordle import (
    daily_puzzle_id, generate_info_embed, generate_puzzle_embed,
    process_message_as_guess, random_puzzle_id)

class Games(commands.Cog, name="games"):
    """Miscellaneous games like Wordle or a dice roller."""

    COG_EMOJI = "🕹️"

    def __init__(self, bot: discord.Client):
        self.bot:discord.Client = bot

    @commands.hybrid_command(name="wordle", description="Plays a game of Wordle : <wordle_id> | daily | random | help.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @discord.app_commands.describe(wordle='<wordle_id>, daily, random, or help')
    @commands.guild_only()
    async def wordle(
        self,
        ctx: commands.Context,
        wordle: str
    ):
        """
        Plays a game of Wordle.

        **You can start a game with:**
        :key: `|h|wordle <puzzle_id>` - Play a puzzle by it's ID
        :sunny: `|h|wordle daily` - Play the puzzle of the day
        :game_die: `|h|wordle random` - Play a random puzzle
        
        Use `|h|wordle help` for info on how to play.
        """
        if wordle in ["random","r","rand",None]:
            await ctx.reply(embed=generate_puzzle_embed(ctx.author, random_puzzle_id()), mention_author=False)
        elif wordle in ["daily","d","today","todays"]:
            await ctx.reply(embed=generate_puzzle_embed(ctx.author, daily_puzzle_id()), mention_author=False)
        elif wordle in ["info","help","?"]:
            await ctx.reply(embed=generate_info_embed(ctx.clean_prefix), mention_author=False, ephemeral=False)
        elif wordle.isdigit():
            await ctx.reply(embed=generate_puzzle_embed(ctx.author, wordle), mention_author=False)
        else:
            await ctx.reply(embed=generate_info_embed(ctx.clean_prefix), ephemeral=True)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(
        self,
        message: discord.Message
    ):
        """
        When a message is sent, process it as a wordle guess.
        """
        # Don't look at messages by bots
        if message.author.bot:
            return False
        
        # get the message replied to
        ref = message.reference
        if not ref or not isinstance(ref.resolved, discord.Message):
            return False
        parent = ref.resolved

        # if the parent message is not the bot's message, ignore it
        if parent.author.id != self.bot.user.id:
            return False

        # if the parent message is not from a bot, ignore it
        if not parent.author.bot:
            return False

        # check that the message has embeds
        if not parent.embeds:
            return False

        embed = parent.embeds[0]
        if not embed.title:
            return False
        if not embed.footer:
            return False
    
        is_wordle_guess = await process_message_as_guess(self.bot, message, parent, embed)

async def setup(bot: commands.bot):
    await bot.add_cog(Games(bot))