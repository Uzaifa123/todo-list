# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# File that stores the to-do list data
DATA_FILE = 'data.txt'

# Function to read data from the file
def read_todo_list():
    try:
        with open(DATA_FILE, 'r') as f:
            todos = f.readlines()
        return [todo.strip() for todo in todos]
    except FileNotFoundError:
        return []

# Function to write data to the file
def write_todo_list(todo_item):
    with open(DATA_FILE, 'a') as f:
        f.write(todo_item + '\n')

# GET endpoint to return all to-do items
@app.route('/api/get-todos', methods=['GET'])
def get_todo_list():
    todos = read_todo_list()
    return jsonify(todos)

# POST endpoint to add a new to-do item
@app.route('/api/add-todo', methods=['POST'])
def add_todo():
    data = request.json
    todo_item = data.get('todo')
    if todo_item:
        write_todo_list(todo_item)
        return jsonify({'message': 'To-do item added successfully!'}), 201
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
