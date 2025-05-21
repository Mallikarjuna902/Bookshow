print("Theater Seats")
H = int(input("Enter number of rows: "))
L, M, R = 6, 10, 6
T = L + M + R
seats = [['A'] * T for _ in range(H)]
for _ in range(H):
    print('A' * L + '  ' + 'A' * M + '  ' + 'A' * R)
for row in seats:
    print(''.join(row[:L]) + '  ' + ''.join(row[L:L+M]) + '  ' + ''.join(row[L+M:]))
row = int(input("Enter row number: "))
col = int(input("Enter seat number: "))
if 0 <= row < H and 0 <= col < T:
    if seats[row][col] == 'A':
        seats[row][col] = 'B'
        print("Seat booked.")
    else:
        print("Seat already booked.")
else:
    print("Invalid seat.")
for row in seats:
    print(''.join(row[:L]) + '  ' + ''.join(row[L:L+M]) + '  ' + ''.join(row[L+M:]))
if input("Book another? (yes/no): ").lower() == 'yes':
    row = int(input("Enter row number: "))
    col = int(input("Enter seat number: "))
    if 0 <= row < H and 0 <= col < T:
        if seats[row][col] == 'A':
            seats[row][col] = 'B'
            print("Seat booked.")
        else:
            print("Seat already booked.")
    else:
        print("Invalid seat.")
print("Final Seat Layout:")
for row in seats:
    print(''.join(row[:L]) + '  ' + ''.join(row[L:L+M]) + '  ' + ''.join(row[L+M:]))
