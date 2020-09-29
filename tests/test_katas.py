import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEquals(katas.add(10, 5), 15)
        self.assertEquals(katas.add(-2, 1), -1)
        self.assertEquals(katas.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEquals(katas.multiply(2, 5), 10)
        self.assertEquals(katas.multiply(5, -4), -20)
        self.assertEquals(katas.multiply(10, 15), 150)

    def test_power(self):
        self.assertEquals(katas.power(2, 3), 8)
        self.assertEquals(katas.power(-10, 2), 100)
        self.assertEquals(katas.power(-6, 2), 36)
        with self.assertRaises(ValueError):
            katas.power(6, -2)
            katas.power(3, 2.5)
            katas.power(6, -3.7)
            katas.power(-5, -4.5)

    def test_factorial(self):
        self.assertEquals(katas.factorial(5), 120)
        self.assertEquals(katas.factorial(3), 6)
        self.assertEquals(katas.factorial(12), 479001600)
        self.assertEquals(katas.factorial(2), 2)
        self.assertEquals(katas.factorial(4), 24)
        self.assertEquals(katas.factorial(6), 720)
        self.assertEquals(katas.factorial(7), 5040)
        self.assertEquals(katas.factorial(8), 40320)
        self.assertEquals(katas.factorial(9), 362880)
        self.assertEquals(katas.factorial(10), 3628800)
        self.assertEquals(katas.factorial(11), 39916800)
        self.assertEquals(katas.factorial(13), 6227020800)
        with self.assertRaises(ValueError):
            katas.factorial(-6)
            katas.factorial(-3)
            katas.factorial(-12)
            katas.factorial(-7)

    def test_fibonacci(self):
        self.assertEquals(katas.fibonacci(4), 3)
        self.assertEquals(katas.fibonacci(9), 34)
        self.assertEquals(katas.fibonacci(2), 1)
        self.assertEquals(katas.fibonacci(3), 2)
        self.assertEquals(katas.fibonacci(5), 5)
        self.assertEquals(katas.fibonacci(6), 8)
        self.assertEquals(katas.fibonacci(7), 13)
        self.assertEquals(katas.fibonacci(8), 21)
        self.assertEquals(katas.fibonacci(10), 55)
        self.assertEquals(katas.fibonacci(11), 89)
        self.assertEquals(katas.fibonacci(12), 144)
        self.assertEquals(katas.fibonacci(13), 233)
        self.assertEquals(katas.fibonacci(14), 377)
        self.assertEquals(katas.fibonacci(15), 610)
        self.assertEquals(katas.fibonacci(16), 987)
        self.assertEquals(katas.fibonacci(17), 1597)
        self.assertEquals(katas.fibonacci(18), 2584)
        self.assertEquals(katas.fibonacci(19), 4181)
        self.assertEquals(katas.fibonacci(20), 6765)
        self.assertEquals(katas.fibonacci(21), 10946)
        self.assertEquals(katas.fibonacci(22), 17711)
        self.assertEquals(katas.fibonacci(23), 28657)
        self.assertEquals(katas.fibonacci(24), 46368)
        self.assertEquals(katas.fibonacci(25), 75025)
        self.assertEquals(katas.fibonacci(26), 121393)
        self.assertEquals(katas.fibonacci(27), 196418)
        with self.assertRaises(ValueError):
            katas.fibonacci(-9)
            katas.fibonacci(-50)
            katas.fibonacci(-19)
            katas.fibonacci(-3)
            katas.fibonacci(-6)


if __name__ == '__main__':
    unittest.main()
