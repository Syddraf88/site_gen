from textnode import TextNode
from htmlnode import HTMLNode

def main():
    textnode = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    htmlnode = HTMLNode(value="this is a value", children="it's a boy!",)
    print(htmlnode)

if __name__ == "__main__":
    main()