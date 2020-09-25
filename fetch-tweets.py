from credentials import CONSUMER_KEY, CONSUMER_SECRET
import tweepy, csv
from time import sleep

def all_rows(anonfile):
  reader = csv.DictReader(open(anonfile, 'r'), delimiter=',')
  return [row for row in reader]

def fetch_tweets(rows):
  tweet_ids = [[row[key] for key in list(row.keys())[1:]] for row in rows]
  tweet_ids = [tweet_id for sublist in tweet_ids for tweet_id in sublist if tweet_id]
  return {tweet.id_str:tweet for tweet in fetch_ids(tweet_ids) if tweet.id_str != ''}

def fetch_ids(ids):
  id_lists = [ids[x:x+100] for x in range(0, len(ids), 100)]
  tweets = []
  for idx, id_list in enumerate(id_lists):
    print('{}.'.format(len(id_lists) - idx), flush=True, end='')
    tweets.extend([tweet for tweet in api.statuses_lookup(id_list, tweet_mode='extended')])
  print()
  return tweets

def deanon(de_anon_file, rows, tweets):
  with open(de_anon_file, 'w', newline='\n', encoding='utf-8') as f:
    fieldnames = list(rows[0].keys())
    tweet_types = [key for key in fieldnames[1:] if '_id' in key]
    fieldnames.extend([key.replace('_id','_text') for key in tweet_types])
    dict_writer = csv.DictWriter(f, quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
    dict_writer.writeheader()
    for row in rows:
      for key in tweet_types:
        row[key.replace('_id','_text')] = tweets[row[key]].full_text if row[key] in tweets else None
      dict_writer.writerow(row)

def convert(anon_file, de_anon_file):
    print('Fetching tweets for {}'.format(anon_file))
    rows = all_rows(anon_file)
    tweets = fetch_tweets(rows)
    deanon(de_anon_file, rows, tweets)

if __name__ == "__main__":
  try:
    CONSUMER_KEY
    CONSUMER_SECRET
  except:
    print('Edit credentials.py to add your Twitter API credentials in the first two lines (CONSUMER_KEY and CONSUMER_SECRET)')
    print('See here for more information on getting API credentials: https://developer.twitter.com/en/apps')
    exit(1)
  auth = tweepy.AppAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
  api = tweepy.API(auth, wait_on_rate_limit=True,
                        wait_on_rate_limit_notify=True,
                        retry_count=10, retry_delay=60,
                        retry_errors=[400] + list(range(402,599)))
  print('This can take some time, so make yourself a cup of Taiwanese oolong tea and let the magic happen!')
  sleep(3)
  convert('SPIRS-non-sarcastic-ids.csv', 'SPIRS-non-sarcastic.csv')
  convert('SPIRS-sarcastic-ids.csv', 'SPIRS-sarcastic.csv')
  print('That\'s it! Hope you enjoyed the ride :)')
