from textnode import TextNode
from textnode import TextType

def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")

    print(node)

if __name__ == "__main__":
    main()