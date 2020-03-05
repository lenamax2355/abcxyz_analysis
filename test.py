import unittest

from abcxyz_analysis import abc_analysis as abc
from abcxyz_analysis import xyz_analysis as xyz


class TestCase(unittest.TestCase):
    

    def test_abc_calculate_shares(self):
        result = abc.calculate_shares([50, 30, 20], 100)
        self.assertEqual(result, [50, 30, 20])


    def test_abc_calculate_accumulated_shares(self):
        result = abc.calculate_accumulated_shares([50, 30, 20])
        self.assertEqual(result, [50, 80, 100])


    def test_abc_assign_to_groups(self):
        result = abc.assign_to_groups([50, 80, 100])
        self.assertEqual(result, ['A', 'B', 'C'])


    def test_xyz_calculate_coefficients_of_variation(self):
        result = xyz.calculate_coefficients_of_variation([
            [1, 1, 1, 1, 1],
            [120.48, 100.14, 139.14, 117.55, 99.69, 114.25, 107.34, 123.71],
            [100, 1]])
        self.assertEqual(result, [0.0, 10.662847785949282, 98.01980198019803])


    def test_xyz_assign_to_groups(self):
        result = xyz.assign_to_groups([0.0, 10.662847785949282, 98.01980198019803])
        self.assertEqual(result, ['X', 'Y', 'Z'])


if __name__ == '__main__':
    unittest.main()