import pymongo
import random
import time

class Quotes:
  def __init__(self, conn_str):
    self.client = pymongo.MongoClient(conn_str)
    self.client.server_info()
    self.quotes = self.client.get_database()['quotes']
    
  def get_random_quote(self, user):
    filter = {'user': user}
    quotes = self.quotes.find(filter)
    if quotes.count():
      quotes = [quote for quote in quotes]
      return random.choice(quotes)

  def create_quote(self, user, quote, guild):
    quote = {
      'time': time.time(),
      'user': user,
      'quote': quote,
      'guild': guild.id
    }
    self.quotes.insert_one(quote)