import unittest
from flask import current_app
from app import db, User, Task
from app import create_app
from config import config


class DemoTestCase(unittest.TestCase):
    def setUp(self) -> None:
        config_class = config['test']
        self.app = create_app(config_class)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.id = 1

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_demo(self):
        self.assertTrue(1 == 1)

    def test_user_exist(self):
        user = User.get_by_id(self.id)
        self.assertTrue(user is None)

    def test_create_user(self):
        user = User.create_element('username', 'password', 'email@gmail.com')
        self.assertTrue(user.id == self.id)
