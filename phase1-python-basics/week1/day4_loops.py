# Day 4 - Loops
# QA Automation Course - Phase 1

# ============================================
# PART 1 - for loops
# ============================================

# A for loop runs through a list of items one by one
# In QA terms - imagine running the same check on multiple URLs

urls_to_test = [
    "https://www.example.com/home",
    "https://www.example.com/login",
    "https://www.example.com/dashboard",
    "https://www.example.com/profile",
    "https://www.example.com/logout"
]
print("=" * 50)
print("URL VALIDATION TEST")
print("=" * 50)

for url in urls_to_test: 
    if "https" in url: 
        print(f"PASS - Secure URL: {url}")
    else:
        print(f"FAIL - Insecure URL: {url}")    

# ============================================
# PART 2 - looping with a counter
# ============================================

print("\n" + "=" * 50)
print("STATUS CODE TEST")
print("=" * 50)
status_codes = [200, 201, 404, 500, 200, 301, 200]
pass_count = 0
fail_count = 0

for code in status_codes:
    if code == 200:
        print(f"PASS - Status code {code} is OK.")
        pass_count += 1
    else:
        print(f"FAIL - Status code {code} indicates an issue.")
        fail_count += 1
print(f"\nTotal Passed: {pass_count}")
print(f"Total Failed: {fail_count}")

# ============================================
# PART 3 - while loops 
# ============================================
print("\n" + "=" * 50)
print("LOGIN RETRY TEST")
print("=" * 50)

max_attempts = 3
current_attempt = 0
login_successful = False

while current_attempt < max_attempts: 
    current_attempt += 1
    print(f"Attempt {current_attempt} of {max_attempts}...")

    if current_attempt == 2: 
        login_successful = True
        print("PASS - Login successful on attempt {current_attempt}.")
        break
    print(f"FAIL - Login failed on attempt {current_attempt}.")

if not login_successful:
    print("FAIL - All login attempts exhausted.")

# ============================================
# PART 4 - range() with for loops
# ============================================

print("\n" + "=" * 50)
print("PERFORMANCE TEST")
print("=" * 50)

import random
for test_number in range(1, 6): 
    response_time = round(random.uniform(0.5, 2.5),2)
    if response_time < 2.0:
        print(f"PASS - Test {test_number}: PASS - Response time {response_time}s ")
    else:
        print(f"FAIL - Test {test_number}: Response time {response_time}s too slow.")

# ============================================
# PART 5 - looping through a list with index
# ============================================

print("\n" + "=" * 50)
print("TEST CASE RESULTS")
print("=" * 50)

test_cases = [
    "Verify login with valid credentials",
    "Verify login with invalid password",
    "Verify login with empty username",
    "Verify dashboard loads after login",
    "Verify logout clears session"
]

results = ["PASS", "PASS", "FAIL", "PASS", "PASS"]

for index, test_case in enumerate(test_cases):
    print(f"TC{index + 1}: [{results[index]}] {test_case}")

    