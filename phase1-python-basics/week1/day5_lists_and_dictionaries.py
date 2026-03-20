# Day 5 - Lists and Dictionaries
# QA Automation Course - Phase 1

# ============================================
# PART 1 - Lists
# ============================================

# A list stores multiple values in order
# Square brackets [] define a list
test_cases = [
    "Verify login with valid credentials",
    "Verify login with invalid password",
    "Verify login with empty username",
    "Verify dashboard loads after login",
    "Verify logout clears session"
]
# Accessing items by index (always starts at 0)
print("First test case:", test_cases[0])
print("Last test case:", test_cases[-1])
print("Total test cases:", len(test_cases))

# ============================================
# PART 2 - List Operations
# ============================================
print("\n--- List Operations ---")

# Adding items to a list
test_cases.append("Verify forgot password link works")
print("After append:", len(test_cases), "test cases")

# Removing an item from a list
test_cases.remove("Verify logout clears session")
print("After remove:", len(test_cases), "test cases")

# Checking if an item exists in a list
if "Verify login with valid credentials" in test_cases:
    print("PASS - Test case exists in suite")
else: 
    print("FAIL - Test case does not exist in suite")   

# Sorting a list alphabetically
status_codes = [404, 200, 500, 201, 301, 200]
status_codes.sort()
print("Sorted status codes:", status_codes)

# Counting occurrences of an item
print("Times 200 appears:", status_codes.count(200))

# Slicing a list (grabbing a portion)
first_three = test_cases[0:3]
print("First 3 test cases:", first_three)

# ============================================
# PART 3 - Dictionaries
# ============================================

print("\n--- Dictionaries ---")

# A dictionary stores key:value pairs
# Curly brackets {} define a dictionary
test_result = {
    "test_name": "Login with valid credentials",
    "status": "PASS",
    "response_time": 1.23,
    "status_code": 200,
    "environment": "staging",
    "tester": "Your Name"
}
# Accessing values by key
print(f"Test Name: {test_result["test_name"]}")
print(f"Status: {test_result["status"]}")
print(f"Response Time: {test_result["response_time"]}")
print(f"Status Code: {test_result["status_code"]}")

# ============================================
# PART 4 - Dictionary Operations
# ============================================

print("\n--- Dictionary Operations ---")

# Adding a new key:value pair
test_result["browser"] = "Chrome"
print("Added browser:", test_result["browser"])

# Updating an existing value
test_result["status"] = "FAIL"
print("Updated status:", test_result["status"])

# Checking if a key exists
if "response_time" in test_result:
    print("PASS - Response time recorded")

# Getting all keys
print("All keys:", list(test_result.keys()))

# Getting all values
print("All values:", list(test_result.values()))

# Looping through a dictionary
print("\n--- Full Test Result ---")
for key, value in test_result.items():
    print(f"{key}: {value}")

# ============================================
# PART 5 - List of Dictionaries
# ============================================

print("\n--- Test Suite Results ---")
print("=" * 50)

# In real automation your results are stored as
# a list of dictionaries - one dictionary per test
test_suite = [
    {
        "test_id": "TC001",
        "test_name": "Login with valid credentials",
        "status": "PASS",
        "response_time": 0.823
    },
    {
        "test_id": "TC002",
        "test_name": "Login with invalid password",
        "status": "PASS",
        "response_time": 0.654
    },
    {
        "test_id": "TC003",
        "test_name": "Login with empty username",
        "status": "FAIL",
        "response_time": 1.432
    },
    {
        "test_id": "TC004",
        "test_name": "Dashboard loads after login",
        "status": "PASS",
        "response_time": 1.123
    },
    {
        "test_id": "TC005",
        "test_name": "Logout clears session",
        "status": "FAIL",
        "response_time": 0.987
    }
]
# Loop through and print each test result
pass_count = 0
fail_count = 0
for test in test_suite: 
    if test["status"] == "PASS":
        pass_count += 1
    else:
        fail_count += 1
    print(f"{test["test_id"]} - {test["test_name"]}: {test["status"]} ({test["response_time"]}s)")

# Print summary
print("=" * 50)
total = pass_count + fail_count
pass_rate = round((pass_count / total) * 100, 1)
print(f"Total: {total} | Passed: {pass_count} | Failed: {fail_count} | Pass Rate: {pass_rate}%")
