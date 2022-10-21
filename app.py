from flask import Flask, render_template, request, redirect
from firebase_admin import firestore
import calendar
import time

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config/config.py')

db = firestore.client()


@app.route('/', methods=['POST', 'GET'])
def index():
    docs = db.collection('taskList').order_by('id', direction=firestore.Query.DESCENDING).get()
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    
    return render_template("Home.html", tasks = data)


@app.route("/addToList", methods=['POST', 'GET'])
def addToList():
    if request.method == 'POST':
        todo = request.form.get('todo')
        id = str(calendar.timegm(time.gmtime()))
        db.collection('taskList').document(f'{id}').set({ 'id' : id, 'data' : todo})

        return redirect('/')


@app.route("/delete/<int:id>")
def delete(id):
    db.collection('taskList').document(f'{id}').delete()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)



