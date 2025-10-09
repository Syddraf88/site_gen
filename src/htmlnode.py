from textnode import TextType, TextNode
import html

class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        
        prop = ' '.join(f'{k}="{html.escape(str(v), quote=True)}"' for k, v in self.props.items())
        
        return f' {prop}'
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (self.tag == other.tag,
                self.value == other.tag,
                self.children == other.children,
                self.props == other.props)
    
class LeafNode(HTMLNode):
        def __init__(self, tag, value, props=None):
            super().__init__(tag=tag, value=value, props=props)

    
        def to_html(self):
            if self.value is None:
                raise ValueError("All leaf nodes must have a value")
            
            if self.tag is None:
                return f"{self.value}"

            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

