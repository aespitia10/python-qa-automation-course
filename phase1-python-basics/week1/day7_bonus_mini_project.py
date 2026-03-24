tester_name = "Your Name"
environment = "production"
test_suite_name = "E-Commerce Checkout Suite"
build_version = "v2.4.1"

test_suite = [
    {
        "test_id": "TC001",
        "test_name": "Add item to cart",
        "status": "PASS",
        "response_time": 0.543,
        "priority": "HIGH",
        "category": "Cart"
    },
    {
        "test_id": "TC002",
        "test_name": "Remove item from cart",
        "status": "PASS",
        "response_time": 0.321,
        "priority": "HIGH",
        "category": "Cart"
    },
    {
        "test_id": "TC003",
        "test_name": "Apply valid discount code",
        "status": "FAIL",
        "response_time": 1.654,
        "priority": "HIGH",
        "category": "Discount"
    },
    {
        "test_id": "TC004",
        "test_name": "Apply invalid discount code",
        "status": "PASS",
        "response_time": 0.876,
        "priority": "MEDIUM",
        "category": "Discount"
    },
    {
        "test_id": "TC005",
        "test_name": "Checkout with credit card",
        "status": "PASS",
        "response_time": 1.123,
        "priority": "HIGH",
        "category": "Payment"
    },
    {
        "test_id": "TC006",
        "test_name": "Checkout with PayPal",
        "status": "FAIL",
        "response_time": 2.543,
        "priority": "HIGH",
        "category": "Payment"
    },
    {
        "test_id": "TC007",
        "test_name": "Checkout with expired card",
        "status": "PASS",
        "response_time": 0.987,
        "priority": "HIGH",
        "category": "Payment"
    },
    {
        "test_id": "TC008",
        "test_name": "Order confirmation email sent",
        "status": "FAIL",
        "response_time": 2.876,
        "priority": "HIGH",
        "category": "Email"
    },
    {
        "test_id": "TC009",
        "test_name": "Order history updates after purchase",
        "status": "PASS",
        "response_time": 1.432,
        "priority": "MEDIUM",
        "category": "Orders"
    },
    {
        "test_id": "TC010",
        "test_name": "Cart persists after page refresh",
        "status": "PASS",
        "response_time": 0.654,
        "priority": "MEDIUM",
        "category": "Cart"
    },
    {
        "test_id": "TC011",
        "test_name": "Guest checkout works without login",
        "status": "PASS",
        "response_time": 1.234,
        "priority": "HIGH",
        "category": "Checkout"
    },
    {
        "test_id": "TC012",
        "test_name": "Checkout with invalid address",
        "status": "FAIL",
        "response_time": 0.765,
        "priority": "MEDIUM",
        "category": "Checkout"
    }
]
test_count_total = 0
test_count_failed = 0
test_count_passed = 0
test_pass_rate = 0.0
test_average_response_time = 0.0
fastes_test_time = 0.0
slowest_test_time =  0.0
test_failed_list = []
high_priority_list= []
category_checkout = 0
category_cart = 0
category_orders = 0
category_discount = 0
category_payment = 0
category_email = 0
counter = 0

for tests in test_suite:
    if tests["status"] == "PASS":
        test_count_passed += 1
    else:
        test_count_failed += 1
test_count_total = test_count_passed + test_count_failed
test_pass_rate = round((test_count_passed / test_count_total) * 100, 1)

for tests in test_suite: 
    if tests["response_time"] > 0.0: 
        test_average_response_time += tests["response_time"]
test_average_response_time = round((test_average_response_time / test_count_total),2)

for category in test_suite: 
    if category["category"] == "Checkout":
        category_checkout += 1
    elif category["category"] == "Cart":
        category_cart += 1
    elif category["category"] == "Orders":
        category_orders += 1
    elif category["category"] == "Discount":
        category_discount += 1
    elif category["category"] == "Payment":
        category_payment += 1
    else: 
        category_email += 1



print("=" *60)
print("E-COMMERCE CHECKOUT TEST REPORT")
print("=" *60)
print(f"Tester: {tester_name} \n Enviornment: {environment.upper()} \n Suite: {test_suite_name} \n Build: {build_version}")
print("=" *60)
for tests in test_suite: 
    print(f"{tests["test_id"]}: [{tests["status"]}] {tests["test_name"]} ({tests["response_time"]}) [{tests["priority"]}] [{tests["category"]}]")
print("=" *60)
print(f"Total Tests: {test_count_total} | Passed: {test_count_passed} | Failed: {test_count_failed} \nPass Rate: {test_pass_rate}% \nAverage Response Time: {test_average_response_time}s")
print(f"Fastest Response Time: {fastes_test_time} | Slowes Response Time: {slowest_test_time}")
print("=" *60)
print("CATEGORY BREAKDOWN")
print(f"Cart: {category_cart} tests \nDiscount: {category_discount} tests \nPayment: {category_payment} tests \nEmail: {category_email} tests \nOrders: {category_orders} tests \nCheckout: {category_checkout} tests")
print("=" *60)