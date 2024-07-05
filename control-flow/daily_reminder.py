task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "mediu":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case_:
        reminder = "Invalid priority. Please enter high, medium or low."
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
    print(f'Reminder: {reminder}')
elif time_bound == "no":
    reminder += "Consider completing it when you have free time."
    print(f"Note: {reminder}")
