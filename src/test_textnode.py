import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "BOLD")
        node2 = TextNode("This is a text node", "BOLD")
        node3 = TextNode("this is some anchor text", "LINK", "https://mylink.dev")
        self.assertEqual(node, node2)
        self.assertIsNotNone(node3.url)

    def test_text(self):
        node = TextNode("This is a text node", "TEXT")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_coercion(self):
        node = TextNode("this is a text node", "BOLD")
        self.assertIsInstance(node.text_type, TextType)
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_textnode_rejection(self):
        with self.assertRaisesRegex(ValueError, r"^not a valid text type$"):
            node = TextNode("This wants to be a text node", "BULLET")

    def test_link(self):
        node = TextNode("Boot.dev", "LINK", "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        node = TextNode("Logo", "IMAGE", "https://img.logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://img.logo.png", "alt": "Logo"})

    def test_bold(self):
        node = TextNode("bold text", "BOLD")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")
        self.assertIsNone(html_node.props)

    def test_italic(self):
        node = TextNode("slanted text", "ITALIC")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "slanted text")
        self.assertIsNone(html_node.props)

    def test_code(self):
        node = TextNode("def boot.dev(self):", "CODE")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "def boot.dev(self):")
        self.assertIsNone(html_node.props)
