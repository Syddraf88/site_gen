import unittest
from htmlnode import HTMLNode

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
        self.assertIsNotNone(test1, test2,)

    