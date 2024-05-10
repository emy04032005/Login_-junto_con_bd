from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registered')
def registered():
    return render_template('registered.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('database/test.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        user = cursor.fetchall()
        
        if user:
            conn.commit()
            conn.close() 
            return redirect(url_for('registered'))
        else:
            conn.commit()
            conn.close() 
            return render_template('register.html')
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['nombre']
        password = request.form['password']
        
        conn = sqlite3.connect('database/test.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE name=? AND password=?', (name, password))
        user = cursor.fetchone()
        
        conn.close()
        
        if user:
            return redirect(url_for('registered'))
        else:
            return render_template('login.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)