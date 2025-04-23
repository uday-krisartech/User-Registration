from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import os

app = Flask(__name__)

# Database connection setup
def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amogh_sql",
        database="login"
    )

@app.route('/', methods=['GET', 'POST'])
def register():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check for existing email
        cursor.execute("SELECT * FROM USERS WHERE email = %s", (email,))
        existing = cursor.fetchone()

        if existing:
            flash('Email ID already exists', 'info')
        else:
            cursor.execute("INSERT INTO USERS (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, password))
            conn.commit()
            flash('Account created successfully!', 'success')

    cursor.close()
    conn.close()
    return render_template('Register.html')

if __name__ == '__main__':
    app.run(debug=True)
