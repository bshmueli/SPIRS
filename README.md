# SPIRS Sarcasm Dataset

SPIRS is a unique dataset of 15,000 sarcastic tweets. SPIRS was collected using **reactive supervision**, a new data capturing method. 
Reactive supervision allows the collection of both _intended sarcasm_ and _perceived sarcasm_ texts. 

**SPIRS** stands for **S**arcasm, **P**erceived and **I**ntended, by **R**eactive **S**upervision :)

To find out more about SPIRS and reactive supervision, check out the [reactive supervision paper](https://arxiv.org/abs/2009.13080), or read the [Medium article](https://towardsdatascience.com/the-magic-of-reactive-supervision-3fc83cdb1ca4). Or watch this short, 7-minute [YouTube video about reactive supervision](https://www.youtube.com/watch?v=Wx6S-KdZ1nM).

Use this repository to download SPIRS. The repository includes the following data files:

  * `SPIRS-sarcastic-ids.csv` the sarcastic tweet IDs (15,000 "positive" samples)
  * `SPIRS-non-sarcastic-ids.csv` the non-sarcastic tweet IDs (15,000 "negative" samples)
  
Additional fields for each sarcastic tweet include the sarcasm perspective (intended/perceived), author sequence, and contextual tweet IDs (cue, oblivious, and eliciting tweets).
More information is available in the reactive supervision paper.

To comply with Twitter's privacy policy, the dataset files include only the tweet IDs. To fetch the tweet texts, follow these steps:

  * Install the latest version of Tweepy:
  
    `pip3 install tweepy`
  * Rename our `credentials-example.py` to `credentials.py`
  * Add your Twitter API credentials by editing `credentials.py`
  * Run the script:
  
    `python3 fetch-tweets.py`

The script will fetch the texts and create two new files, one for sarcastic and the other for non-sarcastic tweets:

  * `SPIRS-sarcastic.csv`
  * `SPIRS-non-sarcastic.csv`

## Citation

Kindly cite the paper using the following BibTex entry:

```
@inproceedings{
    shmueli:reactive-supervision, 
    title={Reactive Supervision: A New Method for Collecting Sarcasm Data}, 
    author={Shmueli, Boaz and Ku, Lun-Wei and Ray, Soumya}, 
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing", 
    year = "2020", 
    publisher = "Association for Computational Linguistics"
}
```

