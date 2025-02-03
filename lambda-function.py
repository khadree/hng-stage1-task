import json

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

def lambda_handler(event, context):
    try:
        query_params = event.get("queryStringParameters", {})
        number_str = query_params.get("number", "")

        if not number_str.isdigit():
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"number": number_str, "error": True}),
            }

        number = int(number_str)
        properties = ["even" if number % 2 == 0 else "odd"]
        if is_armstrong(number):
            properties.append("armstrong")

        response = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": False,  # Placeholder
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": f"{number} is an Armstrong number!" if is_armstrong(number) else "No special fun fact."
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)}),
        }