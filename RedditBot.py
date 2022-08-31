import praw
import random
import time

reddit = praw.Reddit(client_id="HaHNTRHf5IR2V-99LgGw0Q",
					 client_secret="oHx27G8O1JhivW1Znp32rB-JkLDhRw",
					 user_agent="<console:bgbgbg8:1.0>",
					 username="gurudeta",
					 password="baggapoth")

subreddit = reddit.subreddit("television")

inspiring_quotes = ["The best revenge is massive success. -Frank Sinatra",
			  "Talent is cheaper than table salt. What separates the talented individual from the successful one is a lot of hard work. -Stephen King",
			  "Fall seven times, stand up eight. -Japanese Proverb",
			  "He who has a why to live can bear almost any how. -Friedrich Nietzsche"]

for submission in subreddit.hot(limit=10):
	# print("***********")
	# print(submission.title)

	for comment in submission.comments:
		if hasattr(comment, "body"):
			comment_lower = comment.body.lower()
			if " sad " in comment_lower:
				print("----------")
				print(comment.body)
				random_index = random.randint(0, len(sad_quotes) - 1)
				comment.reply(inspiring_quotes[random_index])
				time.sleep(660)


