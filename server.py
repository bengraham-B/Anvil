from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from insert_transaction import insert

print("Goose")
app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/', methods=["GET"])
def home():
    if request.method == "GET":
        data = {
            "status": 200,
            "message": "Server is live"
        }

        return jsonify(data)


    return "Server is working"


@app.route('/test', methods=["GET"])
def test_server():
    if request.method == "GET":
        data = {
            "status": 200,
            "message": "Test Route Works is live"
        }

        return jsonify(data)

    return "Server is working"


@app.route('/insert', methods=['POST', 'GET'])
@cross_origin()
def insert_router():
    if request.method == "GET":
        res_data = {
            "status": "200",
            "message": "Insert is working - GET Request"
        }

        return jsonify(res_data)

    elif request.method == "POST":
        print("=============================================================")
        data = request.json
        print(data)
        print(request.get_data())
        # print(request.headers)
        rep = insert(user_id=data.get("user_id"), details=data.get("details"), category=data.get("category"), amount=data.get("amount"), class_=data.get("class"))
        return jsonify(rep)

if __name__ == '__main__':
    app.run(debug=True)
