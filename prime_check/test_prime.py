import unittest
from prime_check import check_prime


class test_prime(unittest.TestCase) :
    def test_is_prime(self):
        self.assertTrue(check_prime(2))
        self.assertTrue(check_prime(3))
        self.assertFalse(check_prime(4))
        self.assertTrue(check_prime(5))
        self.assertFalse(check_prime(6))
        self.assertTrue(check_prime(7))
        self.assertFalse(check_prime(8))

if __name__ == '__main__':
    unittest.main()