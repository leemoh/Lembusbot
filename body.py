

import random
import json, requests

import re


def text(input_text):
    d=["farewell","adieu","hooray","au revoir","ciao","auf Wiedersehen","adios","bye",'kwaheri',"see you","cheers"]

    w="Welcome,Have a good Day"

    l='My name is LembusBot. I am in development stage right now sorry if i dont understand you well but you can reach out to my developer at @Mclnerney.'

    subreddit = 'LifeProTips'

    r = requests.get(
    'http://www.reddit.com/r/{}.json'.format(subreddit),
    headers={'user-agent': 'Mozilla/5.0'}
    )


    n=[]
    for post in r.json()['data']['children']:
        n.append((post['data']['title']))

    if (input_text).lower()=='bye':
        return (random.choice(d)).title()
    elif input_text.lower() in ["fuck","boring","kwera","lala"]:
        return(l)
    elif (input_text).lower() in ['thank you','asante','thanks']:
        return w
    else:
        #return (random.choice(n),localtime)
        return re.sub('[(){}<>]', '', (random.choice(n)))
