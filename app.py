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
        a = int(a)
        b = int(b)

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b

        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
