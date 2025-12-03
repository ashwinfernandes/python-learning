# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter

NOT_A_NUMBER = "Not a number"
ARITHMETIC_OPERATORS = ['+', '-', '*', '/']

list_buttons = [[('C', 1), ('CE', 1)],
                [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
                [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
                [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
                [('0', 1), ('=', 2), ('/', 1)]
                ]

main_window_padding = 10

def calculate(number1: int, number2: int, operation: str) -> int:
    """Calculates the result of the operation applied to the two numbers"""
    if operation == "+":
        return number1 + number2

    if operation == "-":
        return number1 - number2

    if operation == "*":
        return number1 * number2

    if operation == "/":
        return int(number1 / number2)

    return 0


arithmetic_operation_dict = {
    "operand": '',
    "operation": ''
}


def perform_arithmetic_operation(operation: str, operand1: str, operand2: str) -> str:
    if operation == "/" and operand2 == '0':
        # divide by zero operations results in 'Not a number'
        return NOT_A_NUMBER
    elif operand1 == NOT_A_NUMBER or operand2 == NOT_A_NUMBER:
        # arithmetic operations with 'Not a number' results in 'Not a number'
        return NOT_A_NUMBER
    else:
        n1 = int(operand1) if operand1 != "" else 0
        n2 = int(operand2) if operand2 != "" else 0

        # calculate the result and then set operand to the result
        equals_result = calculate(n1, n2, operation)
        return str(equals_result)


def reset_dict() -> None:
    """Resets the arithmetic_operation_dict dictionary"""
    arithmetic_operation_dict["operand"] = arithmetic_operation_dict["operation"] = ""


def process_click(text: str):
    display = entry_text.get()
    # append entry text if txt is number
    if text.isnumeric():
        # if arith_op_dict["operation"] != "" and
        if display == arithmetic_operation_dict["operand"] or display == NOT_A_NUMBER:
            display = text
        else:
            display = display + text if display != '' and display != '0' else text
    elif text == "C":
        display = '0'
        reset_dict()
        # entry_text.set(display)
    elif text == "CE":
        display = '0'
    elif text == "=":
        if arithmetic_operation_dict["operation"] not in ARITHMETIC_OPERATORS:
            # if no previous arithmetic operations were performed then do a simple assignment
            n1 = str(display) if display != "" else 0
            arithmetic_operation_dict["operand"] = str(n1)
        else:
            arithmetic_operation_dict["operand"] = perform_arithmetic_operation(arithmetic_operation_dict["operation"], arithmetic_operation_dict["operand"], display)
            display = arithmetic_operation_dict["operand"]

        # reset the operation after evaluating the expression
        arithmetic_operation_dict["operation"] = ""

    elif text in ['+', '-', '*', '/']:
        # set the first operand to the displayed number
        if arithmetic_operation_dict["operation"] == "":
            arithmetic_operation_dict["operand"] = display
        else:
            arithmetic_operation_dict["operand"] = perform_arithmetic_operation(arithmetic_operation_dict["operation"],
                                                                                arithmetic_operation_dict["operand"],
                                         display)
            display = arithmetic_operation_dict["operand"]

        # set the operator
        arithmetic_operation_dict["operation"] = text
    else:
        display = text

    entry_text.set(display)


def clicked(btn: tkinter.Button):
    button_txt = str(btn.cget('text'))
    process_click(button_txt)


main_window = tkinter.Tk()
main_window.geometry('240x240+8+200')
main_window.title("Calculator")
main_window["padx"] = main_window_padding

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.columnconfigure(4, weight=1)
main_window.columnconfigure(5, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)
main_window.rowconfigure(4, weight=1)
main_window.rowconfigure(5, weight=1)
main_window.rowconfigure(6, weight=1)

# entry field for result
entry_text = tkinter.StringVar()
entry_text.set('0')
result = tkinter.Entry(main_window, border=2, relief="sunken", textvariable=entry_text, justify="right")
result.grid(row=0, column=0, columnspan=4, sticky="nsew")

# frame for the buttons
key_pad = tkinter.Frame(main_window)
key_pad.grid(row=1, column=0, columnspan=4, rowspan=5, sticky="nsew")
key_pad.columnconfigure(0, weight=1)
key_pad.columnconfigure(1, weight=1)
key_pad.columnconfigure(2, weight=1)
key_pad.columnconfigure(3, weight=1)

final_result = 0

row = 0
for key_row in list_buttons:
    col = 0
    for key in key_row:
        txt, column_span = key
        btn = tkinter.Button(key_pad, text=txt)
        btn.grid(row=row, column=col, columnspan=column_span, sticky=tkinter.E + tkinter.W)
        btn.config(command=lambda button=btn: clicked(button))
        col += column_span
    row += 1

main_window.update()

main_window.minsize(key_pad.winfo_width() + main_window_padding, result.winfo_height() + key_pad.winfo_height())
main_window.maxsize(key_pad.winfo_width() + 50 + main_window_padding, result.winfo_height() + 50 + key_pad.winfo_height())

main_window.mainloop()
