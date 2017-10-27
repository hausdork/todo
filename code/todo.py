import os

#from flask import Flask
#app = Flask(__name__)

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'todo.md')

todolist = open(filename)
items = []

for line in todolist:
    items.append(line)

print(items[2:])
#@app.route('/',methods=['GET'])
#def hello_world():
#    return todolist
