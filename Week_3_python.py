def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount,
               or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

if __name__ == "__main__":
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)
        print(f"The final price is: {final_price:.2f}")  # Format to 2 decimal places

    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount.")
