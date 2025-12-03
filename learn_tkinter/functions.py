def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text))//2
    print(" " * left_margin, text)


def center_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
center_text("Spam and eggs")
center_text("Spam, spam and eggs")
center_text(12)
center_text("Spam, spam, spam and spam")

print("first", "second", 3, 4, "spam")
