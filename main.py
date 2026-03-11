#Imports the modules so their functions and variables can be used

from funtion_sale import agg_sale as sales
import initial_configuration

#It asks the user each time they add a product whether they want to enter another product;
#if not, it sends them a summary of the products they have already entered
while initial_configuration.op!= "no":
    sales()
    initial_configuration.op = str(input("Do you want to continue registering sales? ")).lower()

#The code iterates through the product list to calculate total revenue by multiplying 
#each item's price by the quantity sold and accumulating the sum in the raised variable
for i in range(len(initial_configuration.products_names)):
    total = initial_configuration.products_prices[i] * initial_configuration.quantities_sold[i]
    initial_configuration.raised += total #Accumulating the total in the 'raised' variable

#This code iterates through the product list to print a detailed summary of each item's name, quantity sold, and unit price
for i in range(len(initial_configuration.products_names)):
    print("---------------------------------------------------")
    print(f"name product: {initial_configuration.products_names[i]}, sold: {initial_configuration.quantities_sold[i]}, total raised: {initial_configuration.products_prices[i] * initial_configuration.quantities_sold[i]}")
    print("---------------------------------------------------")
#shows the total value of all sales
print(f"Total raised: {initial_configuration.raised}")