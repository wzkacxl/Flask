from flask import Flask,redirect,render_template,session,url_for,flash
from flask import make_response
from flask.ext.script import Manager
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


class NameForm(Form):
	name = StringField('what is your name?',validators=[Required()])
	submit = SubmitField('Submit')

app.config['SECRET_KEY'] = 'HARD TO GUESS STRING'
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TREADOWN'] = True
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
#moment = Moment(app)
manager = Manager(app)

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(64),unique=True)
	users = db.relationship('User',backref='role')

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(64),unique=True,index=True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username


@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('you changed your name!')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template("index.html",form = form,name = session.get('name'))

@app.route('/usr/<name>')
def usr(name):
	return render_template("user.html",name = name)

@app.route('/baidu')
def baidu():
	return redirect('http://www.baidu.com')

@app.route('/time')
def time_handler():
	return render_template('time.html',current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
	return render_template('child_bootstrap.html'),404

if __name__ == '__main__':
	#manager.run()
	app.run(debug=True)