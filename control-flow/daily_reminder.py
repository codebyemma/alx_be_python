Task = input("Enter your task: ")
Time-Bound = input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
    case "low":
        if Time-Bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if Iime-Bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "high":
        if Time-Bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")