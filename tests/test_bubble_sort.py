import unittest

from src.bubble_sort import BubbleSorter


class TestBubbleSorter(unittest.TestCase):
    def setUp(self) -> None:
        self.sorter = BubbleSorter()

    def test_single_element(self) -> None:
        values = [5]
        expected = [5]

        result = self.sorter.sort(values)

        self.assertEqual(expected, result)
        self.assertIs(values, result)

    def test_already_sorted_pair(self) -> None:
        values = [1, 2]
        expected = [1, 2]

        result = self.sorter.sort(values)

        self.assertEqual(expected, result)

    def test_reversed_pair(self) -> None:
        values = [2, 1]
        expected = [1, 2]

        result = self.sorter.sort(values)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
