from flask import Flask, request, jsonify

app = Flask(__name__)

users = []  # Danh sách user lưu trong RAM (tạm thời)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if "name" in data and "email" in data:
        users.append(data)
        return jsonify({"message": "User added!", "user": data}), 201
    else:
        return jsonify({"error": "Missing data!"}), 400

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)  # Trả về danh sách user đã gửi

if __name__ == '__main__':
    app.run(debug=True)
