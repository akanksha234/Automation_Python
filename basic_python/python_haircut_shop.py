hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35] #price of each haircut mentioned in hairstyles
last_week = [2, 3, 5, 8, 4, 4, 6, 2]  #number_of_customers that took each haircut
total_price = 0

#Calculating average price
for price in prices:
  total_price += price

average_price = total_price/len(prices)
print("Average price before new prices -->", average_price)

#Average price too high so to lure costomers in we need to decrease each price by 5
#using list comprehension
new_prices = [price - 5 for price in prices]
print("New Prices -----> ",new_prices)

#Calculate the revenue generated last week
total_revenue = 0

for price in prices:
  for num_of_customers in last_week:
    total_revenue += price*num_of_customers
print("Total Revenue ---->",total_revenue)

#Average revenue earned each week
average_daily_revenue = total_revenue / 7
print("Average Daily revenue",average_daily_revenue)

#to find out cuts available under 30 in new prices
cuts_under_30 = [ style for style,price in zip(hairstyles, new_prices)if price < 30]
print("Cuts under thirty are --->",cuts_under_30)
