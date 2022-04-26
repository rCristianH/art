from re import A
import secrets
import tweepy

consumer_key = 'hOl2SvO08u1lzqRByR87RCGJc'
consumer_secret = 'Kl4ijpaOzBKDTqmtHssuQMxZL3EqcUwsnkbuIfAnEiPjoj5lJ8'

key = '1499094344585854980-Y11kZJaV04hgCES88Cxb6bbGa5334S'
secret = 'OPpCjzs7gsPhYX8jxcWpnxi3UHAfkugpSIO4MSGs6qOBQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

api.update_status("Hello")
""" def main():
    while True:
        try:
            pass
            ####
        except tweepy.TweepError as e:
            raise e

if __name__ == "__main__":
    main()
 """