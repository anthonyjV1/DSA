import unittest

from problems.arrays.two_sum import Solution


class TwoSumTests(unittest.TestCase):
    def check_pair(self, nums, target):
        result = Solution().twoSum(nums.copy(), target)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        i, j = result
        self.assertIsInstance(i, int)
        self.assertIsInstance(j, int)
        self.assertNotEqual(i, j, "Use two different indices")
        self.assertTrue(0 <= i < len(nums))
        self.assertTrue(0 <= j < len(nums))
        self.assertEqual(nums[i] + nums[j], target)

    def test_regular_pair(self):
        self.check_pair([4, 8, 1, 6], 10)

    def test_duplicate_values(self):
        self.check_pair([5, 5], 10)

    def test_negative_values(self):
        self.check_pair([-8, -3, -6, -2], -10)

    def test_zero(self):
        self.check_pair([0, 7, 2], 7)

    def test_cannot_reuse_an_index(self):
        self.check_pair([3, 2, 4], 6)


if __name__ == "__main__":
    unittest.main()
