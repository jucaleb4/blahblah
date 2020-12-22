from flask import Flask, request, render_template, redirect, url_for
import groupme_fetch, parse_text
import time, json, datetime, random

app = Flask(__name__)

# to get group_id
# https://api.groupme.com/v3/groups?token=3fa5bab020ae01365acf5f17e077a979

token = "3fa5bab020ae01365acf5f17e077a979"
group_id = "49717086" # "45658198" # "40057204" # "40031922" # "40031850" # "40013007" Pledge Group Chat
CHANCE = 0.05

@app.route('/')
def home():
    return render_template('index.html', name="joe")

@app.route('/stream', methods=['GET'])
def stream():
    currVal = {}
    getMessages(currVal)
    return json.dumps(currVal)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/501')
def chores():
    ppl = ['Aditya', 'Derek', 'Nabeel', 'Wan']
    num_days = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days
    shift = (num_days//7) % 4
    next_shift = 7 - (num_days % 7)
    sex = ''
    if(random.random() < CHANCE):
        rand_idx = int(random.random() * 4)
        if(rand_idx > 3): rand_idx = 3
        msgs = ['Aditya is a rat', 'Wan def played football and hockey in hs', 'Nabeel did a great job as F/O', 'Is derej home??']
        sex = msgs[rand_idx]
    return render_template('chores.html',
            name1=ppl[shift], 
            name2=ppl[(1+shift) % 4], 
            name3=ppl[(2+shift) % 4], 
            name4=ppl[(3+shift) % 4], 
            queue=next_shift, secret=sex)

def getMessages(curr):
    # returns dictionary
    d = groupme_fetch.main2(group_id, token)
    print(d)
    # print data for testing, get index
    # temp = parse_to_google.data_parse(d, curr, i)
    # changes curr
    parse_text.data_parse(d, curr)

if __name__ == '__main__':
    app.run()
