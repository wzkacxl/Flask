from flask import render_template
from . imprt main

@main.app_errorhander(404)
def page_not_found(e):
	return render_template('404.html'),404

@main.app_errorhander(500)
def internal_server_error(e):
	return render_template('500.html'),500

