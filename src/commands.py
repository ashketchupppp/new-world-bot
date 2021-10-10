from discord.ext import commands
from discord import Embed

class QuoteCommands(commands.Cog):
  def __init__(self, bot, quotes):
      self.bot = bot
      self.quotes = quotes
      self.quoteChannelName = 'quotes'

  @commands.command(name='create-quote')
  async def createQuote(self, ctx, user, quote):
    self.quotes.create_quote(user, quote, ctx.guild)
    await ctx.send(f'Created a new quote for {user}')
    if not self.quoteChannelName in [ch.name for ch in ctx.guild.channels]:
      await ctx.guild.create_text_channel(self.quoteChannelName)
    quotesChannel = [ch for ch in ctx.guild.channels if ch.name == self.quoteChannelName].pop()
    await quotesChannel.send(user, embed=Embed(description=quote))

  @commands.command(name='get-quote')
  async def getQuote(self, ctx, user):
    quote = self.quotes.get_random_quote(user)
    if quote:
      await ctx.send(f'{quote["user"]}: `{quote["quote"]}`')
    else:
      await ctx.send(f'Unable to find a quote from {user}')

  @getQuote.error
  @createQuote.error
  async def standard_errors(self, ctx, error):
      await ctx.send(error)
      print(error)