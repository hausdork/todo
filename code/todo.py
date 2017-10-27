#from flask import Flask
#app = Flask(__name__)

todolist = open("G:\\git\\code\\todo.md")
items = []

for line in todolist:
    items.append(line)

print(items[2:])
#@app.route('/',methods=['GET'])
#def hello_world():
#    return todolist
