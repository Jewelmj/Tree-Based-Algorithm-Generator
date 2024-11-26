class Node:
    def __init__(self, file_name) :
        self.file_name = file_name 
        self.left = self.right = None  # left is a child rigth is a sibling
        self.parent = None
        
    def get_file_name(self):
        return self.file_name 
    
    def set_file_name(self, file_name):
        self.file_name = file_name
    
    def get_left(self):
        return self.left
    
    def set_left(self, left):
        self.left = left
        
    def get_right(self):
        return self.right 
    
    def set_right(self, right):
        self.right = right
    
    def get_parent(self):
        return self.parent 
    
    def set_parent(self, parent): 
        self.parent = parent
    
        
class File_explorer:
    def __init__(self) :
        self.home_page = None 
    
    @staticmethod
    def _search_node(root, parent_data) :
        if root is None :
            pass
        elif root.get_file_name() == parent_data: # reached parent
            return root
        else:
            parent =  File_explorer._search_node(root.get_left(),parent_data)
            if parent is None:
                parent = File_explorer._search_node(root.get_right(),parent_data)
            return parent

    @staticmethod
    def _insert_to_parent(root, temp, parent_node) :
        if root is None :
            parent_node.set_left(temp)
            temp.set_parent(parent_node)
        elif root.get_right() is None: 
            root.set_right(temp)
            temp.set_parent(root)
        else:
            File_explorer._insert_to_parent(root.get_right(), temp, parent_node)


    def insert(self, data, parent_data = None) :  
        temp = Node(data)
        if self.home_page is None:
            self.home_page = temp
            return self
        parent_node = File_explorer._search_node(self.home_page, parent_data)
        File_explorer._insert_to_parent(parent_node.get_left(), temp, parent_node)

    @staticmethod
    def _find_parent(node):
        curent_node = node
        parent_node = node.get_parent()
        while parent_node.get_right() and parent_node.get_right() == curent_node: 
            curent_node = parent_node
            parent_node = parent_node.get_parent()
        return parent_node

    def get_parent_data(self,node_data):
        if self.home_page is None:
            print('Tree is empty')
            return None
        node = File_explorer._search_node(self.home_page,node_data)
        parent_node = File_explorer._find_parent(node)
        return parent_node.get_file_name()
    
    @staticmethod
    def _display_working_directory(root,spacing=' '):
        if root is None:
            return None
        print(spacing,root.get_file_name())
        File_explorer._display_working_directory(root.get_left(), spacing+'--')
        File_explorer._display_working_directory(root.get_right(), spacing)


    def display_working_directory(self, working_directory): # for step 1, a
        if self.home_page is None:
            return print('Empty tree')
        node = File_explorer._search_node(self.home_page, working_directory)
        File_explorer._display_working_directory(node.get_left(), '')

    def find_directory(self, directory_data): # for step 1, b
        if self.home_page is None:
            return print('Empty tree')
        directory_node = File_explorer._search_node(self.home_page, directory_data)
        return directory_node
    
    @staticmethod
    def _find_node_equal_level(root, parent_node, child_list) :
        if root is None :
            return child_list
        child_list.append(root)
        return File_explorer._find_node_equal_level(root.get_right(), parent_node, child_list)
    
    def find_child(self,node_data): # for step 1, c
        if self.home_page is None:
            return print('Tree is empty')
        current_node = File_explorer._search_node(self.home_page,node_data)
        child_list = File_explorer._find_node_equal_level(current_node.get_left(), current_node, [])
        return child_list
    
    def find_sibling(self,node_data):  # for step 1, d
        if self.home_page is None:
            return print('Tree is empty')
        current_node = File_explorer._search_node(self.home_page,node_data)
        sibling_list = File_explorer._find_node_equal_level(current_node.get_right(), current_node, [])
        return sibling_list
    
    def find_ancestor(self, node_data):  # for step 1, d
        if self.home_page is None:
            return print('Tree is empty')
        current_node = File_explorer._search_node(self.home_page,node_data)
        ancestor_list = []
        while current_node.get_parent():
            current_node = File_explorer._find_parent(current_node)
            ancestor_list.append(current_node)
        return ancestor_list
        
    
        
if __name__ == 'main':
    # Example usage:
    tree = File_explorer()
    a = ['A',"B","C","D","E","F","G"]

    tree.insert(a[0])
    tree.insert(a[1], a[0])
    tree.insert(a[2], a[0])
    tree.insert(a[3], a[1])
    tree.insert(a[4], a[1])
    tree.insert(a[5], a[2])
    tree.insert(a[6], a[2])

    print('-----')
    tree.display_tree()
    print('-----')
    child = tree.find_child('B')
    print(child)
    print('-----')
    parent = tree.find_parent(child[0])
    print(parent)
    print('-----')
    tree.display_working_directory('B')