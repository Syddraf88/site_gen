from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode



def main():
    textnode = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    #htmlnode = HTMLNode(value="this is a value", children="it's a boy!",)
    print(textnode)

    parent_test = ParentNode("p", [LeafNode("b", "Bold text"),
                                   LeafNode(None, "Normal text"),
                                   LeafNode("i", "italic text"),
                                   LeafNode(None, "Normal text"),
                                   ])
    
    print(parent_test.to_html())

if __name__ == "__main__":
    main()