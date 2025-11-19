from contents import pantry, recipes

print("")
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# - using dictionary comprehension
display_dict = {}
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
        for ingredient in ingredients:
            if ingredient in pantry:
                print(f"\t{ingredient} OK.")
            else:
                print(f"\tYou don't have a necessary ingredient: {ingredient}")
