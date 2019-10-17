import tweepy
# from TextBlob import TextBlob
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger

# To automatically load the init variables
from app import app

# firstly_authentication
consumer_key= app.config['TWTR_CONSUMER_KEY']
consumer_secret= app.config['TWTR_CONSUMER_SCRT']

access_token=app.config['TWTR_ACCESS_TOKEN']
access_token_secret=app.config['TWTR_ACCESS_TOKEN_SECRET']

class tweet_sentiment_result:
    def __init__(self, tweet, sentiment):
        self.tweet = tweet
        self.sentiment = sentiment

def tweep_run(keyword, count):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Define a return  list 
    results = []
    # Define a temp class variable 
    # singleresult = tweet_sentiment_result()

    # secondly-retrieve_tweets_from_respective_keyword(s)
    # public_tweets = api.search('microsoft')
    print("Searching for keyword: " + keyword)

    public_tweets = api.search(keyword, lang='en', count=count)

    for tweet in public_tweets:
        # singleresult.tweet = tweet.text 
        # print(tweet.text)
        
        # finally-perform_sentiment_analysis_on_tweets
        analysis = TextBlob(tweet.text)

        # singleresult.sentiment = analysis.sentiment
        # print(analysis.sentiment)

        # print("")

        results.append(tweet_sentiment_result(tweet.text, analysis.sentiment) )

    return(results)

