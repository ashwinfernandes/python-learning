menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Goal: print the meals with spam removed

# Approach 1: Remove spam from the list and print it
for meal in menu:
    top_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        reversed_index = top_index - index
        if item == "spam":
            del meal[reversed_index]
    print(meal)

# Approach 2: Create temporary local lists
# for menu_item in menu:
#     list_without_spam = []
#     for item in menu_item:
#         if item == "spam":
#             continue
#         list_without_spam.append(item)
#     print(list_without_spam)

# Approach 3: Print the menu without spam without removing it from the list. Print simple formatted strings
# for meal in menu:
#     list_string = "["
#     for index, item in enumerate(meal):
#         if item == "spam":
#             continue
#         list_string+= item
#         list_string+=','
#     list_string+= "]"
#     list_string = list_string.replace(",,",",")
#     list_string = list_string.replace(",]","]")
#     print(list_string)
