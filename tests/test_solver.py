import subprocess
import sys
import unittest


class SolverTests(unittest.TestCase):
    def test_accepts_and_prints_coefficients(self) -> None:
        self.assert_solver_output(
            "2\n-3\n1\n",
            0,
            "Enter a: Enter b: Enter c: Coefficients accepted: a = 2.0, b = -3.0, c = 1.0\n",
        )

    def test_rejects_zero_leading_coefficient(self) -> None:
        self.assert_solver_output(
            "0\n3\n4\n", 1, "Enter a: Enter b: Enter c: Not a quadratic equation: a = 0.\n"
        )

    def test_rejects_invalid_input_without_a_traceback(self) -> None:
        for data in ("x\n-3\n1\n", "nan\n-3\n1\n", ""):
            with self.subTest(data=data):
                self.assert_solver_output(data, 1, "Enter a: Error: enter a finite numeric value.\n")

    def assert_solver_output(self, data: str, status: int, output: str) -> None:
        result = subprocess.run(
            [sys.executable, "solver.py"], input=data, capture_output=True, text=True, timeout=5
        )
        self.assertEqual(result.returncode, status)
        self.assertEqual(result.stdout, output)
        self.assertEqual(result.stderr, "")
