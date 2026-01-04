# DataInsight Engine

A professional command-line data analytics engine built with Python.  
It provides product insights, order analysis, and revenue calculations using SQLite as the data source.

## Features

- Show all products stored in the database
- Sort products by price (descending)
- Calculate average product price
- Display all customer orders
- Compute total revenue from all orders
- Analyze revenue per product
- Analyze revenue per day

## Technologies Used

- Python 3
- SQLite
- Object-Oriented Programming
- Modular CLI design

## Project Structure

```
datainsight-engine/
├── engine/
│   ├── main.py
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── analytics.py
│   └── sales.db
└── README.md
```

## How to Run

1. Navigate to the `engine` folder:

```bash
cd datainsight-engine/engine
```

2. Run the CLI:

```bash
python main.py
```

3. Use the menu to explore available options.

## Sample Menu

```
=== DataInsight Engine ===
1. Show all products
2. Show products sorted by price (desc)
3. Show average product price
4. Exit
5. Show all orders
6. Show total revenue
7. Show revenue per product
8. Show revenue per day
```

## License

This project is open-source and available under the MIT License.
