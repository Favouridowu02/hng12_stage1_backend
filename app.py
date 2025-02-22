from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:  # Prevent issues with negative numbers
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    if n < 0:  # Prevent issues with negative numbers
        return False
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))  # Handle negative numbers correctly

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}", timeout=3)  # Add timeout
        return response.text if response.status_code == 200 else "No fun fact found."
    except requests.RequestException as e:
        return f"Error fetching fun fact: {str(e)}"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    try:
        if not number or not number.lstrip('-').isdigit():
            return jsonify({"error": "Invalid input. Please provide an integer."}), 400

        number = int(number)
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("even" if number % 2 == 0 else "odd")

        return jsonify({
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": get_fun_fact(number)
        }), 200
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500  # Debugging info

if __name__ == '__main__':
    app.run(debug=True)
