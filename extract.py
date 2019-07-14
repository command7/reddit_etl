import praw
import configparser
import os

config_parser = configparser.ConfigParser()
config_parser.read_file(open('configurations.cfg', 'r'))

client_secret = config_parser['REDDIT']['CLIENT_SECRET']
client_id = config_parser['REDDIT']['CLIENT_ID']
username = config_parser['REDDIT']['USERNAME']
password = config_parser['REDDIT']['PASSWORD']

