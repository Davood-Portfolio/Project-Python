class Analytics:
    def __init__(self, data):
        self.data = data

    def total(self, column_index):
        """Sum of values in a column."""
        return sum(row[column_index] for row in self.data)

    def average(self, column_index):
        """Average of values in a column."""
        if not self.data:
            return 0
        return self.total(column_index) / len(self.data)

    def max_value(self, column_index):
        """Maximum value in a column."""
        return max(row[column_index] for row in self.data)

    def min_value(self, column_index):
        """Minimum value in a column."""
        return min(row[column_index] for row in self.data)

    def count(self):
        """Total number of rows."""
        return len(self.data)
