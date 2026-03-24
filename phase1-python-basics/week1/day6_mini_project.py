tester_name = "Your Name"
environment = "staging"
test_suite_name = "Login and Authentication Suite"

test_suite = [
    {
        "test_id": "TC001",
        "test_name": "Login with valid credentials",
        "status": "PASS",
        "response_time": 0.823,
        "priority": "HIGH"
    },
    {
        "test_id": "TC002",
        "test_name": "Login with invalid password",
        "status": "PASS",
        "response_time": 0.654,
        "priority": "HIGH"
    },
    {
        "test_id": "TC003",
        "test_name": "Login with empty username",
        "status": "FAIL",
        "response_time": 1.432,
        "priority": "HIGH"
    },
    {
        "test_id": "TC004",
        "test_name": "Login with empty password",
        "status": "FAIL",
        "response_time": 1.245,
        "priority": "HIGH"
    },
    {
        "test_id": "TC005",
        "test_name": "Dashboard loads after login",
        "status": "PASS",
        "response_time": 1.123,
        "priority": "MEDIUM"
    },
    {
        "test_id": "TC006",
        "test_name": "Remember me checkbox works",
        "status": "PASS",
        "response_time": 0.987,
        "priority": "LOW"
    },
    {
        "test_id": "TC007",
        "test_name": "Forgot password link works",
        "status": "FAIL",
        "response_time": 2.341,
        "priority": "MEDIUM"
    },
    {
        "test_id": "TC008",
        "test_name": "Logout clears session",
        "status": "PASS",
        "response_time": 0.432,
        "priority": "HIGH"
    },
    {
        "test_id": "TC009",
        "test_name": "Session expires after timeout",
        "status": "PASS",
        "response_time": 1.654,
        "priority": "MEDIUM"
    },
    {
        "test_id": "TC010",
        "test_name": "Login page loads under 2 seconds",
        "status": "FAIL",
        "response_time": 2.876,
        "priority": "HIGH"
    }
]


passed_tests = 0
passed_rate = 0
failed_tests = 0
average_response_time = 0.0
fastest_test_name = "null"
fastest_test_time = 0.0
slowest_test_name = "null"
slowest_test_time = 0.0
failed_tests_list = []
 
for values in test_suite:
    if values["status"] == "PASS":
        passed_tests += 1
    else:
        failed_tests += 1
        failed_tests_list.append(values)   

total_tests = passed_tests + failed_tests
passed_rate = round((passed_tests / total_tests) * 100, 3)

for values in test_suite:
    if values["response_time"] > test_suite[0]["response_time"]:
        slowest_test_name = values["test_name"] 
        slowest_test_time = values["response_time"]
    if values["response_time"] < test_suite[0]["response_time"]:
        fastest_test_name = values["test_name"]
        fastest_test_time = values["response_time"]

for values in test_suite:
    average_response_time += values["response_time"]   
average_response_time = round(average_response_time / (total_tests + 0.0), 3)
  

print("=" * 55)
print("QA TEST REPORT")
print("=" * 55)
print(f"Tester: {tester_name}")
print(f"Environment: {environment.upper()}")
print(f"Suite: {test_suite_name}")
print("=" * 55)

for values in test_suite: 
    print(f"{values['test_id']}: [{values['status']}] {values['test_name']} ({values['response_time']}s) [{values['priority']}]")
print("=" * 55)

print(f"Total Tests: {total_tests} | Passed: {passed_tests} | Failed: {failed_tests}")
print(f"Pass Rate: {passed_rate}%")
print(f"Average Response Time: {average_response_time}s")
print(f"Fastest Test: {fastest_test_name} ({fastest_test_time})s")
print(f"Slowest Test: {slowest_test_name} ({slowest_test_time})s")
print("=" * 55)

if passed_rate >= 95:
    print("OVERALL: PASS")
elif 80 <= passed_rate < 95: 
    print("OVERALL: WARN - Below target")
else:
    print("OVERALL: FAIL - Critical failure")

print("=" * 55) 
print("FAILED TESTS SUMMARY")
for values in failed_tests_list:
    print(f"{values['test_id']}: {values['test_name']} [{values['priority']}]")
print("=" * 55)

print("SLOW TEST WARNINGS")
for values in test_suite:
    if values["response_time"] > 2.0:
        print(f"{values['test_id']}: {values['test_name']} took {values['response_time']}s")
