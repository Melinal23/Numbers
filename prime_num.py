'''Given a prime number, return the next smallest prime number

Examples:
Input: 3
Output: 5

#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
#  113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
'''

def is_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False

        return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False

# print(is_prime(6))


def next_smallest_prime(num):

    next_prime = (num + 1)

    while(is_prime(next_prime) is False):
        next_prime += 1

    return next_prime

print(next_smallest_prime(157))