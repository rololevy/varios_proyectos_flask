from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    def test_app_exists_web(self):
        self.assertIsNotNone(current_app)

    def test_app_in_testing(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_index_redirects(self):
        response = self.client.get(url_for("index"))
        self.assertRedirects(response, url_for("/show_information"))

    def test_show_information_get(self):
        response = self.client.get(url_for("show_information"))
        self.assertEqual(response.status_code, 200)

    def test_show_information_post(self):
        test_form_fake = {"username": "Rolo", "password": "12345***"}
        response = self.client.post(url_for("show_information"), data=test_form_fake)
        self.assertRedirects(response, url_for("/index"))
