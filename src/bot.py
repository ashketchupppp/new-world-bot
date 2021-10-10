import os
import sys
import pathlib
from discord.ext import commands
from dotenv import load_dotenv

from commands import QuoteCommands
from mongo import Quotes

envPath = pathlib.Path(__file__).parent.parent.resolve()
load_dotenv(envPath)
args = {
  'TOKEN': None, 
  'MONGO_CONN_STR': None
}
i = 1
for arg in args:
  args[arg] = os.getenv(arg)
  if not args[arg]:
    args[arg] = sys.argv[i]
  i += 1
print(args)
print(args)
print('Connecting to mongo...')
quotes = Quotes(args['MONGO_CONN_STR'])
print('Successful connection made to mongo')

bot = commands.Bot(command_prefix='q!')
bot.add_cog(QuoteCommands(bot, quotes))

try:
  bot.run(args['TOKEN'])
except KeyboardInterrupt:
  print('Exiting...')
finally:
  pass
