from textnode import TextType
from textnode import TextNode

def main():

    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()