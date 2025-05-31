# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process based on priority using match-case
match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
