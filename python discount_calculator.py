# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate discount amount
        final_price = price - discount_amount  # Subtract discount from the original price
        return final_price  # Return the final price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))  # Get the original price
discount_percent = float(input("Enter the discount percentage: "))  # Get the discount percentage

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount is applied
print(f"The final price is: {final_price}")
# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")
