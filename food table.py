import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# In-memory bookings
bookings = []

# Function to book a table
def book_table():
    name = name_var.get()
    contact = contact_var.get()
    date = date_var.get()
    time = time_var.get()
    guests = guests_var.get()

    if not name or not contact or not date or not time or not guests:
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        # Validate date & time
        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(time, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid date or time format")
        return

    booking = {
        "name": name,
        "contact": contact,
        "date": date,
        "time": time,
        "guests": guests
    }
    bookings.append(booking)
    messagebox.showinfo("Success", "Table booked successfully")
    clear_fields()

# Clear input fields
def clear_fields():
    name_var.set("")
    contact_var.set("")
    date_var.set("")
    time_var.set("")
    guests_var.set("")

# Show all bookings in a new window
def show_bookings():
    booking_window = tk.Toplevel(root)
    booking_window.title("All Bookings")
    booking_window.geometry("500x300")

    tree = ttk.Treeview(booking_window, columns=("Name", "Contact", "Date", "Time", "Guests"), show='headings')
    tree.heading("Name", text="Name")
    tree.heading("Contact", text="Contact")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")
    tree.heading("Guests", text="Guests")

    for booking in bookings:
        tree.insert("", tk.END, values=(booking["name"], booking["contact"], booking["date"], booking["time"], booking["guests"]))

    tree.pack(expand=True, fill="both", padx=10, pady=10)

# GUI Setup
root = tk.Tk()
root.title("Restaurant Table Booking")
root.geometry("400x400")

tk.Label(root, text="Table Booking Form", font=("Helvetica", 16, "bold")).pack(pady=10)

name_var = tk.StringVar()
contact_var = tk.StringVar()
date_var = tk.StringVar()
time_var = tk.StringVar()
guests_var = tk.StringVar()

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Contact No").pack()
tk.Entry(root, textvariable=contact_var).pack()

tk.Label(root, text="Date (YYYY-MM-DD)").pack()
tk.Entry(root, textvariable=date_var).pack()

tk.Label(root, text="Time (HH:MM, 24hr)").pack()
tk.Entry(root, textvariable=time_var).pack()

tk.Label(root, text="Number of Guests").pack()
tk.Entry(root, textvariable=guests_var).pack()

tk.Button(root, text="Book Table", command=book_table, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Show All Bookings", command=show_bookings, bg="blue", fg="white").pack()

root.mainloop()