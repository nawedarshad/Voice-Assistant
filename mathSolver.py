import data
result = 0

def solve(command, req):
    global result

    if req.lower() in ["add", "sum", "calculate", "plus"]:
        result = sum(command)
    
    elif req.lower() in ["subtract", "difference", "minus"]:
        result = command[0] - sum(command[1:])
    
    elif req.lower() in ["multiply", "product", "times"]:
        result = 1
        for i in command:
            result *= i
    
    elif req.lower() in ["divide", "quotient", "divided by"]:
        result = command[0]
        for i in command[1:]:
            result /= i

    return result