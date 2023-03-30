import sqlite3
from bottle import route, request, run, redirect
from time import ctime

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''
            ''')





DB = {}
def insert(user, text):
    if not user in DB:
        DB[user] = []
    DB[user].insert(0, [text,ctime(),0])



@route('/<user>/timeline')
def get_post(user):
    return DB[user]




@route('/<user>/timeline', method='POST')
def create_post(user):
    clap = request.forms.get('clap')
    insert(user, clap)

    #c.execute("(post_text)", (post_text))
    #conn.commit()
    
    redirect(request.headers.get("Referer")+f"{user}/timeline")

run(host='127.0.0.1', port=7591)



