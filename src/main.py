from textnode import TextType
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():

    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()