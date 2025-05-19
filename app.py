from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from supabase import create_client, Client
from supabase_client import supabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key='your_secret_key'

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Hash the password
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    response = supabase.table('users').insert({'username': username, 'email': email, 'password': hashed_password}).execute()
    if response.data:
      print(f"User {username} created successfully!")
      return redirect(url_for('login'))
    else:
      print(f"Failed to create user {username}.")
  return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    response = supabase.table('users').select('*').eq('username', username).execute()
    user = response.data
    print(f'User: {user}')
    
    if user and len(user) > 0:
      if check_password_hash(user[0]['password'], password):
        session['username'] = username
        return redirect(url_for('dashboard'))
      else:
        print("Invalid password")
    else:
        print("User not found")

  return render_template('login.html')


@app.route('/dashboard')
def dashboard():
  if 'username' in session:
    return render_template('dashboard.html', username=session['username'])
  return redirect(url_for('login'))  

@app.route('/logout', methods=['GET'])
def logout():
  if 'username' in session:
    session.pop('username', None)
    return redirect(url_for('login'))
  
  return render_template('home.html')

if __name__ == '__main__':
  app.run(debug=True)