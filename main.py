# Array satu dimensi

# Array satu dimensi (daftar angka)
numbers = [1, 2, 3, 4, 5]

# Mengakses elemen dalam array satu dimensi menggunakan indeks
print(numbers[0])  # Output: 1
print(numbers[3])  # Output: 4

# Mengubah nilai elemen dalam array satu dimensi
numbers[1] = 10
print(numbers)  # Output: [1, 10, 3, 4, 5]

# Menambahkan elemen baru ke dalam array satu dimensi
numbers.append(6)
print(numbers)  # Output: [1, 10, 3, 4, 5, 6]

# Menghitung panjang (jumlah elemen) dalam array satu dimensi
length = len(numbers)
print("Panjang array:", length)  # Output: Panjang array: 6

# Array dua dimensi

# Array dua dimensi (matriks angka)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mengakses elemen dalam array dua dimensi menggunakan indeks baris dan kolom
print(matrix[0][0])  # Output: 1
print(matrix[1][2])  # Output: 6

# Mengubah nilai elemen dalam array dua dimensi
matrix[1][1] = 55
print(matrix)  # Output: [[1, 2, 3], [4, 55, 6], [7, 8, 9]]

# Menghitung jumlah baris dan kolom dalam array dua dimensi
num_rows = len(matrix)
num_cols = len(matrix[0])
print("Jumlah baris:", num_rows)  # Output: Jumlah baris: 3
print("Jumlah kolom:", num_cols)  # Output: Jumlah kolom: 3
