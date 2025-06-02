def crypto_advisor():
    # Predefined crypto dataset
    crypto_db = {
        "Bitcoin": {
            "price_trend": "rising",
            "market_cap": "high",
            "energy_use": "high",
            "sustainability_score": 3/10
        },
        "Ethereum": {
            "price_trend": "stable",
            "market_cap": "high",
            "energy_use": "medium",
            "sustainability_score": 6/10
        },
        "Cardano": {
            "price_trend": "rising",
            "market_cap": "medium",
            "energy_use": "low",
            "sustainability_score": 8/10
        }
    }

    # Chatbot introduction
    print("🌟 Welcome to CryptoBuddy, your AI-powered financial sidekick! 🌟")
    print("Ask me about crypto trends or sustainability! (Type 'exit' to quit)")
    print("Example questions: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'")
    print("⚠️ Disclaimer: Crypto is risky—always do your own research!")

    while True:
        # Get user input
        user_query = input("\nYou: ").lower().strip()

        # Exit condition
        if user_query == "exit":
            print("CryptoBuddy: Thanks for chatting! Stay savvy! 🚀")
            break

        # Initialize response
        response = "CryptoBuddy: Hmm, let me think... 🤔 "

        # Logic for handling queries
        if "trending up" in user_query or "profitable" in user_query or "buy for growth" in user_query:
            # Prioritize rising price_trend and high market_cap
            profitable_coins = [
                coin for coin, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["market_cap"] == "high"
            ]
            if profitable_coins:
                response += f"Invest in {profitable_coins[0]}! It’s trending up with a high market cap! 🚀"
            else:
                response += "Cardano is a great pick! It’s rising and has strong potential! 🚀"
        elif "sustainable" in user_query or "eco-friendly" in user_query:
            # Prioritize low energy_use and sustainability_score > 7/10
            sustainable_coin = max(
                crypto_db,
                key=lambda x: crypto_db[x]["sustainability_score"]
            )
            if crypto_db[sustainable_coin]["sustainability_score"] > 7/10:
                response += f"Invest in {sustainable_coin}! 🌱 It’s eco-friendly with a sustainability score of {crypto_db[sustainable_coin]['sustainability_score']*10}/10!"
            else:
                response += "Cardano is the most sustainable option with low energy use! 🌱"
        elif "info" in user_query or "details" in user_query:
            # Provide details about a specific coin
            for coin in crypto_db:
                if coin.lower() in user_query:
                    data = crypto_db[coin]
                    response += f"{coin}: Price trend: {data['price_trend']}, Market cap: {data['market_cap']}, Energy use: {data['energy_use']}, Sustainability: {data['sustainability_score']*10}/10"
                    break
            else:
                response += "Please specify a coin (e.g., Bitcoin, Ethereum, Cardano)."
        else:
            response += "I’m not sure what you mean. Try asking about trends, sustainability, or a specific coin!"

        print(response)

# Run the chatbot
if __name__ == "__main__":
    crypto_advisor()
