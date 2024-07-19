from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data store
data_store = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25}
}

# Endpoint to get a greeting
@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        data = {"data": "Hello World"}
        return jsonify(data)

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data_store)

# Endpoint to get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_store.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    if not user_data or not user_data.get("name") or not user_data.get("age"):
        return jsonify({"error": "Invalid input"}), 400
    
    new_id = max(data_store.keys()) + 1
    data_store[new_id] = {
        "name": user_data["name"],
        "age": user_data["age"]
    }
    return jsonify({"id": new_id}), 201

# Endpoint to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    if not user_data or not user_data.get("name") or not user_data.get("age"):
        return jsonify({"error": "Invalid input"}), 400
    
    user = data_store.get(user_id)
    if user:
        data_store[user_id] = {
            "name": user_data["name"],
            "age": user_data["age"]
        }
        return jsonify(data_store[user_id])
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in data_store:
        del data_store[user_id]
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)