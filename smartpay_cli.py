def smartpay_advisor():
    print("\nWelcome to SmartPay Advisor – CLI Payment Recommender!\n")

    category = input("Enter purchase category: ")
    amount = float(input("Enter the amount: ₹"))

    wallet_offer = float(input("Enter wallet offer (%): "))
    card_cashback = float(input("Enter card cashback (%): "))
    is_upi_user = input("Are you a frequent UPI user? (Yes/No): ").strip().lower()
    wallet_balance = float(input("Enter your wallet balance: ₹"))
    card_limit = float(input("Enter your card limit: ₹"))

    print("\n📊 Analyzing best payment method...\n")

    if card_cashback >= 3 and card_limit >= amount:
        recommendation = "Card"
    elif wallet_offer >= 3 and wallet_balance >= amount:
        recommendation = "Wallet"
    elif is_upi_user == "yes" and amount <= 500:
        recommendation = "UPI"
    else:
        recommendation = "Card"

    print(f"✅ Recommended Method for {category}: {recommendation}")

# Run the tool
smartpay_advisor()