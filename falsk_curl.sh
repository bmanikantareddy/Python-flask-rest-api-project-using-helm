# GET /hello
curl -X GET http://localhost:9001/hello

# GET /users
curl -X GET http://localhost:9001/users

# GET /users/<user_id>
curl -X GET http://localhost:9001/users/1

# POST /users
curl -X POST http://localhost:9001/users -H "Content-Type: application/json" -d '{"name": "Charlie", "age": 28}'

# PUT /users/<user_id>
curl -X PUT http://localhost:9001/users/1 -H "Content-Type: application/json" -d '{"name": "Alice Updated", "age": 31}'

# DELETE /users/<user_id>
curl -X DELETE http://localhost:9001/users/1
