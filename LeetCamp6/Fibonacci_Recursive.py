class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.fib(n - 1)


if __name__ == "__main__":
    # Input n
    n = 5

    # Initialize Solution object
    s = Solution()
    # Call fib method and print the output
    print(s.fib(n))
