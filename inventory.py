products=[]
categories=("Accessories","Stationary","Storage")

# 1. Add Product
def Add_product():
    pid=int(input("Enter Product ID: "))

    for product in products:
        if product["id"]==pid:
            print("Product ID Already Exist!")
            return

    pname=input("Enter Product Name: ")

    print("Categories:",categories)
    category=input("Enter Category: ")
    if category not in categories:
        print("Invalid Category")
        return

    price=float(input("Enter Price: "))
    if price<=0:
        print("Price must be positive!")
        return
    
    stock=int(input("Enter Stock Quantity: "))
    if stock<0:
        print("Stock Cannot be negative!")
        return
    
    reorder=int(input("Enter Reorder Level: "))
    if reorder<0:
        print("Reorder level cannot be negative!")

    product={"id":pid,"Name":pname,"Category":category,"Price":price,"Stock":stock,"Reorder":reorder}
    products.append(product)
    print("Product Added Successfully!")

# 2. Display Product
def Display_product():
    if len(products)==0:
        print("No Products Available!")
        return

    print("\n-------PRODUCT INVENTORY-------")
    for product in products:
        print("ID:",product["id"])
        print("Name:",product["Name"])
        print("Category:",product["Category"])
        print("Price:",product["Price"])
        print("Stock:",product["Stock"])
        print("Reorder:",product["Reorder"])

# 3. Search Product
def Search_product():
    pid=int(input("Enter Product ID: "))
    found=False
    for product in products:
        if product["id"]==pid:
            print("Product Found!")
            print("ID:",product["id"])
            print("Name:",product["Name"])
            print("Category:",product["Category"])
            print("Price:",product["Price"])
            print("Stock:",product["Stock"])

            found=True
            break
    if not found:
        print("Product Not Found!")

# 4. Update Product
def Update_product():
    pid=int(input("Enter Product ID: "))
    for product in products:
        if product["id"]==pid:
            print("1. Update Price")
            print("2. Update Stock")
            print("3. Update Reorder Level")
            choice=int(input("Enter your choice: "))
            if choice==1:
                price=float(input("Enter New Price: "))
                if price>0:
                    product["Price"]=price
                    print("Price Updated Successfully!")
                else:
                    print("Invalid Price!")
            elif choice==2:
                stock=int(input("Enter New Stock: "))
                if stock>=0:
                    product["Stock"]=stock
                    print("Stock Upadated!")
                else:
                    print("Invalid Stock!")
            elif choice==3:
                reorder=int(input("Enter New Reorder Level: "))
                if reorder>=0:
                    product["Reorder"]=reorder
                    print("Reorder Level Updated!")
                else:
                    print("Invalid Reorder Level!")
            else:
                print("Invalid Choice!")

    return
    print("Product Not Found!")

# 5. Delete Product
def Delete_product():
    pid=int(input("Enter Product ID: "))
    for product in products:
        if product["id"]==pid:
            confirm=input("Are You Sure?(yes/no): ")
            if confirm.lower()=="yes":
                products.remove(product)
                print("Product Deleted Successfully!")
            else:
                print("Delete Cancelled!")
            return
    print("Product Not Found!")

# 6. Low Stock Report
def Low_stock_report():
    found=False

    print("\n-----LOW STOCK REPORT-----")
    for product in products:
        if product["Stock"]<=product["Reorder"]:
            print("Name:",product["Name"])
            print("Stock:",product["Stock"])
            print("Reorder Level:",product["Reorder"])
            print("Status:REORDER")

            found=True

    if found==False:
        print("No Low Stock Products!")

# 7. Inventory Summary
def Inventory_summary():
    total_products=len(products)
    total_units=0
    inventory_value=0
    category_set=set()
    for product in products:
        total_units+=product["Stock"]
        inventory_value+=product["Price"]*product["Stock"]
        category_set.add(product["Category"])

    print("\n-----INVENTORY SUMMARY-----")
    print("Total Products:",total_products)
    print("Total Stock Units:",total_units)
    print("Inventory Value: Rs.",inventory_value)
    print("Categories:",category_set)

# 8. Main Function
def main():
    while True:
        print("\n=======RETAIL INVENTORY MANAGER=======")

        print("1. Add Product")
        print("2. Display Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Report")
        print("7. Inventory Summary")
        print("8. Exit")

        choice=int(input("Enter Choice: "))
        if choice==1:
            Add_product()

        elif choice==2:
            Display_product()

        elif choice==3:
            Search_product()

        elif choice==4:
            Update_product()

        elif choice==5:
            Delete_product()

        elif choice==6:
            Low_stock_report()

        elif choice==7:
            Inventory_summary()

        elif choice==8:
            print("THANK YOU👍")
            break
        else:
            print("Invalid Choice!")

# Calling Main Function
if __name__=="__main__":
    main()
