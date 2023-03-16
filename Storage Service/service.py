import sqlite3
from bottle import route, request, run

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''
            ''')


DB = {}
def insert(user, text):
    if not user in DB:
        DB[user] = []
    DB[user].insert(0, text)



@route('/<user>/timeline')
def get_post(user):


    return str(DB[user])




@route('/<user>/timeline', method='POST')
def create_post(user):
    clap = request.forms.get('clap')
    insert(user, clap)

    #c.execute("(post_text)", (post_text))
    #conn.commit()
    
    return {'message': 'Post created successfully'}

run(host='localhost', port=7591)



