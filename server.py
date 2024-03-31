from flask import Flask,jsonify,request
from insert_transaction import insert

print("Goose")
app = Flask(__name__)



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
def insert_router():
    return insert()

if __name__ == '__main__':
    app.run(debug=True)
