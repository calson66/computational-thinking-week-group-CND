def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution_station_4(input_value: int) -> bool:
    # Determine if the input is a prime number
    return is_prime(input_value)


