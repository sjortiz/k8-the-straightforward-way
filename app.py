from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {"Message": "Hello World!"}

api.add_resource(HelloWorld, '/')

app.run(host='0.0.0.0')
