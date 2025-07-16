import re

def assess_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                        number_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_case_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_case_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&).")

    return strength, feedback

# Example usage
password = input("Enter a password to assess its strength: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for message in feedback:
        print(f"- {message}")