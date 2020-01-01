from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World!'}

    def post(self):
        some_json = request.get_json()
        return {"You've sent": some_json}


class Multiply(Resource):
    def get(self, num):
        return {'result': num * 20}

api.add_resource(HelloWorld, '/')
api.add_resource(Multiply, '/multi/<int:num>')

if __name__ == "__main__":
    app.run(debug=True)