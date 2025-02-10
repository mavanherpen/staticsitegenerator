from textnode import TextType
from textnode import TextNode

def main():

    node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(node)

main()