import praw
import configparser
import os

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


