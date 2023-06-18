import unittest

from main import y


class Tests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(y(3), 1.824236970483513)
        self.assertEqual(y(0), 1.0)
        self.assertEqual(y(1), 2.682941969615793)
        self.assertEqual(y(-1), 2.449489742783178)

    def test_args(self):
        self.assertEqual(y(), 'Отсутствуют введённые данные')
        self.assertEqual(y(1, 2, 'Test', 4), 2.682941969615793)
        self.assertEqual(y('Test'), 'Введённые данные не являются числом')


if __name__ == '__main__':
    unittest.main()
