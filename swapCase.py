def swap_case(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

print(swap_case('HakceRWSasWa'))