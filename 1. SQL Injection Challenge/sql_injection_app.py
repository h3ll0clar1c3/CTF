# File: sql_injection_app.py
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('challenge.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS flags (id INTEGER PRIMARY KEY, flag TEXT)")
    c.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin')")
    c.execute("INSERT OR IGNORE INTO flags (id, flag) VALUES (1, 'CTF{sql_injection_flag}')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    output = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vulnerable SQL query
        conn = sqlite3.connect('challenge.db')
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        c.execute(query)
        user = c.fetchone()
        
        if user:
            output = "Welcome, admin! Here is your flag: CTF{sql_injection_flag}"
        else:
            output = "Invalid credentials!"
    
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <body>
        <h2>Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{ output }}</p>
    </body>
    </html>
    """, output=output)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)