import tree

def count_tabs(line):
    number_tabs = 0
    word = ''
    while line:
        if line.startswith('\t'):
            number_tabs += 1
            line = line[1:]
        else:
            word = line
            line = ''
    return  (number_tabs, word)

def converter_for_gui(sub_directory_list):
    list_of = []
    for sub in sub_directory_list:
        sub_menue_list = [node.get_file_name() for node in tree1.find_child(sub)]
        if sub_menue_list:
            sub_elements = converter_for_gui(sub_menue_list)
            if sub_elements:
                my_tuple = (sub, sub_elements)
                list_of.append(my_tuple)
        else:
            my_tuple = (sub, [])
            list_of.append(my_tuple)

    return list_of


def clean_menu_structure(menu_structure):
    cleaned_menu_structure = []

    for menu_item in menu_structure:
        label, items = menu_item
        if items:
            cleaned_items = clean_menu_structure(items)
            cleaned_menu_structure.append((label, cleaned_items))
        else:
            cleaned_menu_structure.append(label)

    return cleaned_menu_structure

# user_input_text = input('Enter the text file: ')
user_input_text = 'input.txt'  # remove in final code
tree1 = tree.File_explorer()
tree1.insert('home')

parent_name = 'home'
current_tabs = 0
prev_tabs = -1

with open(f'{user_input_text}','r') as f:
    lines_list = f.read().split('\n') # redundent, just to see the values
    for line in lines_list:
        number_tab_and_word = count_tabs(line)
        current_tabs = number_tab_and_word[0]

        if prev_tabs == current_tabs: 
            parent_name = tree1.get_parent_data(parent_name)
        elif prev_tabs > current_tabs:
            for i in range(prev_tabs - current_tabs+1):
                parent_name = tree1.get_parent_data(parent_name)

        tree1.insert(number_tab_and_word[1],parent_name)

        parent_name = number_tab_and_word[1]
        prev_tabs = number_tab_and_word[0]

def menu_gui_maker(menu_structure,gui_code = "gui.py"):
    gui_code_list = []
    gui_code_list.append(f"""from tkinter import Tk, Menu, messagebox

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
                        
menu_structure = {menu_structure}
for menu_item in menu_structure:
    add_menu(menubar, *menu_item)
root.mainloop()""")

    with open(gui_code, "w") as file:
        for line in gui_code_list:
            file.write(line)

main_directory_list = [main.get_file_name() for main in tree1.find_child('home')] 
menu_structure = clean_menu_structure(converter_for_gui(main_directory_list))
menu_gui_maker(menu_structure)