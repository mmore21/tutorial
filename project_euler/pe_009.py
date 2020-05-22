"""
Project Euler #9 - Special Pythagorean Triplet
Methodology: Brute force possible triplet combinations.
"""
def find_pythagorean_triple():
    for a in range(1, 500):
        for b in range(1, 1000):
            c = 1000 - a - b
            if (a**2 + b**2) == c**2:
                return a * b * c

print(find_pythagorean_triple())