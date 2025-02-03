import json
import math
import urllib.request

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if n is a perfect number.
       A perfect number is a positive integer that is equal to the sum of its proper divisors.
    """
    if n < 1:
        return False
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) == n

def is_armstrong(n):
    """Check if n is an Armstrong number.
       An Armstrong number is a number that is the sum
       of its own digits each raised to the power of the number of digits.
    """
    if n < 0:
        return False
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

def digit_sum(n):
    """Return the sum of the digits of n."""
    return sum(int(d) for d in str(abs(n)))

def get_properties(n, armstrong_flag):
    """Determine the properties list."""
    parity = "odd" if n % 2 != 0 else "even"
    return ["armstrong", parity] if armstrong_flag else [parity]

def fetch_fun_fact(n):
    """Fetch a fun fact from Numbers API using urllib."""
    try:
        api_url = f"http://numbersapi.com/{n}/math?json"
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())
            return data.get("text", "")
    except Exception:
        return ""

def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    Expected event format:
      {
         "queryStringParameters": {
              "number": "371"
         }
      }
    """
    qs = event.get('queryStringParameters') or {}
    number_param = qs.get('number')

    if number_param is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"number": None, "error": True}),
            "headers": {"Content-Type": "application/json"}
        }

    try:
        n = int(number_param)
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps({"number": number_param, "error": True}),
            "headers": {"Content-Type": "application/json"}
        }

    armstrong_flag = is_armstrong(n)
    properties = get_properties(n, armstrong_flag)
    result = {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": digit_sum(n),
        "fun_fact": fetch_fun_fact(n),
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": {"Content-Type": "application/json"}
    }
