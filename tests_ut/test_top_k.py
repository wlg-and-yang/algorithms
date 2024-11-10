import unittest
from algorithms.arrays import top_k

class TestTopK(unittest.TestCase):

    def test_top_k_with_positive_numbers(self):
        self.assertEqual(top_k([1, 2, 3, 2, 3, 4, 4, 4], 2), [4, 4])

    def test_top_k_with_negative_numbers(self):
        self.assertEqual(top_k([-1, -2, -3, -2, -3, -4, -4, -4], 2), [-1, -2])

    def test_top_k_with_single_element(self):
        self.assertEqual(top_k([1], 1), [1])

    def test_top_k_with_empty_list(self):
        self.assertEqual(top_k([], 1), -1)

    def test_top_k_with_k_greater_than_unique_elements(self):
        self.assertEqual(top_k([1, 2, 3], 5), -1)

    def test_top_k_with_k_zero(self):
        self.assertEqual(top_k([1, 2, 3], 0), [])

    def test_top_k_with_all_elements_same(self):
        self.assertEqual(top_k([1, 1, 1, 1], 2), [1, 1])

    # def test_top_k_with_k_negative(self):
    #     with self.assertRaises(ValueError):
    #         top_k([1, 2, 3], -1)

if __name__ == '__main__':
    unittest.main()
