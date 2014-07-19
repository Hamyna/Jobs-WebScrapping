
import requests_oauthlib
from oauthlib.oauth2 import BackendApplicationClient

def request_token():
    consumer_key = "grant_type"
    consumer_secret = "CONSUMER_SECRET"
    redirect_url = "https://secure.dice.com/oauth/token"

    client = BackendApplicationClient(consumer_key)
    session = requests_oauthlib.OAuth2Session(consumer_key, client=client)
    token = session.fetch_token(redirect_url, client_id=consumer_key, client_secret=consumer_secret)
    # store token if you fancy
    session.get('https://secure.dice.com/oauth/token')



if __name__ == "__main__":
    request_token()
