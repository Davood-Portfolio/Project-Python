from data_loader import DataLoader
from data_processor import DataProcessor
from analytics import Analytics

DB_PATH = "../sales.db"

def show_menu():
    print("\n=== DataInsight Engine ===")
    print("1. Show all products")
    print("2. Show products sorted by price (desc)")
    print("3. Show average product price")
    print("4. Show all orders")
    print("5. Show total revenue")
    print("6. Show revenue per product")
    print("7. Show revenue per day")
    print("8. Exit")


def main():
    loader = DataLoader(DB_PATH)

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            products = loader.fetch_all("SELECT * FROM products")
            print("\nProducts:")
            for p in products:
                print(p)

        elif choice == "2":
            products = loader.fetch_all("SELECT * FROM products")
            processor = DataProcessor(products)
            sorted_products = processor.sort(key_index=2, reverse=True)

            print("\nProducts sorted by price (desc):")
            for p in sorted_products:
                print(p)

        elif choice == "3":
            products = loader.fetch_all("SELECT * FROM products")
            analytics = Analytics(products)
            avg_price = analytics.average(column_index=2)

            print(f"\nAverage product price: {avg_price:.2f}")

        elif choice == "4":
            print("Exiting...")
            break

        elif choice == "5":
            orders = loader.fetch_all("SELECT * FROM orders")
            print("\nOrders:")
            for o in orders:
                print(o)

        elif choice == "6":
            orders = loader.fetch_all("SELECT * FROM orders")
            products = loader.fetch_all("SELECT * FROM products")

            product_prices = {p[0]: p[2] for p in products}

            total_revenue = 0

            for o in orders:
                product_id = o[1]
                price = product_prices.get(product_id, 0)
                total_revenue += price

            print(f"\nTotal revenue: {total_revenue:.2f}")

        elif choice == "7":
            orders = loader.fetch_all("SELECT * FROM orders")
            products = loader.fetch_all("SELECT * FROM products")

            product_prices = {p[0]: p[2] for p in products}
            revenue_per_product = {}

            for o in orders:
                product_id = o[1]
                price = product_prices.get(product_id, 0)
                revenue_per_product[product_id] = revenue_per_product.get(product_id, 0) + price

            print("\nRevenue per product:")
            for p in products:
                pid, name, price = p
                revenue = revenue_per_product.get(pid, 0)
                print(f"{name}: {revenue:.2f}")

        elif choice == "8":
                orders = loader.fetch_all("SELECT * FROM orders")
                products = loader.fetch_all("SELECT * FROM products")

                product_prices = {p[0]: p[2] for p in products}
                revenue_per_day = {}

                for o in orders:
                    product_id = o[1]
                    date = o[2]
                    price = product_prices.get(product_id, 0)
                    revenue_per_day[date] = revenue_per_day.get(date, 0) + price

                print("\nRevenue per day:")
                for day, revenue in revenue_per_day.items():
                    print(f"{day}: {revenue:.2f}")

       
        else:
        
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
