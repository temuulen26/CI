from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/lab15/operation/', methods=['POST'])
def calculate():
    data = request.get_json()

    a = data.get('a')
    b = data.get('b')
    operator = data.get('operator')

    if a is None or b is None or operator not in ['+', '-', '*', '/']:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        else:
            return jsonify({'error': 'Unsupported operator'}), 400

        return jsonify({'result': str(result)}), 200  # str() хийж текст болгож байна
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
