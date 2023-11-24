from fastapi import FastAPI;
import math

app = FastAPI();

@app.get("/")
async def findRoots(a: int, b: int, c: int):

    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    if d<0:
        return {"No Real Roots"}
    elif d==0:
        sol1 = (-b + math.sqrt(d)) / (2 * a)
        return {"Root":sol1}
    else:
        sol1 = (-b - math.sqrt(d)) / (2 * a)
        sol2 = (-b + math.sqrt(d)) / (2 * a)
        return {"Root 1":sol1, "Root 2": sol2}