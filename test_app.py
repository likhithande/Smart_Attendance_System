import unittest
from app import app 

class TestAttendanceSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        print("\n--- Starting Home Page Test ---")
        try:
            result = self.app.get('/')
            self.assertEqual(result.status_code, 200)
            print("SUCCESS: Home page loaded with Status Code 200.")
        except Exception as e:
            print(f"FAILED: Home page test failed with error: {e}")
            raise  # Re-raise the error so unittest knows it failed

    def test_invalid_page(self):
        print("\n--- Starting 404 Error Test ---")
        result = self.app.get('/this-page-does-not-exist')
        if result.status_code == 404:
            print("SUCCESS: Correctly returned 404 for missing page.")
        else:
            print(f"FAILED: Expected 404, but got {result.status_code}")
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    print("***************************************")
    print("  SMART ATTENDANCE SYSTEM TEST ")
    print("***************************************")
    unittest.main()