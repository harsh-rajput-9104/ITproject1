class TicketSystem:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = [["Available" for _ in range(cols)] for _ in range(rows)]

    def display_seats(self):
        print("\nSeating Arrangement:")
        for row in range(self.rows):
            for col in range(self.cols):
                seat = f"R{row+1}C{col+1}"
                status = "✓" if self.seats[row][col] != "Available" else "✗"
                print(f"{seat}({status})", end="  ")
            print()

    def book_ticket(self, row, col, name):
        if self.is_valid_seat(row, col):
            if self.seats[row][col] == "Available":
                self.seats[row][col] = name
                print(f"Seat R{row+1}C{col+1} has been booked successfully for {name}!")
            else:
                print(f"Seat R{row+1}C{col+1} is already booked.")
        else:
            print("Invalid seat number. Please try again.")

    def cancel_ticket(self, row, col):
        if self.is_valid_seat(row, col):
            if self.seats[row][col] != "Available":
                print(f"Booking for seat R{row+1}C{col+1} has been canceled.")
                self.seats[row][col] = "Available"
            else:
                print(f"Seat R{row+1}C{col+1} is not booked yet.")
        else:
            print("Invalid seat number. Please try again.")

    def show_summary(self):
        print("\nBooking Summary:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[row][col] != "Available":
                    print(f"Seat R{row+1}C{col+1}: Booked by {self.seats[row][col]}")
        print("End of Summary.\n")

    def is_valid_seat(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

# Main functionality
if __name__ == "__main__":
    rows, cols = 5, 5  # Customize seating layout
    system = TicketSystem(rows, cols)

    while True:
        print("\nMenu:")
        print("1. View Seats")
        print("2. Book a Ticket")
        print("3. Cancel a Ticket")
        print("4. Show Booking Summary")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.display_seats()
        elif choice == 2:
            name = input("Enter your name: ")
            seat = input("Enter seat number (e.g., R1C1): ")
            try:
                row, col = map(int, seat[1:].split("C"))
                system.book_ticket(row - 1, col - 1, name)
            except (ValueError, IndexError):
                print("Invalid input format. Please use the format R1C1.")
        elif choice == 3:
            seat = input("Enter seat number to cancel (e.g., R1C1): ")
            try:
                row, col = map(int, seat[1:].split("C"))
                system.cancel_ticket(row - 1, col - 1)
            except (ValueError, IndexError):
                print("Invalid input format. Please use the format R1C1.")
        elif choice == 4:
            system.show_summary()
        elif choice == 5:
            print("Thank you for using the Online Ticket System!")
            break
        else:
            print("Invalid choice. Please try again.")
