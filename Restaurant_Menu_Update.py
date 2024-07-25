# Restaurant Menu Dictionary
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
}
# Update the restaurant menu dictionary with new items and prices.
restaurant_menu.update({"Beverages": {"Water": 0.99, "Dr.Pepper": 1.99}})

# Update the prices of existing menu items.
restaurant_menu ["Main Course"] ["Steak"] = 17.99

# Delete a menu item.
del restaurant_menu["Starters"]["Bruschetta"]

# Display the updated restaurant menu.
print(restaurant_menu)
