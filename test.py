import unittest
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "CLAVE SEGURA"


class TestFlask(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.items = [
            "ITEM 1",
            "ITEM 2",
            "ITEM 3",
            "ITEM 4",
        ]

    def test_index_route(self):
        response = self.app.get("/index")
        self.assertEqual(response.status_code, 302)
        self.assertIn(b"Found", response.data)
        self.assertIn(b"Location: /show_information_address", response.data)
        session_value = session.get("user_ip_information")
        self.assertIsNotNone(session_value)

    def test_show_information_address_route(self):
        response = self.app.get("/show_information_address")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"IP Information", response.data)
        self.assertIn(b"User IP:", response.data)
        session_value = session.get("user_ip_information")
        self.assertIsNotNone(session_value)
        user_ip = response.data.decode("utf-8").strip()
        self.assertEqual(user_ip, session_value)
        items_html = response.data.decode("utf-8").strip()
        for item in self.items:
            self.assertIn(item.encode("utf-8"), items_html)


if __name__ == "__main__":
    unittest.main()
