
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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        #value error if tag is none
        if not self.tag or self.tag == "":
            raise ValueError("tag cannot == None")
        
        #vvalue error if nildren is none
        if self.children is None or self.children == "":
            raise ValueError("Must have children")
        
        #check self.children is iterable
        try:
            it = iter(self.children)
        except TypeError:
            raise TypeError("children must be iterable")
        
        #Retrun string representing the html tag of nod and children needs to be recursive method.
        if not self.children:
            return f"<{self.tag}></{self.tag}>"
        
        child_html = []

        for child in self.children:
            if isinstance(child, HTMLNode):
                child_html.append(child.to_html()) #Recursive call
            else:
                child_html.append(str(child))

        return f"<{self.tag}>{''.join(child_html)}</{self.tag}>"
    
    
