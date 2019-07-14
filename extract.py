import praw
import configparser
import pandas as pd

def connect_to_reddit(configuration_file):
    config_parser = configparser.ConfigParser()
    config_parser.read_file(open(configuration_file, 'r'))

    client_secret = config_parser['REDDIT']['CLIENT_SECRET']
    client_id = config_parser['REDDIT']['CLIENT_ID']
    username = config_parser['REDDIT']['USERNAME']
    password = config_parser['REDDIT']['PASSWORD']

    reddit_client = praw.Reddit(client_id=client_id,
                                client_secret=client_secret,
                                username=username,
                                password=password,
                                user_agent='testscript by /u/dash_365'
                                )
    returned_user_name = ''
    try:
        returned_user_name = reddit_client.user.me()
    except Exception as e:
        print("Connection unsuccessful. Check credentials.")
    if returned_user_name == username:
        print("Connection successful")
        return reddit_client


def get_posts(reddit_client, num_posts=1):
    posts = []
    column_names = ['id', 'title', 'num_comments',
                    'score', 'upvote_ratio', 'created_utc',
                    'url']
    hot_posts = reddit_client.subreddit('all').top('day', limit=num_posts)
    print(f'Obtained Submission object with top {num_posts} comments.')
    for count, post in enumerate(hot_posts, start=1):
        print(f'Processing {count} of {num_posts}.')
        posts.append([post.id,
                      post.title,
                      post.num_comments,
                      post.score,
                      post.upvote_ratio,
                      post.created_utc,
                      post.url
                      ])
    print("Process completed successfully.\nWriting data to CSV format.")
    df = pd.DataFrame(posts, columns=column_names)
    df.to_csv('post_details.csv')
    print("CSV file stored.")


if __name__ == '__main__':
    reddit_client = connect_to_reddit('configurations.cfg')
    get_posts(reddit_client, 5)





