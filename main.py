from fastapi import FastAPI, HTTPException
from utils import algos

app = FastAPI()


@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    """
    Calculates the Fibonacci sequence up to the nth term.

    Args:
        n: The number of terms in the Fibonacci sequence to calculate.

    Returns:
        A dictionary containing the Fibonacci sequence as a list under the key "result".

    Raises:
        HTTPException: If n is not a positive integer, returns a 400 Bad Request error.
    """
    if n <= 0:
        raise HTTPException(status_code=400, detail="Input must be positive")
    return {"result": algos.fibonacci(n)}


@app.get("/power/{x}/{n}")
async def get_power(x: float, n: int):
    """
    Calculates x raised to the power of n (x^n).

    Args:
        x: The base number (float).
        n: The exponent (integer).

    Returns:
        A dictionary containing the result of x^n under the key "result".
    """
    return {"result": algos.power(x, n)}


@app.get("/factorial/{n}")
async def get_factorial(n: int):
    """
    Calculates the factorial of a non-negative integer n (n!).

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        A dictionary containing the factorial of n under the key "result".

    Raises:
        HTTPException: If n is negative, returns a 400 Bad Request error.
    """
    if n < 0:
        raise HTTPException(status_code=400, detail="Input must be non-negative")
    return {"result": algos.factorial(n)}


@app.get("/divide/{a}/{b}")
async def divide(a: float, b: float):
    """
    Divides two numbers.

    Args:
        a: The dividend (float).
        b: The divisor (float).

    Returns:
        A dictionary containing the result of a / b under the key "result".

    Raises:
        HTTPException: If b is zero, returns a 400 Bad Request error.
    """
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}


@app.post("/reverse-string")
async def reverse_string(input_string: str):
    """
    Reverses a given string.

    Args:
        input_string: The string to be reversed.

    Returns:
        A dictionary containing the reversed string under the key "reversed".
    """
    return {"reversed": input_string[::-1]}


@app.post("/concatenate-strings")
async def concatenate_strings(str1: str, str2: str):
    """
    Concatenates two strings.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        A dictionary containing the concatenated string under the key "concatenated".
    """
    return {"concatenated": str1 + str2}
