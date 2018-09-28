# Object-oriented programming:  Java, C++, C#, Python,
#PHP, JavaScript, Ruby, Perl, Object Pascal, Objective-C,
#Dart, Swift, Scala, Common Lisp, and Smalltalk.
# f(),x: f() is method, x is object (property) -- encapsulation
# -- abstraction (hide detail of complexity)
# -- inheritance
# -- polymorphism (many forms)


######### BST ################
# a node consists of key, value, left (smaller) and right (larger) subtree
# search, insert, get

# create a bianary tree
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
 
root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"
 
root.left.left = Tree()
root.left.left.data = "left 2"
root.left.right = Tree()
root.left.right.data = "left-right"

# create root
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)

root = Node(10)
root.PrintTree()

# compare the new value with the parent node
