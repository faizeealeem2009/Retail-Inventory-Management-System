# Retail Inventory Management

## Introduction

A simple python console program for track of products in a small shop by using basic python skills,like tuple,dictionary,set,if,elif,else,functions.

## What the program does?

The program shows a menu with these options:

1. Add product:-Enter product id,product name,category only in these 3 categories(Accessories,Stationery,Storage),price,stock quantity and reorder level add in products list.
2. Display product:-View all added products during run file.
3. Search product:-Find product using its ID.
4. Update product:-Enter product id and choose option and change only price,stock,reorder level.
5. Delete product:-Enter product id and confirm yes/no and delete the product.
6. Low stock product:-Show products whose reorder level greater than stock.
7. Inventory Summary:-Show Number of total products,total stock units,inventory value in rupees and categories.
8. Exit:-Close the program.

## Requirements

1. Python installed in system.
2. Terminal or command prompt or visual studio code.

## How to Run

1. Save the python program as inventory.py.
2. Open terminal and type python inventory.py and press enter.
3. Choose a number from menu and enjoy the program.

## Input Rules

1. Product id should be different for each product.
2. Category only in these 3 categories(Accessories,Stationery,Storage).
3. Price must be greater than zero.
4. Stock quantity and reorder level should not be negative.
5. When deleting a product,type yes to confirm for delete or another response to cancel.

## How data is store?

Product are kept in a python list.Each product is stored as dictionary containing its id,name,category,price,stock and reorder level.The allowed categories are kept in a tuple,and the inventory summary uses a set to collect distinct categories.

The data is stored in memory only.Products are not save in file or database,so the list becomes empty when program is closed.

## Test Cases

- [x] Duplicate Product ID is rejected.
- [x] Negative price, stock or reorder level is rejected.
- [x] Non-numeric entries do not terminate the program.
- [x] Missing ID returns a clear not-found message.
- [x] Summary equals manually calculated sample totals.
- [x] No products displays an informative empty-state message.

## Limitations

1. The program does not keep product data after it is closed.
2. It expects numeric input for menu choices,IDs,prices and quantities.Entering text in these fields can cause an input error.
3. Product names are not currently checked for blank input.
4. The program starts with an empty inventory,so products need to be entered manually before testing the reports.

## Project file

- `inventory.py` --the main python program.
