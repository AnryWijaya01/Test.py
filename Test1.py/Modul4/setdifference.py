# membuat A and B
A={1,2, 2, 4,5}
B={4, 5,6, 7, 8}

# Menggunakan operator - pada A
# Output: {1, 2, 3}
print(A - B)

# Output: {1, 2, 3}
A.difference(B)

# Menggunakan operator - pada B
# Output: {8, 6, 7}
print(B - A)

# Output: {8, 6, 7}
B.difference(A)
