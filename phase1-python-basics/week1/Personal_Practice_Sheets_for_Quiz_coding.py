#Personal Practice Sheets for Quiz coding questions 

endpoints = [
    {"url": "/api/v1/login", "status_code": 200, "response_time": 0.432},
    {"url": "/api/v1/users", "status_code": 404, "response_time": 0.654},
    {"url": "/api/v1/products", "status_code": 200, "response_time": 1.823},
    {"url": "/api/v1/orders", "status_code": 500, "response_time": 2.341},
    {"url": "/api/v1/checkout", "status_code": 200, "response_time": 0.987}
]
total_passed = 0
total_warned = 0
total_failed = 0
fastest_response = min(endpoint["response_time"] for endpoint in endpoints)
slowest_response = max(endpoint["response_time"] for endpoint in endpoints)
average_response = round(sum(endpoint["response_time"] for endpoint in endpoints) / len(endpoints),2)


for endpoint in endpoints: 
    if endpoint["status_code"] == 200 and endpoint["response_time"] < 2.0: 
        total_passed += 1
        print(f"PASS - URL: {endpoint['url']} - {endpoint['status_code']} - {endpoint['response_time']}s")
    elif endpoint["status_code"] == 200 and endpoint["response_time"] >= 2.0:
        total_warned += 1
        print(f"WARN - URL: {endpoint['url']} - {endpoint['status_code']} - {endpoint['response_time']}s")
    else:
        total_failed += 1
        print(f"FAIL - URL: {endpoint['url']} - {endpoint['status_code']} - {endpoint['response_time']}s")   

print(f"\nTotal Passed: {total_passed}")
print(f"Total Warned: {total_warned}")
print(f"Total Failed: {total_failed}")
print(f"Fastest Endpoint: {endpoint['url']}  ({fastest_response}s)")
print(f"Slowest Endpoint: {endpoint['url']}  ({slowest_response}s)")
print(f"Average Response Time: {average_response}s")

