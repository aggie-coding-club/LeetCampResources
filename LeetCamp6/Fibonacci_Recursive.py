class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]


if __name__ == "__main__":
    # Input n
    n = 6

    # Initialize Solution object
    s = Solution()
    # Call fib method and print the output
    print(s.fib(n))
