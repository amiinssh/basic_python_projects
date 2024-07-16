import random

num_cashiers = 1
num_cooks = 2
total_num_served = 0

total_minutes = 5 * 60

waiting_to_order = 0
waiting_for_food = 0

for minute in range(total_minutes):
    # Customers arrive every minute and line up to order
    waiting_to_order = waiting_to_order + random.randint(0, 6)
    
    # Each cashier can take up to three orders per minute
    new_orders = min(num_cashiers * 3, waiting_to_order)
    
    # Each cook can fill up to two orders per minute
    filled_orders = min(num_cooks, waiting_for_food)

    # After ordering, customers wait for their food to be made
    waiting_to_order = waiting_to_order - new_orders
    waiting_for_food = waiting_for_food + new_orders
    waiting_for_food = waiting_for_food - filled_orders
    total_num_served += filled_orders
    print(f"At minute {minute + 1}:")
    print(str(waiting_to_order) + " customers waiting to order")
    print(str(waiting_for_food) + " customers waiting for food")
print(str(total_num_served) + " customers served")