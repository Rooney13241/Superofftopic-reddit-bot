import praw
import configparser

''' Task List
-Init reddit
-Collect New Comments
-Parse Comment for keyword
-Log Comment for future use
'''

def main():
    subreddit = 'superofftopic'
    config = configparser.ConfigParser()
    config.read('/home/ami/src/venv/Superofftopic-reddit-bot/praw.ini')
    cfg = config['bot']
    reddit = init_reddit(cfg)
    stream_comments(reddit,subreddit)

def init_reddit(cfg):
    return praw.Reddit(client_id=cfg['client_id'],
            client_secret=cfg['client_secret'],
            user_agent=cfg['user_agent'],
            username=cfg['username'],
            password=cfg['password'])

def stream_comments(reddit,subreddit):
    for submission in reddit.subreddit(subreddit).stream.submissions(skip_existing = True):
        author =str(submission.author)
        title = submission.title
        content = submission.selftext
        print(title +"\n" + content)



if __name__ == '__main__':
    main()
   
