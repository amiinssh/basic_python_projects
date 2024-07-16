import random

# Constants
num_cashiers = 1
working_hours = 5
minutes_per_hour = 60
total_minutes = working_hours * minutes_per_hour

# Initialize counters for customers
waiting_to_order = 0
waiting_for_food = 0

# Simulate each minute of operation from 12 PM to 5 PM
for minute in range(total_minutes):
    # Customers arrive every minute and line up to order
    waiting_to_order += random.randint(0, 6)

    # Each cashier can take up to three orders per minute
    new_orders = min(num_cashiers * 3, waiting_to_order)

    # After ordering, customers wait for their food to be made
    waiting_to_order -= new_orders
    waiting_for_food += new_orders

    # Print the state at each minute
    print(f"Minute {minute + 1}: {waiting_to_order} customers waiting to order, {waiting_for_food} customers waiting for food.")

# Final state after 5 hours
print("Final state after 5 hours:")
print(f"{waiting_to_order} customers waiting to order.")
print(f"{waiting_for_food} customers waiting for food.")