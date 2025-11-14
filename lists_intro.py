computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball" # use direct assignment
print(computer_parts[3:])

computer_parts[3:] = "trackball" # replaces "mouse" and "mouse mat" with the iterable string resulting in [..., 'keyboard', 't', 'r', 'a', 'c', 'k', 'b', 'a', 'l', 'l']
computer_parts[3:] = ["trackball"] # replaces "mouse" and "mouse mat" with the list of strings resulting in [...., 'keyboard', 'trackball']
print(computer_parts)
