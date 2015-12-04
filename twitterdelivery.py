from twitter import Twitter, OAuth
import pickle
from authcred import token, token_secret
from authcred import consumer_key, consumer_secret
import os

def get_emoji(score):
    if score >= 2:
        return u'\U0001F4AF \n'
    elif score >= 0.2:
        return u'\U0001F525 \n'
    elif score >= 0.02:        return u'\U0001F610 \n'
    else:
        return u'\U0001F6AB \n'

def make_message(info):
    hmoji = get_emoji(info['hconf'])
    lmoji = get_emoji(info['lconf'])
    mess = " %s valid: %s\n"%(info['station'],info['fctime'])

    diurnal_high = info['diurnal_high']
    if diurnal_high > 0:
        mess += "High: %d +/- %d "%(round(info['high']),round(info['hstd']))
        mess += hmoji
    else:
        mess += u"Not normal high timing \U0001F6AB \n"
    if diurnal_high == 1:
        mess += u"WARNING: maybe 6z high\n"

    diurnal = info['diurnal']
    if diurnal > 0:
        mess += "Low: %d +/- %d"%(round(info['low']),round(info['lstd']))
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

    with open(os.path.expanduser('~/wxcbot/'+tag+'.fc'), 'r') as f:
        info = pickle.load(f)

    mess = make_message(info)

    tweeter.statuses.update(status=mess)




