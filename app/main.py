from flask import Flask,render_template
import sqlite3


app = Flask(__name__)

# @app.route("/")
# # def hello_world():
# #     return "<p>Hello, World!</p>"
# def index():
#     return render_template('index.html')
@app.route('/hello')
def hello():
    return 'Hello, World'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)