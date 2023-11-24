async def evaluate(x, y, operator):
    res = eval(f"{x} {operator} {y}")
    return res
