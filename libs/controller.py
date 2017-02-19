import web
import json
import libs.template

class signup:
	def GET(self):
		#db = web.database(dbn='postgres', db='db', user='postgres', pw='2339')
		# userid = db.insert('users', username="A", password="B")
		#users = db.select('auth')
		#web.setcookie('set', 'a', 3600)
		return libs.template.renderTemp('signup.html')

	def POST(self):
		post_input = web.input(_method='post')

		# Check empty values
		for key, value in post_input.items():
			if value == "":
				error = "Please, fill out all filds"
				return libs.template.renderTemp('signup.html', post_input, error)

		# Search in database
		return post_input
