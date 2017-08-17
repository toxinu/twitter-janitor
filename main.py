#!/usr/bin/env python
import os
import datetime

import twitter

now = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
older_than = now - datetime.timedelta(days=30 * 3)


def destroy_favorites(api):
    print(" :: Destroying favorites...")
    lastest_id = None
    favs_count = 0
    favs_deleted_count = 0
    while True:
        favs = api.GetFavorites(count=200, max_id=lastest_id)
        for fav in favs:
            favs_count += 1
            created_at = datetime.datetime.strptime(
                fav.created_at, '%a %b %d %H:%M:%S %z %Y')
            if created_at < older_than:
                favs_deleted_count += 1
                print('Unfavoriting... "{} - {}"'.format(
                    fav.created_at, fav.text.replace('\n', '')))
                api.DestroyFavorite(fav)
        else:
            if lastest_id == fav.id:
                break
            lastest_id = fav.id

    print("    - Total favorites: {}".format(favs_count))
    print("    - Total favorites deleted: {}".format(favs_deleted_count))


def destroy_statuses(api):
    print(" :: Destroying statuses (including retweets + replies)...")
    lastest_id = None
    statuses_count = 0
    statuses_deleted_count = 0
    while True:
        statuses = api.GetUserTimeline(count=200, max_id=lastest_id)
        for status in statuses:
            statuses_count += 1
            created_at = datetime.datetime.strptime(
                status.created_at, '%a %b %d %H:%M:%S %z %Y')
            if created_at < older_than:
                statuses_deleted_count += 1
                print('Unretweet... "{} - {}"'.format(
                    status.created_at, status.text.replace('\n', '')))
                api.DestroyStatus(status)
        else:
            if lastest_id == status.id:
                break
            lastest_id = status.id

    print("    - Total statuses: {}".format(statuses_count))
    print("    - Total statuses deleted: {}".format(statuses_deleted_count))


def main():
    api = twitter.Api(
        consumer_key=os.environ.get("TWITTER_CONSUMER_KEY"),
        consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
        access_token_key=os.environ.get("TWITTER_ACCESS_TOKEN_KEY"),
        access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
        sleep_on_rate_limit=True)
    destroy_favorites(api)
    destroy_statuses(api)


def handler(event, context):
    main()


if __name__ == "__main__":
    main()
