# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority (Python 3.10+)
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Add time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["medium", "low"]:
        message += ". Consider completing it when you have free time."
    else:
        message += "."

print("\n" + message)
