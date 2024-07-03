task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))
match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:", "'",task,"'", "is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Reminder:", "'", task, "'", "is a high priority task. Consider completing it when you have free time.")
        else:
            print("Invalid! Please assign appropriate priority")
    case "medium":
        if time_bound == "yes":
            print("Reminder:", "'", task, "'", "is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Reminder:", "'", task, "'", "is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Invalid! Please assign appropriate priority")
    case "low":
        if time_bound == "yes":
            print("Reminder:", "'", task, "'", "is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Reminder:", "'", task, "'", "is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid! Please assign appropriate priority")
