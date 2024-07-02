task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        print("'" + task + "'" + " is a high priority task that requires immediate attention today!")
    case "medium":
        print("'" + task + "'" + "is a medium priority task that should be completed within the next hour.")
    case "low":
        print("'" + task + "'" "is a low priority task. Consider completing it when you have free time.")

if time_bound == "no":
    print("'" + task + "'" + "is a low priority task. Consider completing it when you have free time.")