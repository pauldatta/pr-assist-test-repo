from fastapi import FastAPI, HTTPException
from utils import algos

app = FastAPI()

@app.get("/fibonacci/{n}") 
async def get_fibonacci(n: int):
    """Calculates the Fibonacci sequence.""" 
    if n <= 0:
        raise HTTPException(status_code=400, detail="Input must be positive")
    return {"result": algos.fibonacci_wrong(n)}


@app.get("/factorial/{n}")
async def get_factorial(n: int):
    """Calculates a Factorial.
    
    Args:
      n: number of factorial steps
    """
    return {"result": algos.factorial_recursive(n)}


@app.get("/divide/{a}/{b}")  
async def divide(a: float, b: float):
    return {"result": a / b}


@app.post("/reverse-string")
async def reverse_string(input_string: str):
    return {"reversed": input_string[::-1]}