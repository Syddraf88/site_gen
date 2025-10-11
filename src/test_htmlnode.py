import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    #tests for children and grandchildren
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    #tests for missing mandatory values and error cases
    def test_missing_tag_raises(self):
        node = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertIn("tag cannot == None", str(cm.exception))

    def test_missing_children_raises(self):
        node = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertIn("Must have children", str(cm.exception))

    #def test_invalid_tag_values(self):
    #    for bad_tag in ("", "  ", 0, False):
    #        with self.subTest(bad_tag=bad_tag):
    #            node = ParentNode(tag=bad_tag, children=[])
    #            with self.assertRaises(ValueError):
    #                node.to_html()

    def test_children_not_iterable_typerror(self):
        node = ParentNode(tag="div", children=123) #not iterable
        with self.assertRaises(TypeError):
            node.to_html()

    #Base and simple cases
    def test_empty_children_renders_empty_tag(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_single_text_child(self):
        node = ParentNode("p", ["hi"])
        self.assertEqual(node.to_html(), "<p>hi</p>")
    
    def test_falsy_text_children(self):
        cases = [(0, "0"), (False, "False"), ("", "")]
        for val, expected in cases:
            with self.subTest(val=val):
                node = ParentNode("span", [val])
                self.assertEqual(node.to_html(), f"<span>{expected}</span>")
    
    #mixed and nexted cases
    def test_mixed_children_order_preserved(self):
        node = ParentNode("p", ["Hello ", ParentNode("em", ["world"]), "!"])
        self.assertEqual(node.to_html(), f"<p>Hello <em>world</em>!</p>")

    def test_deep_nesting(self):
        depth = 100
        leaf = ParentNode("b", ["x"])
        node = leaf
        for _ in range(depth):
            node = ParentNode("div", [node])

        html = node.to_html()
        self.assertEqual(html.count("<div>"), depth)
        self.assertTrue(html.endswith("</div>" * depth))
        self.assertIn("<b>x</b>", html)

    def test_duplicate_child_refrence_renders_twice(self):
        child = ParentNode("li", ["A"])
        ul = ParentNode("ul", [child, child])
        self.assertEqual(ul.to_html(), "<ul><li>A</li><li>A</li></ul>")

    #No Mutations
    def test_to_html_does_not_mutate_children(self):
        children = [ParentNode("i", ["one"]), " two "]
        node = ParentNode("span", list(children)) #shallow copy
        _ = node.to_html()
        self.assertIsInstance(node.children[0], ParentNode)
        self.assertEqual(node.children[1], " two ")

    #Cycles should generatre recursion error

    def test_cycle_raises_recursion_error(self):
        parent = ParentNode("div", [])
        child = ParentNode("div", [parent])
        parent.children.append(child)
        with self.assertRaises(RecursionError):
            parent.to_html()
    

if __name__ == "__main__":
    unittest.main(verbosity=2)