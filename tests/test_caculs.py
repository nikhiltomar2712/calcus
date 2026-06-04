import unittest
from src.caculs import safe_eval_expr

class TestCaculs(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(safe_eval_expr("1 + 1"), 2)
        self.assertEqual(safe_eval_expr("2 + 3"), 5)

    def test_subtraction(self):
        self.assertEqual(safe_eval_expr("5 - 3"), 2)
        self.assertEqual(safe_eval_expr("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(safe_eval_expr("3 * 7"), 21)
        self.assertEqual(safe_eval_expr("2 * 5"), 10)

    def test_division(self):
        self.assertEqual(safe_eval_expr("10 / 2"), 5.0)
        self.assertEqual(safe_eval_expr("9 / 3"), 3.0)

    def test_floor_division(self):
        self.assertEqual(safe_eval_expr("10 // 3"), 3)
        self.assertEqual(safe_eval_expr("7 // 2"), 3)

    def test_modulus(self):
        self.assertEqual(safe_eval_expr("10 % 3"), 1)
        self.assertEqual(safe_eval_expr("7 % 2"), 1)

    def test_power(self):
        self.assertEqual(safe_eval_expr("2 ** 3"), 8)
        self.assertEqual(safe_eval_expr("3 ** 2"), 9)

    def test_unary_operations(self):
        self.assertEqual(safe_eval_expr("-5"), -5)
        self.assertEqual(safe_eval_expr("+3"), 3)

    def test_math_functions(self):
        self.assertAlmostEqual(safe_eval_expr("sqrt(16)"), 4)
        self.assertAlmostEqual(safe_eval_expr("sin(pi / 2)"), 1)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            safe_eval_expr("1 / 0")
        with self.assertRaises(ValueError):
            safe_eval_expr("unknown_function(1)")

if __name__ == "__main__":
    unittest.main()
