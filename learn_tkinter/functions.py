def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text))//2
    print(" " * left_margin, text)


def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = text.removesuffix(sep)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


with open("centered", mode='w') as centered_file:
    # call the function
    center_text("Spam and eggs", file=centered_file)
    center_text("Spam, spam and eggs", file=centered_file)
    center_text(12, file=centered_file)
    center_text("Spam, spam, spam and spam", file=centered_file)

    # print("first", "second", 3, 4, "spam")
    center_text("first", "second", 3, 4, "spam", sep=':', file=centered_file)
