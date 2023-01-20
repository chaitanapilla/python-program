import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient

query = "(from:elonmusk) until:2023-01-10 since:2022-07-25"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
     if len(tweets) == limit:
       break
     else:
       tweets.append([tweet.date, tweet.user.username, tweet.content])
df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
print(df)
