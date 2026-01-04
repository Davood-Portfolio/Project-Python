class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter(self, condition_fn):
        """Return rows that match a condition function."""
        return [row for row in self.data if condition_fn(row)]

    def sort(self, key_index=0, reverse=False):
        """Sort rows by a specific column index."""
        return sorted(self.data, key=lambda row: row[key_index], reverse=reverse)

    def search(self, key_index, value):
        """Search rows where a column matches a value."""
        return [row for row in self.data if row[key_index] == value]

    def group_by(self, key_index):
        """Group rows by a specific column index."""
        groups = {}
        for row in self.data:
            key = row[key_index]
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
        return groups
