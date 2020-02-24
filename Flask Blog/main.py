from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/mecode'
db=SQLAlchemy(app)

class Posts(db.Model):
	sno=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(40), nullable=True)
	email=db.Column(db.String(40), nullable=False)
	phone=db.Column(db.Integer, nullable=True)
	msg=db.Column(db.String(40), nullable=True)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
	if request.method=="POST":
		name=request.form.getlist('name')
		email=request.form.getlist('email')
		phone=request.form.getlist('phone')
		msg=request.form.getlist('msg')

		entry=Posts(name=name, email=email, phone=phone, msg=msg)
		db.session.add(entry)
		db.session.commit()
	return render_template('contact.html')

@app.route('/post')
def post():
	return render_template('post.html')

if __name__ == '__main__':
    app.debug = True
    app.run()