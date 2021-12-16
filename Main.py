from random_word import RandomWords
from discord_webhook import DiscordWebhook
from datetime import date,datetime
import pytz
from time import sleep

IST = pytz.timezone('Asia/Kolkata')
today = date.today()
r = RandomWords()
IST = pytz.timezone('Asia/Kolkata')

# Return a single random word
# print(r.get_random_word())
# # Return list of Random words
# print(r.get_random_words())
# # Return Word of the day
woday = r.word_of_the_day()
worday = woday.replace("{","")
worday = worday.replace("}","")
worday = worday.replace("[","")
worday = worday.replace("]","")
worday = worday.replace('"',"")
worday = worday.replace('note',"")
worday = worday.replace('null',"")
worday = worday.replace(',',"\n")
worday = worday.replace('word',"\n\n Word of the day")

webhook = DiscordWebhook(url='//your webhook//', rate_limit_retry=True,
                            content=f'{today},{datetime.now(IST)}{worday}')
response = webhook.execute()
print (f"{datetime.now(IST)}")
print(worday)
