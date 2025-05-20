import unittest
from app import create_app

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_api_fires(self):
        res = self.app.get("/api/fires")
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
