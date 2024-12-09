def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = power(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = power(base, (exponent - 1) // 2)
        return base * half_power * half_power


a = power(2, 10)
print(a)
