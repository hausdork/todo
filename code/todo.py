import os
from flask import request
from flask import Flask
app = Flask(__name__)

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'todo.md')

items = []
incomplete = []
complete = []

todolist = open(filename, "r")
for line in todolist:
    items.append(line)
todolist.close()

for i in items:
    if i[:3] == "[ ]":
        incomplete.append(i)
    elif i[:3] == "[x]":
        complete.append(i)

# RESTful API

@app.route('/tasks',methods=['GET'])
def gettasks():
    tmp = ""
    for i in incomplete:
        tmp = tmp + i
    tmp = tmp + "\n"
    for i in complete:
        tmp = tmp + i
    return tmp

        
        
    
