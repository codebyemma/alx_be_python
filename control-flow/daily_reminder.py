Task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")