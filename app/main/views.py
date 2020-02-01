from flask import render_template, abort
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	return render_template('main/user.html', user=user)