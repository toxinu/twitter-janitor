# twitter-janitor

A simple script (AWS Lambda compatible) that delete `likes` and every `statuses` 
older than 3 months from your Twitter account.

## Setup

- Register a Twitter app in order to use it.
- Add these environment variables: `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`,`TWITTER_ACCESS_TOKEN_KEY`, `TWITTER_ACCESS_TOKEN_SECRET`
- Create a `virtualenv` and install `requirements.txt`
- Run `python main.py`

If you want to deploy on AWS Lambda, run `make package` to have your `.zip` int `./build` directory.
