task = input("Enter your task: ")
priority = input("Priority (low, medium, high): ")
time-bound = input("Is it timr-bound? (yes/no): ")

match pirority:
    case "low":
        if time-bound.lower() == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time-bound.lower() == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "high":
        if time-bound.lower() == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")