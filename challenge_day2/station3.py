# Checks if sample input is divisible by 3. 
def check_divisibility_by_3(sample_input):

    digit_sum = sum(int(digit) for digit in str(abs(sample_input)))

    return digit_sum % 3 == 0