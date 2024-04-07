from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from insert_transaction import insert
from get_transactions import get_transactions
from save_category import save_category_db
from get_categories import get_categories_db

print("Goose")
app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=["GET"])
@cross_origin()
def home():
    if request.method == "GET":
        data = {
            "status": 200,
            "message": "Server is live"
        }

        return jsonify(data)


    return "Server is working"


@app.route('/test', methods=["GET"])
@cross_origin()
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
        data = request.json
        rep = insert(user_id=data.get("user_id"), details=data.get("details"), category=data.get("category"), amount=data.get("amount"), class_=data.get("class"))
        return jsonify(rep)
    

@app.route("/get_transactions", methods=['POST'])
@cross_origin()
def get_transactions_router():

    if request.method == "POST":
        user_records = get_transactions("d14637")

        data = {
            "status": 200,
            "message": "Records retrived successfully",
            "records": user_records
        }

        return jsonify(data)

    else:
        data = {
            "status": 501,
            "message": "This is a POST route"
        }

        return jsonify(data)

@app.route("/save_category", methods=["POST"])
@cross_origin()
def save_category():
    if request.method == "POST":
        data = request.json
        print(data)
        user_category = save_category_db(name=data.get("name"), user_id=data.get("user_id"))

        print(user_category['status'])
        print("===========================================")
        if user_category['status'] == 200:
            data = {
                "status": 200,
                "message": "Route is working"
            }

            return jsonify(user_category)

        else:
            data = {
                "status": 400,
                "Message": "Category Not Saved"
            }

            return jsonify(user_category)
    else:
        data = {
                "status": 501,
                "message": "Wrong method"
        }

@app.route("/get_categories", methods=["POST"])
@cross_origin()
def get_categories():
    if request.method == "POST":
        data = request.json

        category_array = get_categories_db(user_id=data.get("user_id"))

        data = {
            "status": 200,
            "message": "Works",
            "categories": category_array
        }
        return jsonify(data)

    else:
        data = {
                "status": 400,
                "Message": "Category Not Saved"
            }

        return jsonify(data)

    

if __name__ == '__main__':
    app.run(debug=True)
