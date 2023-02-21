
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a1db07e0c878dcf8251f83ca6b9a80b51802d199a6b38eb3'
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE messages (title TEXT, content TEXT")
messagesDB = cursor.execute("SELECT title, content from messages").fetchall()

@app.route('/')
def index():
    return render_template('index.html', messages=messagesDB)


@app.route('/create/', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            cursor.execute("INSERT INTO messages VALUES (?,?)", title, content)
            return redirect(url_for('index'))

    return render_template('create.html')