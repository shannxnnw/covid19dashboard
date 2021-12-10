from flask import Flask
from flask import render_template
from flask import request
import logging

import sched
import time


app = Flask(__name__)

s = sched.scheduler(time.time, time.sleep)

news = [{"title": "TITLE EXAMPLE", "content": "CONTENT EXAMPLE"},{"title": "TITLE EXAMPLE 2", "content": "CONTENT EXAMPLE2"}]

def add_news_article():
    """ Adds a new news article to the dashboard """
    news.append({'title': "T", 'content': "C"})

def schedule_add_news(up):
    """ Schedules the newly added news article to be added to the dashboard """
    e1 = s.enter(up,1,add_news_article)



def hours_to_minutes( hours: str) -> int:
    """Converts hours to minutes"""
    return int(hours)*60

def minutes_to_seconds( minutes: str) -> int:
    """Converts minutes to seconds"""
    return int(minutes)*60

def hhmm_to_seconds( hhmm: str ) -> int:
    """ converts hours and minutes format to seconds """
    if len(hhmm.split(':')) != 2:
        print('Incorrect format. Argument must be formatted as HH:MM')
        return None
    return minutes_to_seconds(hours_to_minutes(hhmm.split(':')[0])) + \
           minutes_to_seconds(hhmm.split(':')[1])


def hhmmss_to_seconds( hhmmss: str ) -> int:
    """ converts hours, minutes and seconds format to seconds """
    if len(hhmmss.split(':')) != 3:
        print('Incorrect format. Argument must be formatted as HH:MM:SS')
        return None
    return minutes_to_seconds(hours_to_minutes(hhmmss.split(':')[0])) + \
           minutes_to_seconds(hhmmss.split(':')[1])
        
@app.route('/index')
def hello():
    """ this function takes the html template and runs it
    whilst using the scheduler to update and blocking/threading to run in general
    """
    s.run(blocking=False)
    text_field =  request.args.get('two')
    print(text_field)
    if text_field:
        update_time = request.args.get('update')
        print(update_time)
        update_time_sec = hhmm_to_seconds(update_time)
        schedule_add_news(update_time_sec)
    return render_template('index.html', title='Daily update', news_articles= news)


if __name__ =='__main__':
    app.run()

logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so') # will not print anything
logging.basicConfig(filename='sys.log', encoding='utf-8')
