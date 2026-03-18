# Day 3 - Conditionals
# QA Automation Course - Phase 1

# --- Basic if/else ---

test_passed = 75
total_test = 100
pass_rate = (test_passed / total_test) * 100

if pass_rate >= 80: 
    print(f"PASS - Test suite passed with {round(pass_rate, 1)}%")
else:    
    print(f"FAIL - Test suite failed with {round(pass_rate, 1)}%")

# --- if/elif/else (multiple conditions) ---
http_status_code = 500

if http_status_code == 200:
    print("Status: OK - Page loaded successfully.")
elif http_status_code == 404:
    print("Status: Not Found - Page does not exist.")
elif http_status_code == 500:
    print("Status: Server Error - Something went wrong.")
elif http_status_code == 401:
    print("Status: Unauthorized - Invalid credentials.")
else:
    print(f"Status: Unknown - Unexpected status code {http_status_code}")

# --- Combining conditions with and / or / not  ---
is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Access granted - Admin dashboard.")
elif is_logged_in and not is_admin:
    print("Access granted - Standard dashboard.")
else:
    print("Access denied - Please log in.")

# --- Real QA scenario 1 - checking a login response ---
expected_url = "https://www.example.com/dashboard"
actual_url = "https://www.example.com/dashboard"
response_time = 2.5

print("\n--- Login Test Result ---")
if actual_url == expected_url and response_time < 2.0:
    print(f"PASS - Redirected to {actual_url} in {response_time}s.")
elif actual_url == expected_url and response_time >= 2.0:
    print(f"WARN - Correct page but slow response: {actual_url} but slow response ({response_time}s).")
else:
    print(f"FAIL - Wrong URL. Expected {expected_url} but got {actual_url}.")

# --- Real QA scenario 2 - form validation ---
print("\n--- Form Validation Test ---")
username_input = "testuser"
password_input = "abc"
username_min_length = 6
password_min_length = 6

if len(username_input) >= username_min_length and len(password_input) >= password_min_length:
    print("PASS - Username and password meet minimum length requirements.")
else: print(f"FAIL - Username or password are too short.")

print("\n--- API Response Test ---")
api_response_code = 401
api_response_time = 0.432
api_response_body = "success"

if api_response_code == 200 and api_response_time < 1.0 and "success" in api_response_body:
    print(f"PASS - API returned {api_response_code} in {api_response_time}s with correct body.")
else:
    print(f"FAIL - API test failed with Code: {api_response_code}, | Time {api_response_time}s, | Body: {api_response_body}")

