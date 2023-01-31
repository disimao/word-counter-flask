from app import app as word_counter

import unittest


class TestView(unittest.TestCase):
    def setUp(self):
        self.app = word_counter.test_client()

    def test_get(self):
        self.response = self.app.get("/")
        self.assertEqual(200, self.response.status_code)

    def test_html_form_exists(self):
        self.response = self.app.get("/?textbody=")
        self.assertIn(b'<form method="get"', self.response.data)

    def test_html_string_response_with_empty_input(self):
        self.response = self.app.get("/?textbody=")
        self.assertIn(b"some text input is required", self.response.data)

    def test_response_has_number_of_words(self):
        self.response = self.app.get(
            "/?textbody=Text input, test data with 6 words"
        )
        self.assertIn(b"Total of 6 words", self.response.data)

    def test_response_has_number_of_words(self):
        self.response = self.app.get(
            "/?textbody=Text input, test data with 6 words words"
        )
        self.assertIn(b"Total of 6 words", self.response.data)