# frontend.py
from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

# Frontend route to display the page
@app.route('/')
def index():
    return render_template('index.html', todos=None)

# Route to handle form submission and send data to the backend API
@app.route('/add-todo', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo')
    if todo_item:
        # Send the new to-do item to the backend API
        requests.post('http://127.0.0.1:5000/api/add-todo', json={'todo': todo_item})
    return redirect(url_for('index'))

# Route to fetch the to-do list and display it
@app.route('/get-todos', methods=['POST'])
def get_todos():
    # Fetch the current to-do list from the backend API
    response = requests.get('http://127.0.0.1:5000/api/get-todos')
    todo_list = response.json()
    return render_template('index.html', todos=todo_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
