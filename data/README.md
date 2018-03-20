This directory contains two files containing IDs and labels for experiments conducted in the paper
"Separating Facts from Fiction: Linguistic Models to Classify Suspicious and Trusted News Posts on
Twitter". It also contains a file `tweets.json`, which contains all available Tweets (as of
March 19, 2018) referenced in these files, scraped to a JSON array.

The two files from the original paper are:
* multiclass_tweets.csv
    - CSV containing ID's and four labels for the multiclass experiments 
    presented in the paper
    - The mapping between integers and labels in this dataset is the following:
    
    Propaganda: 0;
    Clickbait: 1;
    Satire: 2;
    Hoax: 3

* binary_tweets.csv
    - CSV containing ID's and two labels for binary experiments
    presented in the paper
    - Note that the tweets labeled as 'unverified' in this dataset make up
    the dataset in multiclass.csv, but contain more granular labels in the multiclass.csv file
    - The mapping between integers and labels in this dataset is the following:
    
    Verified News: 0;
    Unverified News: 1

Each of these contains the following columns:
* user_id: Twitter-assigned user ID
* tweet_id: Twitter-assigned tweet ID
* label: Integer indicating the label of tweets used in running our experiments for the paper
