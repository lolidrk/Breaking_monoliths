from flask import Flask, request as flask_request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Exponent(Resource):
    def get(self):
        number_1 = int(flask_request.args.get('param1'))
        number_2 = int(flask_request.args.get('param2'))
        return {'result': number_1 ** number_2}

api.add_resource(Exponent, '/Exponent')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5056)
