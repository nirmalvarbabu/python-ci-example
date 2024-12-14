# test_app.py
import unittest
from app import hello_world

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")
def test_say_hello():
    assert say_hello() == "Hello, CI World!"


if __name__ == "__main__":
    unittest.main()
