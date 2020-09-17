= SPIRS

This directory includes the following data files. To comply with Twitter's privacy policy, the files include only the tweet IDs.

  - SPIRS-sarcastic-ids.csv
  - SPIRS-non-sarcastic-ids.csv

To fetch the tweet texts, follow these steps:

  - Rename credentials-example.py to credentials.py
  - Add your Twitter API credentials by editing credentials.py
  - Run `python3 fetch_texts.py`

The script will fetch the texts and create two new files, one for sarcastic and the other for non-sarcastic tweets.
