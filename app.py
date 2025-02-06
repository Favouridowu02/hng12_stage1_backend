#!/usr/bin/env python3
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timezone
from dotenv import load_dotenv

app = Flask(__name__)


def is_prime(number: int) -> bool:
    """ This Function is used to check if a number is prime
    Argument:
        number: the number
        Return: True if the number is a prime else false
    """
    if number % 2 == 0:
        return False
    return 

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        return response.text if response.status_code == 200 else "No fun fact found."
    except requests.RequestException:
        return "Error fetching fun fact."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400
    
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
    })

if __name__ == '__main__':
    app.run()
