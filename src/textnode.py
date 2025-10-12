from enum import Enum, auto
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = auto() #"text"
    BOLD = auto() #"bold"
    ITALIC = auto() #"italic"
    CODE = auto() #"code"
    LINK = auto() #"link"
    IMAGE = auto() #"image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        try:
            text_type = TextType[text_type]
        except KeyError:
            raise ValueError("not a valid text type")
        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}. {self.text_type}, {self.url})"
    
#determines what type of node and tag to conver textnode to based on texttyp enum
def text_node_to_html_node(text_node):
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("not a valid TextNode type")