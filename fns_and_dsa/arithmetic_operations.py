def perform_operation(num, num1, opp):

    if opp == "add":
        return num + num1
    elif opp == "subtract":
        return num - num1
    elif opp == "multiply":
        return num * num1
    elif opp == "divide":
        if num == 0 or num1 == 0:
            return "Cannot divide by zero"
        else:
            return num / num1
    else:
        return "Invalid operation"