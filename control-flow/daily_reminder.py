task = input("Enter the description of the task at hand: ")
pirority = input("Enter the priority for this task (low, medium, high): ")
time_sensitive = input("Is this task time-sensitive? (yes/no): ")

match pirority:
    case "low":
        if time_sensitive.lower() == "yes":
            print(f"Reminder: {task} is a {pirority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {pirority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_sensitive.lower() == "yes":
            print(f"Reminder: {task} is a {pirority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {pirority} priority task. Consider completing it when you have free time.")
    case "high":
        if time_sensitive.lower() == "yes":
            print(f"Reminder: {task} is a {pirority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {pirority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")