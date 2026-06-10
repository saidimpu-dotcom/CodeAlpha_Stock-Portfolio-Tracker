# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0
portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker")

# Number of stocks user wants to add
num_stocks = int(input("How many stocks do you want to enter? "))

# User input for stock names and quantity
for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio[stock_name] = quantity

        print(f"{stock_name} added successfully!")
    else:
        print("❌ Stock not found in price list!")

# Display portfolio summary
print("\n📊 Portfolio Summary")
print("----------------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(f"{stock} - Quantity: {quantity}, Price: ${price}, Value: ${value}")

print("\n💰 Total Investment Value: $", total_investment)

# Optional: Save result to a text file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-------------------------\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(f"{stock} - Quantity: {quantity}, Price: ${price}, Value: ${value}\n")

        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("✅ Portfolio saved to portfolio_summary.txt")
else:
    print("Thank you for using Stock Portfolio Tracker!")
