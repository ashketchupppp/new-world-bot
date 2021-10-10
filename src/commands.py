import math
from discord.ext import commands
from discord import Embed, Color

levelExp = [100, 205, 315, 430, 550, 675, 805, 940, 1080, 1225, 1375, 1530, 1690, 1855, 2025, 2200, 2380, 2565, 2755, 2950, 3150, 3355, 3565, 3780, 4000, 4225, 4455, 4690, 4930, 5175, 5425, 5680, 5940, 6205, 6475, 6750, 7030, 7315, 7605, 7900, 8200, 8505, 8815, 9130, 9450, 9775, 10105, 10440, 10780, 11125, 11625, 12175, 12775, 13425, 14125, 14875, 15675, 16525, 17425, 18375, 19375, 20425, 21525, 22675, 23875, 25125, 26425, 27775, 29175, 30625, 32125, 33675, 35275, 36925, 38625, 40375, 42175, 44025, 45925, 47875, 49875, 51925, 54025, 56175, 58375, 60625, 62925, 65275, 67675, 70125, 72625, 75175, 77775, 80425, 83125, 85875, 88675, 91525, 94425, 97375, 100909, 104629, 108535, 112627, 116905, 121369, 126019, 130855, 135877, 141085, 146479, 152059, 157825, 163777, 169915, 176239, 182749, 189445, 196327, 203395, 210649, 218089, 225715, 233527, 241525, 249709, 258079, 266635, 275377, 284305, 293419, 302719, 312205, 321877, 331735, 341779, 352009, 362425, 373027, 383815, 394789, 405949, 417295, 428827, 440545, 452449, 464539, 476815, 489277, 501925, 514325, 527345, 540985, 555245, 570125, 585625, 601745, 618485, 635845, 653825, 672425, 691645, 711485, 731945,
        753025, 774725, 797045, 819985, 843545, 867725, 892525, 917945, 943985, 970645, 997925, 1025825, 1054345, 1083485, 1113245, 1143625, 1174625, 1206245, 1238485, 1271345, 1304825, 1338925, 1373645, 1408985, 1444945, 1481525, 1518725, 1556545, 1594985, 1634045, 1673725, 1714025, 1754945, 1796485, 1838645, 1881425]

def expToLevel(exp):
    for i in range(len(levelExp)):
        if levelExp[i] < exp:
            return i

def levelToExp(level):
    if 0 < level <= len(levelExp) + 1:
        return levelExp[level - 1]
    return None

def numItemsToCraft(startingLevel, targetLevel, itemExp):
    startingExp = levelToExp(startingLevel)
    targetExp = levelToExp(targetLevel)
    return math.ceil((targetExp - startingExp) / itemExp)

def isInt(x):
  try:
    a = int(x)
  except ValueError:
    return False
  return True

commandHelps = {
  'craft-level' : '''Usage: 
  nw!craft-level <startingLevel> <targetLevel> <itemsExp>
Purpose:
  Calculates the number of items needed to craft to go from <startingLevel> to <targetLevel>.
  <itemsExp> is the amount of experience given by each item.
'''
}

class NewWorldCommands(commands.Cog):
  @commands.command(name='craft-level')
  async def itemExpCalc(self, ctx, startingLevel, targetLevel, itemExp):
    ''' Calculates the number of items needed to craft to go from one crafting profession level to another. '''
    message = ''
    title = 'Error'
    color = color=Color.red()
    argsValid = True
    if isInt(startingLevel):
      startingLevel = int(startingLevel)
    else:
      message = 'startingLevel is not an integer'
      argsValid = False
    if isInt(targetLevel):
      targetLevel = int(targetLevel)
    else:
      message = 'targetLevel is not an integer'
      argsValid = False
    if isInt(itemExp):
      itemExp = int(itemExp)
    else:
      message = 'itemExp is not an integer'
      argsValid = False
    if argsValid:
      if startingLevel < 1 or 200 < startingLevel:
          message = f'Starting level must be a number between 1 and 200'
      elif targetLevel < 1 or 200 < targetLevel:
          message = f'Target level must be a number between 1 and 200'
      elif itemExp < 1:
          message = f'Item experience must be larger than 0'
      elif startingLevel > targetLevel:
          message = f'Starting level must be less than target level'
      else:
          numItemsNeeded = numItemsToCraft(startingLevel, targetLevel, itemExp)
          title = 'Result'
          message = f'''Craft {numItemsNeeded} items for {itemExp} each, to go from level {startingLevel} to {targetLevel}'''
          color = Color.green()
    await ctx.send(embed=Embed(description=message, title=title, color=color))

  @itemExpCalc.error
  async def standard_errors(self, ctx, error):
      await ctx.send(error)
      print(error)
