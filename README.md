# Number Classification API

## Overview
This is a Flask-based API that classifies numbers based on their mathematical properties. It checks if a number is prime, perfect, Armstrong, even or odd, and also provides the sum of its digits along with a fun fact from the Numbers API.

## Features
- Check if a number is **prime**.
- Check if a number is **perfect**.
- Check if a number is an **Armstrong number**.
- Determine if a number is **even** or **odd**.
- Compute the **digit sum** of a number.
- Retrieve a **fun fact** about the number from the Numbers API.

## Technologies Used
- **Python**
- **Flask**
- **Flask-CORS**
- **Requests**

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended). You also need to install Flask and other dependencies.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/number-classification-api.git
   cd number-classification-api
   ```

2. Install dependencies:
   ```sh
   pip install flask flask-cors requests
   ```

3. Run the application:
   ```sh
   python app.py
   ```

The API will start on `http://127.0.0.1:5000/`

## API Endpoints
### `GET /api/classify-number`
#### Description
Classifies a given number based on its mathematical properties.

#### Request Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `number`  | int  | Yes      | The number to classify |

#### Example Request
```sh
GET http://127.0.0.1:5000/api/classify-number?number=28
```

#### Example Response
```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even"],
  "digit_sum": 10,
  "fun_fact": "28 is the number of dominoes in a standard set."
}
```

## Functions Explanation
### `is_prime(n) -> bool`
Checks if a given number is prime.

### `is_perfect(n) -> bool`
Checks if a given number is perfect (sum of its divisors equals the number itself).

### `is_armstrong(n) -> bool`
Checks if a given number is an Armstrong number (sum of its digits raised to the power of its length equals the number).

### `digit_sum(n) -> int`
Computes the sum of the digits of a number.

### `get_fun_fact(n) -> str`
Fetches a fun fact about the number from [Numbers API](http://numbersapi.com/).

## License
This project is open-source and available under the MIT License.

## Author
[Your Name] - [GitHub Profile](https://github.com/yourusername)

