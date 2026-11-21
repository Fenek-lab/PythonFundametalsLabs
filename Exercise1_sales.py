# Step 1 - Create and run a Python File
print("*****Python Foundation Lab Start*****") # print function

#Step 2 - Create variables and data type
product = "Laptop" # string variable
quantity = 3 # int variable
unit_price = 666.50 # float variable
in_stock = True # boolean variable

print("Product:", product)
print("Quantity:", quantity)
print("Price:", unit_price)
print("In stock:", in_stock)

print("***** Variable Values *****")
print(type(product))
print(type(quantity))
print(type(unit_price))
print(type(in_stock))

# Step 3 - Perform a sales calculation
total_sales = quantity * unit_price # calculate total sales

print ("Product:", product)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("Total Sales:", total_sales)

#Step 4 - Apply Condtional Statements
if total_sales >= 2000:
    print("Sales target achived!")
else:
    print("Sales target not achived. Keep trying!")

# Step 5 - Process Multiple Sales using loop
sales = [1200, 850, 2400, 1750, 3200] # list of sales amounts
print("****** Processing Multiple Sales ******")
for sale in sales:
    if sale >= 2000:
        print(f"Sale amount {sale} - Target achieved!")
    else:
        print(f"Sale amount {sale} - Target not achieved. Keep trying!")