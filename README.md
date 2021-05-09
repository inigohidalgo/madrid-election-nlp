1. Clone the repository: `git clone github.com/inigohidalgo/madrid-election-nlp`
2. Navigate into it: `cd madrid-election-nlp`
3. Install the requirements: `pip install -r requirements.txt`

In order to carry out your own sentiment analysis, we have provided the code to gather tweets on a new hashtag. In the script twitter_import.py you need to fill in your twitter developer credentials in order to be able to download new tweets. Alternatively, we have provided the #debateTelemadrid tweets in the repository.
Running `python twitter_import.py <search_term>` in the command-line will start the download of tweets. The script automatically adds a hashtag to the beginning of the term, and will begin streaming the tweets and will store them in data/#search_term.json

You can then start running the notebook. We have provided the training dataset but have also made available the trained model’s weights on our google drive (GitHub only allows files up to 100MB). You can find it [here](https://drive.google.com/file/d/1sFHdn5c5onhJufHQU9Cut75RznBFUMMQ/view?usp=sharing). Download the file and place it in the folder called saved_model alongside the file config.json. This can be imported through the notebook which will allow you to directly make predictions without having to re-train the model. 

If you simply want to perform new sentiment predictions for a new dataset, you should run the following sections:
1.	Setup, making sure the hashtag_analyzed variable is correct (since it is also the filename of the json containing the tweets)
2.	Import and join election tweets
3.	Prepare data for training
4.	Move onto Predictions and run all the way to the cell before the Processing section which will generate a csv with the list of tweets and their predicted sentiment.
