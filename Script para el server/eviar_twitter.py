import tweepy
consumer_key = "heJhuIjceNhOiAmPMTmytRM0z"
consumer_secret = "aW9ZyZ62ftjqQsUlyTLgCyQQcuuRiuCdRDdArJvxkSBrmfPxJL"
access_token = "1684587296-jJ0Ybg4kyfEQkLzgP5CPNhO8KAUX1EnfL6yl5uc"
access_token_secret = "qms7eW88cn18DErumweKMlhoy5t62cBnRNWHL97pzeRuw"

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    api.update_status("hola, soy un bot")

