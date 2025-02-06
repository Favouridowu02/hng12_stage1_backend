#!/usr/bin/env python3
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timezone
from dotenv import load_dotenv

def is_prime(number: int) -> bool:
    """ This Function is used to check if a number is prime
    Argument:
        number: the number to the argument
        Return: True if the number is a prime else false
    """
    if number % 2 == 0:
        return False
    return 

def is_perfect(number: int) -> bool:
    """
        This function is used to check is a number is perfect
            Argument:
        number: the number to the argument
        Return: True if the number is a perfect else false
    """
    total = 0 
    for i in str(number):
        total += int(i)
    return total == number


# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    """
    This function returns a JSON response with email, current datetime, and GitHub URL.
    """
    return jsonify({"greetings": "welcome onboard cracker"})

@app.route('/api/classify_numbers', methods=["GET"], strict_paramter=False)
def classify_number():
    """GET /api/classify_numbers
    Description: Returns Funfacts about Numbers
    Return: A JSON Representation 
    """
    number = int(request.args.get("number"))


    information = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" 
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)