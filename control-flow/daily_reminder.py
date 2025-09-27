# daily_reminder.py

# Ask the user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a loop to ensure valid priority input
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Use a loop to ensure valid time_bound input
while time_bound not in ["yes", "no"]:
    print("Invalid input! Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Check if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
