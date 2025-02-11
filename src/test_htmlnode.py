import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
#    def test_to_html_props(self):
#        node = HTMLNode(
#            "p",
#            "This is a test!",
#            None,
#            {"target": "_blank", "href": "https://localhost:8888"},
#        )
#        self.assertEqual(
#            node.props_to_html(),
#            ' target="_blank" href="https://localhost:8888"',
#        )
    
    def test_values(self):
        node = HTMLNode(
            "a",
            "Testing, please wait",
        )
        self.assertEqual(
            node.tag,
            "a",
        )
        self.assertEqual(
            node.value,
            "Testing, please wait",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "Yes, yes, still testing!",
            None,
            {"target": "testing"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Yes, yes, still testing!, children: None, {'target': 'testing'})",
        )

if __name__ == "__main__":
    unittest.main()