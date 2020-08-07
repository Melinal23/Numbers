
def isHappy(n):
    seen = set()
    seen.add(n)

    while (1):
        if n == 1:
            return True

        total = 0
        # get the digits in the int
        while (n > 0):
            digit = n % 10
            total += digit ** 2
            n //= 10

        n = total

        if n in seen:
            return False

        seen.add(n)

print(isHappy(7))







