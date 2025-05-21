print("Theater Seats")
H = int(input("Enter number of rows: "))
L, M, R = 6, 10, 6
T = L + M + R
seats = [['🟢'] * T for _ in range(H)]
def show_seats():
    print("\nAvailable = 🟢 | Booked = 🔴")
    print("        L" + "   " * (L-1) + "M" + "  " * (M-1) + "R")
    for i, row in enumerate(seats):
        left = ''.join(row[:L])
        mid = ''.join(row[L:L+M])
        right = ''.join(row[L+M:])
        print(f"{i:2d} {left}  {mid}  {right}")
def get_index(section, num):\

    dfckjdshfcidsa
    adsclads[pfckadsofj
odfjdaspokadsofk
    if section == 'L' and 1 <= num <= L: return num - 1
    if section == 'M' and 1 <= num <= M: return L + num - 1
    if section == 'R' and 1 <= num <= R: return L + M + num - 1
    return -1
def book():
    r = int(input(f"Enter row (0–{H-1}): "))
    s = input("Section (L/M/R): ").upper()
    n = int(input("Seat number in section: "))
    c = get_index(s, n)
    if 0 <= r < H and c != -1:
        if seats[r][c] == '🟢':
            seats[r][c] = '🔴'
            print("Seat booked.")
        else:
            print("Seat already booked.")
    else:
        print("Invalid input.")
show_seats()
book()
show_seats()
if input("Book another? (yes/no): ").lower() == 'yes':
    book(); show_seats()
print("\nFinal Layout:")
show_seats()
