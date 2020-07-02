import praw
import pandas as pd

reddit = praw.Reddit(client_id = 'CLIENT_ID',
                    client_secret = 'CLIENT_SECRET',
                    usernme = 'USERNAME',
                    password = 'PASSWORD',
                    user_agent = 'PRAW Blog')


subreddit_list=  ['india','worldnews','announcements','funny','AskReddit',
                  'gaming','pics','science','movies','todayilearned'
                 ]


author_list = []
id_list = []
link_flair_text_list = []
num_comments_list = []
score_list = []
title_list = []
upvote_ratio_list = []


for subred in subreddit_list:
    
    subreddit = reddit.subreddit(subred)
    hot_post = subreddit.hot(limit = 10000)

    for sub in hot_post:

        author_list.append(sub.author)
        id_list.append(sub.id)
        link_flair_text_list.append(sub.link_flair_text)
        num_comments_list.append(sub.num_comments)
        score_list.append(sub.score)
        title_list.append(sub.title)
        upvote_ratio_list.append(sub.upvote_ratio)

    print(subred, 'completed; ', end='')
    print('total', len(author_list), 'posts has been scraped')


df = pd.DataFrame({'ID':id_list, 
                   'Author':author_list, 
                   'Title':title_list,
                   'Count_of_Comments':num_comments_list,
                   'Upvote_Count':score_list,
                   'Upvote_Ratio':upvote_ratio_list,
                   'Flair':link_flair_text_list
                  })
df.to_csv('reddit_dataset.csv', index = False)
