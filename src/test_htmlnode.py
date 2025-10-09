import unittest
from htmlnode import HTMLNode, LeafNode

prop1 = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
    })

expected1 = ' href="https://www.google.com" target="_blank"'

prop2 = HTMLNode(props={
        "href": "https://www.wikipedia.org",
        "target": "_self",
    })

expected2 = ' href="https://www.wikipedia.org" target="_self"'

prop3 = HTMLNode(props={
        "href": "https://www.github.com",
        "target": "_blank",
    })

expected3 = ' href="https://www.github.com" target="_blank"'


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test1 = prop1.props_to_html()
        test2 = prop2.props_to_html()
        test3 = prop3.props_to_html()
        self.assertEqual(test1, expected1)
        self.assertEqual(test2, expected2)
        self.assertEqual(test3, expected3)
        self.assertTrue(test1, test2,)
        self.assertIsNotNone(test1, test2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        
        node2 = LeafNode("b", None, props={
        "href": "https://www.github.com",
        "target": "_blank",
    })
        
        node3 = LeafNode(None, "hello world", {"href": "https://yourmom.com",
                                               "traget": "_blank",
        })

        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
        with self.assertRaises(ValueError):
            test = node2.to_html()
        
        self.assertEqual(node3.to_html(), "hello world")

        self.assertEqual(node4.to_html(), '<a href="https://www.google.com">Click me!</a>')