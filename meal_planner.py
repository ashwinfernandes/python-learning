from contents import pantry, recipes


def add_ingredients_to_shopping_cart(shopping_cart: dict, item: (str, int)):
    """
    Add a tuple `item` containing the ingredient and quantity to a
    `shopping_cart` dictionary. The quantity gets added to the existing ingredient
    if it's already in `the shopping cart` or a new entry is created.
    """
    food_item, quantity = item
    shopping_cart[food_item] = shopping_cart.setdefault(food_item, 0) + quantity


print("")
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# - using dictionary comprehension
display_dict = {}
shopping_list = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of recipes we know how to cook
    print("Please choose your recipe")
    print("-" * 25)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]

        for ingredient, require_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(ingredient, 0)
            if require_quantity <= quantity_in_pantry:
                print(f"\t{ingredient} OK.")
            else:
                quantity_to_buy = require_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {ingredient}")
                print(f"\tAdding {quantity_to_buy} of {ingredient} to shopping cart...")
                add_ingredients_to_shopping_cart(shopping_list, (ingredient, quantity_to_buy))

for things in shopping_list.items():
    print(things)
