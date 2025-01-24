from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Temporary history storage
history = []

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/calculate', methods=['POST'])
def calculate():
    global history
    data = request.get_json()
    expression = data.get('expression', '')

    try:
        # Evaluate the mathematical expression
        expression = expression.replace('%', '/100')
        result = eval(expression)
        history.append(f"{expression} = {result}")
        if len(history) > 10:  # Limit history to the last 10 entries
            history.pop(0)
        return jsonify({'result': result, 'history': history})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route("/clear-history", methods=["POST"])
def clear_history():
    global history
    history.clear()  # Hapus semua history
    return jsonify({"message": "History cleared!"})

if __name__ == '__main__':
    app.run(debug=True)
