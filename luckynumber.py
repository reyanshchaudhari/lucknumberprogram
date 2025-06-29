chaldean_map = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
    'B': 2, 'K': 2, 'R': 2,
    'C': 3, 'G': 3, 'L': 3, 'S': 3,
    'D': 4, 'M': 4, 'T': 4,
    'E': 5, 'H': 5, 'N': 5, 'X': 5,
    'U': 6, 'V': 6, 'W': 6,
    'O': 7, 'Z': 7,
    'F': 8, 'P': 8
}

def reduce_number(n):
    """Reduce to a single digit unless it's 11 or 22 (master numbers)"""
    while n > 9 and n not in [11, 22]:
        n = sum(int(digit) for digit in str(n))
    return n

def chaldean_lucky_number(name):
    name = name.upper()
    total = 0
    print(f"\nCalculating lucky number for: {name}\n")
    for char in name:
        if char in chaldean_map:
            value = chaldean_map[char]
            total += value
            print(f"{char} = {value}")
        else:
            print(f"{char} is ignored.")










    print(f"\nTotal value = {total}")
    lucky_number = reduce_number(total)
    print(f"Lucky Number = {lucky_number}\n")
    return lucky_number

# Example usage
user_name = input("Enter your name: ")
chaldean_lucky_number(user_name)