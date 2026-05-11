import yfinance as yf
import pandas as pd
import os

class StockExpertSystem:
    def __init__(self, filename="expert_report.csv"):
        self.filename = filename

        # Knowledge Base Rules
        self.rules = [

            {"signal": "BUY", "condition": lambda p, sma: p < (sma * 0.98), "reason": "Price is below the 50-day SMA."},
            {"signal": "SELL", "condition": lambda p, sma: p > (sma * 1.05), "reason": "Price is 5% above the 50-day SMA."},
            {"signal": "HOLD", "condition": lambda p, sma: True, "reason": "Stable market trend."},
        ]

    def analyze_stock(self, ticker):
        ticker = ticker.strip().upper()

        try:

            stock = yf.Ticker(ticker)
            hist = stock.history(period="60d")

            if hist.empty:
                print(f"Error: No data found for {ticker}")
                return None

            price = hist["Close"].iloc[-1]
            sma = hist["Close"].mean()

            # Inference Engine
            for rule in self.rules:

                if rule["condition"](price, sma):
                    return {
                        "Ticker": ticker,
                        "Price": round(price, 2),
                        "SMA_50": round(sma, 2),
                        "Decision": rule["signal"],
                        "Reason": rule["reason"],
                    }

        except Exception as e:
            print(f"Technical error with {ticker}: {e}")
            return None

    def save_to_csv(self, data):
        df = pd.DataFrame([data])

        # 'a' mode appends data, header is only written if file doesn't exist
        file_exists = os.path.isfile(self.filename)
        df.to_csv(self.filename, mode='a', index=False, header=not file_exists)
        print(f"Done! {data['Ticker']} has been added to {self.filename}.")

    #Switch-Case Simulation Logic


def main():
        expert = StockExpertSystem()

        while True:

            print("\n- STOCK MARKET EXPERT SYSTEM -")
            print("1. Analyze & Save a New Stock")
            print("2. View Current CSV Report")
            print("3. Clear CSiV File")
            print("4. Exit")

            choice = input("Select an option (1-4): ")

            if choice == "1":
                ticker = input("Enter Stock Ticker (e.g., RELIANCE.NS or TSLA): ")
                result = expert.analyze_stock(ticker)

                if result:
                    print(f"\nResult: {result['Decision']} ({result['Reason']})")
                    expert.save_to_csv(result)

            elif choice == "2":
                if os.path.exists(expert.filename):
                    df = pd.read_csv(expert.filename)
                    print("\n- CURRENT SAVED DATA -")
                    print(df)
                else:
                    print("\nReport file is empty.")

            elif choice == "3":
                if os.path.exists(expert.filename):
                    os.remove(expert.filename)
                    print("\nFile cleared.")
                else:
                    print("\nNo file to clear.")

            elif choice == "4":
                print("Exiting Expert System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()