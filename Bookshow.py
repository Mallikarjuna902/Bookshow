def print_layout(height, left, middle, right):
    print("\nInitial Theater Layout:\n")
    for _ in range(height):
        print('A' * left + '  ' + 'A' * middle + '  ' + 'A' * right)

def create_seats(height, total_cols):
    return [['A' for _ in range(total_cols)] for _ in range(height)]

def show_seats(seats, left, middle):
    print("\nCurrent Seat Status:")
    for row in seats:
        print(''.join(row[:left]) + '  ' + ''.join(row[left:left+middle]) + '  ' + ''.join(row[left+middle:]))

def book(seats, left, middle, right):
    while True:
        show_seats(seats, left, middle)
        try:
            row = int(input("Enter row number (starting from 0): "))
            col = int(input("Enter seat number (starting from 0): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if 0 <= row < len(seats) and 0 <= col < (left + middle + right):
            if seats[row][col] == 'A':
                seats[row][col] = 'B'
                print("Seat booked.")
            else:
                print("Seat already booked.")
        else:
            print("Invalid seat position.")

        # Ask for next step
        cont = input("Book another seat? (yes/no): ").strip().lower()
        if cont != 'yes':
            show_seats(seats, left, middle)
            print("Booking complete.")
            break

def run():
    print("🎭 Theater Seat Booking System 🎭\n")
    try:
        H = int(input("Enter number of rows: "))
        L = int(input("Enter number of seats in Left section: "))
        M = int(input("Enter number of seats in Middle section: "))
        R = int(input("Enter number of seats in Right section: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print_layout(H, L, M, R)
    total_cols = L + M + R
    seats = create_seats(H, total_cols)
    book(seats, L, M, R)

# Run the program
run()
