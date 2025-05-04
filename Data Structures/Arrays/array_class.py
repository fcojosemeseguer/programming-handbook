class Array:
    def __init__(self, max_size):
        """Initialize an empty array with a maximum size."""
        self.max_size = max_size
        self.n = 0  # Current size
        self.arr = [0] * max_size

    def insert_beg(self, item):
        """Insert an item at the beginning of the array."""
        if self.n >= self.max_size:
            print("Overflow")
            return

        for i in range(self.n, 0, -1):  # Shift elements right
            self.arr[i] = self.arr[i - 1]

        self.arr[0] = item
        self.n += 1

    def insert_after(self, val, item):
        """Insert an item after a given value."""
        if self.n >= self.max_size:
            print("Overflow")
            return

        if val not in self.arr[: self.n]:  # Ensure value exists in valid portion
            print("Value not found")
            return

        i = self.n - 1
        while self.arr[i] != val:
            i -= 1

        for j in range(self.n, i + 1, -1):  # Shift elements right
            self.arr[j] = self.arr[j - 1]

        self.arr[i + 1] = item
        self.n += 1

    def insert_end(self, item):
        """Insert an item at the end of the array."""
        if self.n >= self.max_size:
            print("Overflow")
            return

        self.arr[self.n] = item
        self.n += 1

    def del_beg(self):
        """Delete the first element."""
        if self.n == 0:
            print("Underflow")
            return

        for i in range(1, self.n):
            self.arr[i - 1] = self.arr[i]

        self.n -= 1

    def del_after(self, val):
        """Delete the element after a given value."""
        if val not in self.arr[: self.n]:
            print("Value not found")
            return

        i = self.n - 1
        while self.arr[i] != val:
            i -= 1

        if i + 1 >= self.n:
            print("No element after given value")
            return

        for j in range(i + 1, self.n - 1):  # Shift elements left
            self.arr[j] = self.arr[j + 1]

        self.n -= 1

    def del_end(self):
        """Delete the last element."""
        if self.n == 0:
            print("Underflow")
            return

        self.n -= 1

    def display(self):
        """Display the array up to its valid elements."""
        print("Array:", self.arr[: self.n])


if __name__ == "__main__":
    array = Array(10)
    array.insert_end(5)
    array.insert_end(10)
    array.insert_beg(3)
    array.insert_after(5, 7)
    array.display()

    array.del_beg()
    array.display()

    array.del_end()
    array.display()
