class FizzBuzz:
    def game(self, n):
        if isinstance(n, int):
            if n % 15 == 0:
                return "FizzBuzz"
            elif n % 5 == 0:
                return "Buzz"
            elif n % 3 == 0:
                return "Fizz"
            else:
                return n
        else:
            return "err"
