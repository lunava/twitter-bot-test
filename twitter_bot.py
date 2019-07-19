import tweepy , tkinter, datetime, os, sys, random, time, pytz
from keys import *

from tweepy import TweepError


#Create oauth handler for tokens setting
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key,secret)

api = tweepy.API(auth)

random_lyrics = 'Lyrics.txt'

time_stamp = pytz.timezone('US/Central')


#Creating a function that scans and stores the last statusID

def test_bot():

    try:
        api.verify_credentials()
        print('Authentication was successful')

    except:
        print('Error')

    user = api.me()
    print(user.name + ' ' + 'Succesfully Signing In....')
   


    mentions = api.mentions_timeline(count = 1)

    mentions_id = api.get_status

    print(mentions_id)

    for tweet in mentions:

        filesong = open(random_lyrics, 'r')
        lyrics = filesong.readlines()
        song_lines = len(lyrics)

        #Setting Counter


        random_lyric = random.randrange(0, song_lines)


        tid = tweet.user.id
        username_of_person = tweet.user.screen_name
        
        try:
             api.update_status("@" + username_of_person + ' ' + lyrics[random_lyric], in_reply_to_status_id = tid).append(time_stamp)
             print('Replied to' + ' ' + username_of_person + ' ' + 'with:'+ ' '+lyrics[random_lyric])
                      
        except tweepy.TweepError as e:
            print(e.reason)

 #LOOPS Infinately, for every 10 seconds
while True:
    test_bot()
    time.sleep(15)