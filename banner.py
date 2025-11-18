def banner_text(text=" ", screen_width = 80):
    if not screen_width.is_integer():
        raise TypeError("The text width is not of type int. Expected integer. ")

    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the light side of life", 60)
banner_text("If life seems jolly rotten", 60)
banner_text("There's something you've forgotten", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps", 60)
banner_text("Don't be silly chumps", 60)
banner_text("Just purse your lips and whistle, that's the thing", 60)
banner_text("And...always look on the light side of life...", 60)
banner_text("*", 60)
