class BubbleSorter:
    def sort(self, values: list[int]) -> list[int]:
        size = len(values)

        for i in range(size, 1, -1):
            for j in range(i - 1):
                if values[j] > values[j + 1]:
                    auxiliary = values[j]
                    values[j] = values[j + 1]
                    values[j + 1] = auxiliary

        return values
