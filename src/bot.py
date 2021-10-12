import os
import sys
import pathlib
from discord.ext import commands
from dotenv import load_dotenv

from commands import NewWorldCommands 
# from mongo import Quotes

envPath = pathlib.Path(__file__).parent.parent.resolve()
load_dotenv(envPath)
args = {
  'TOKEN': None
}
i = 1
for arg in args:
  args[arg] = os.getenv(arg)
  if not args[arg]:
    args[arg] = sys.argv[i]
  i += 1

bot = commands.Bot(command_prefix='qq!')
bot.add_cog(NewWorldCommands())
try:
  bot.run(args['TOKEN'])
except KeyboardInterrupt:
  print('Exiting...')
finally:
  pass
