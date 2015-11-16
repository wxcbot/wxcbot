from twitter import Twitter, OAuth
import pickle
from authcred import token, token_secret
from authcred import consumer_key, consumer_secret
import sys
import os

def get_emoji(score):
    if score >= 10:
        return u'\U0001F4AF \n'
    elif score >= 5:
        return u'\U0001F525 \n'
    elif score >= 1:
        return u'\U0001F610 \n'
    else:
        return u'\U0001F6AB \n'

def make_message(info):
    hmoji = get_emoji(info['hconf'])
    lmoji = get_emoji(info['lconf'])
    mess = " %s %s\n"%(info['station'],info['fctime'])
    mess += "High: %d +/- %d "%(info['high'],info['hstd'])
    mess += hmoji
    diurnal = info['diurnal']
    if diurnal > 0:
        mess += "Low: %d +/- %d"%(info['low'],info['lstd'])
        mess += lmoji
    else:
        mess += u"Not normal low timing \U0001F6AB \n"
    if diurnal == 1:
        mess += u"WARNING: maybe 6z low\n"

    return mess


if __name__=='__main__':
    
    tag = 'WXC'

    tweeter = Twitter(auth=OAuth(token=token,
                                 token_secret=token_secret,
                                 consumer_key=consumer_key,
                                 consumer_secret=consumer_secret))

    info = pickle.load(os.path.expanduser('~/weatherbot/'+tag+'.fc'))

    mess = make_message(info)

    tweeter.statuses.update(status=mess)




