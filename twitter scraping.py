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


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.twitter_scraped_data
collection = db.scraped data

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = {"scraped data+current Timestamp": [df.to_dict(orient='records')]}
collection.insert_one(data)

import streamlit as st
keyword = st.text_input("Enter keyword or hashtag to search")
date_range = st.selectbox("Select date range", ["Last 100 days"])
tweet_count = st.number_input("Enter number of tweets to scrape", min_value=1, max_value=1000, value=100)
def get_tweets(hashtag, date_range, count):
    data = {'date': [], 'id': [], 'url': [], 'tweet_content': [], 'user': [], 'reply_count': [], 'retweet_count': [], 'language': [], 'source': [], 'like_count': []}
    tweets = tweepy.Cursor(api.search,
                       q=hashtag,
                       lang="en",
                       since=date_range[0],
                       until=date_range[1]).items(count)
    for tweet in tweets:
        data['date'].append(tweet.created_at)
        data['id'].append(tweet.id)
        data['url'].append("https://twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id))
        data['tweet_content'].append(tweet.text)
        data['user'].append(tweet.user.screen_name)
        data['reply_count'].append(tweet.reply_count)
        data['retweet_count'].append(tweet.retweet_count)
        data['language'].append(tweet.lang)
        data['source'].append(tweet.source)
        data['like_count'].append(tweet.favorite_count)
    df = pd.DataFrame(data)
    return df

    
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
    st.dataframe(df)

if st.button("Save to database"):
   
    st.success("Data saved to database")


if st.button("Download data"):
    file_format = st.selectbox("Select file format", ["CSV", "JSON"])
    if file_format == "CSV":
        df.to_csv("tweets.csv", index=False)
        st.success("Data downloaded as CSV")
    elif file_format == "JSON":
        df.to_json("tweets.json", index=False)
        st.success("Data downloaded as JSON")
