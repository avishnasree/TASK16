#CHECK THE GIVEN NUMBER IS PRIME OR NOT.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = 17
result = is_prime(number)
print("is Prime:", result)
