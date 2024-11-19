from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

# Definir el endpoint /todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    
    todos.append(request_body)  # Agrega el nuevo todo a la lista
    return jsonify(todos)  # Devuelve la lista actualizada

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)
        print("Deleted task at position: {position}")

        return jsonify(todos)
    except IndexError:
        return jsonify({"error": "Position out of range"}), 400

# Mantener estas líneas al final del archivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)