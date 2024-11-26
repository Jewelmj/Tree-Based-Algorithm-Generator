from tkinter import Tk, Menu, messagebox

def add_menu(menu, label, items):
    sub_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label=label, menu=sub_menu)
    for item in items:
        if isinstance(item, tuple):
            add_menu(sub_menu, *item)
        else:
            # Add a command with a dedicated callback function
            sub_menu.add_command(label=item, command=lambda item=item: menu_callback(item))

def menu_callback(label):
    messagebox.showinfo("Menu Clicked", "You clicked on "+label)

root = Tk()
root.title('Dynamic Menu Demo')

menubar = Menu(root)
root.config(menu=menubar)
                        
menu_structure = [('jewel', [('five', ['eight', ('nine', ['ten'])]), 'six', ('seven', ['eleven', ('twelve', ['thirteen', 'fourteen', 'fifteen'])])]), ('two', ['sixteen', 'seventeen', ('eighteen', [('nineteen', ['twenty']), ('twentyone', ['twentytwo', 'twentythree'])])]), ('three', ['twentyfour', 'twentyfive', 'twentysix']), ('four', ['twentyseven', ('twentyeight', ['twentynine', 'thirty', 'thirtyone', ('thirtytwo', ['thirtythree', 'thirtyfour', 'thirtyfive'])]), ('thirtysix', ['thirtyseven', 'thirtyeight']), 'thirtynine', 'forty'])]
for menu_item in menu_structure:
    add_menu(menubar, *menu_item)
root.mainloop()