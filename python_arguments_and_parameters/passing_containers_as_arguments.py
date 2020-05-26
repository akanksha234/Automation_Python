from python_arguments_and_parameters.keyword_arguments import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}

#if we want to pass a dictionary or a list to the method and want it to work as args or kwargs we have
#to pass it as * and **
# Call create_product() by passing new_product_dict
# as kwargs!
create_products(**new_product_dict)