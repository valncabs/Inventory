#This part of the code asks the user to enter information for each product

import initial_configuration

def  agg_sale():
        product_name = str(input("Enter the product name: "))
        initial_configuration.products_names.append(product_name)
        product_price= float(input("Enter the product price: "))
        initial_configuration.products_prices.append(product_price)
        quantity_sold = int(input("Enter the number of products sold: "))
        initial_configuration.quantities_sold.append(quantity_sold)




