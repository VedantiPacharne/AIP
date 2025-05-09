import matplotlib.pyplot as plt

def evaluate_performance(punctuality, teamwork, project_completion, technical_skill):
    scores = [punctuality, teamwork, project_completion, technical_skill]
    if all(score >= 4 for score in scores):
        return "Excellent"
    elif sum(score >= 3 for score in scores) >= 3 and any(score >= 4 for score in scores):
        return "Good"
    elif all(score >= 2 for score in scores):
        return "Average"
    else:
        return "Poor"

def validate_score(score):
    while score < 1 or score > 5:
        print("Invalid score. Please enter a value between 1 and 5.")
        score = int(input("Enter the score again (1-5): "))
    return score

# Input from user
num_employees = int(input("Enter number of employees to evaluate: "))
employees = []
performance_counts = {"Excellent": 0, "Good": 0, "Average": 0, "Poor": 0}

for i in range(num_employees):
    print(f"\nEnter details for Employee {i + 1}")
    name = input("Name: ")
    
    punctuality = validate_score(int(input("Punctuality (1-5): ")))
    teamwork = validate_score(int(input("Teamwork (1-5): ")))
    project_completion = validate_score(int(input("Project Completion (1-5): ")))
    technical_skill = validate_score(int(input("Technical Skill (1-5): ")))
    
    performance = evaluate_performance(punctuality, teamwork, project_completion, technical_skill)
    employees.append((name, performance))
    performance_counts[performance] += 1

# Output Report
print("\n--- Employee Performance Report ---")
for name, performance in employees:
    print(f"{name}: {performance}")

# Performance Summary
print("\n--- Performance Summary ---")
for performance, count in performance_counts.items():
    print(f"{performance}: {count} employee(s)")

# Plot Performance Distribution
labels = list(performance_counts.keys())
sizes = list(performance_counts.values())
colors = ['green', 'blue', 'orange', 'red']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Employee Performance Distribution")
plt.show()
