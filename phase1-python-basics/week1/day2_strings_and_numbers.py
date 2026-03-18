#Day 1 - String and Numbers
#QA Automation Course - Phase 1

# --- String Operations ---
test_url_base = "https://www.example.com"
endpoint = "/login"

# Joining two strings together (called concatenation)
full_url = test_url_base + endpoint
print("Full URL:", full_url)

# Another way to join strings (called f-string, used constantly in automation)
username = "testuser"
password = "abc123"
print(f"Logging in with username: {username} and password: {password}")

# String length - how many characters are in a string
error_message = "Page not found"
print("Error message length:", len(error_message))

# Uppercase and lowercase
button_text = "Login"
print("Uppercase:", button_text.upper())
print("Lowercase:", button_text.lower())

# Check if a word exists inside a string (used heavily in QA assertions)
page_title = "Welcome to the Dashboard"
print("Contains 'Dashboard':", "Dashboard" in page_title)
print("Contains 'Login':", "Login" in page_title)

# Replace text in a string
environment = "https://staging.example.com"
production = environment.replace("staging", "production")
print("Staging URL:", environment)
print("Production UR::", production)

# --- Number Operations ---
total_tests = 100
tests_passed = 87
tests_failed = total_tests - tests_passed

# Basic math
print("\n--- Test Results ---")
print("Total Tests: ", total_tests)
print("Passed:", tests_passed)
print("Failed:", tests_failed)

# Calculating pass rate percentage
pass_rate = (tests_passed/total_tests) * 100
print(f"Pass Rate: {pass_rate}%")

# Rounding a number
response_time = 1.756432
print(f"Respond Time: {round(response_time,2)} seconds")



