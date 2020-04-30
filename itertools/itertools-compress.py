from itertools import compress

selected_toppings = compress(
    ["Tomato", "Cheese", "Onions", "Ham", "Jalapenos"], [True, False, 1, 0, "Yes"]
)
for topping in selected_toppings:
    print(topping)  # Tomato, Onions, Jalapenos
