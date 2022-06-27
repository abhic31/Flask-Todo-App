from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'


db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self) -> str:
        return f"Todo('{self.sno}', '{self.title}')"

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    alltodo = Todo.query.all()
    return render_template('index.html',alltodo = alltodo)

@app.route("/Update/<int:sno>", methods = ['GET', 'POST'])
def Update():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.commit()
        return redirect('/')
    
    

@app.route("/Delete/<int:sno>", methods = ['GET', 'POST'])
def Delete():
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run()
    app.run(debug=True)
    