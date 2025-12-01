try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test() # used to test existence of tkinter

main_window = tkinter.Tk()

main_window.title("Hello World")
main_window.geometry('640x480+8+400')
main_window.mainloop()
