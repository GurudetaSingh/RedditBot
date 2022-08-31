import praw
import random
import time

# Python Reddit API Wrapper, create account at reddit.com/prefs/apps and replace information
reddit = praw.Reddit(client_id="",
		     client_secret="",
		     user_agent="",
		     username="",
		     password="")

# Access television subreddit
subreddit = reddit.subreddit("television")

inspiring_quotes = ["The best revenge is massive success. -Frank Sinatra",
		    "Talent is cheaper than table salt. What separates the talented individual from the successful one is a lot of hard work. -Stephen King",
		    "Fall seven times, stand up eight. -Japanese Proverb",
		    "He who has a why to live can bear almost any how. -Friedrich Nietzsche"]

# Loop through first 10 submisssions in subreddit
for submission in subreddit.hot(limit=10):
	# print("***********")
	# print(submission.title)

	# Loop through comments for word 'sad' and replace with random inspiring quote
	for comment in submission.comments:
		if hasattr(comment, "body"):
			comment_lower = comment.body.lower()
			if " sad " in comment_lower:
				print("----------")
				print(comment.body)
				random_index = random.randint(0, len(sad_quotes) - 1)
				comment.reply(inspiring_quotes[random_index])
				time.sleep(660)


