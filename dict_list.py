available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if chosen_part in computer_parts:
            # Remove the computer part from the list
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            # Add the computer part to the list
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

print(computer_parts)
