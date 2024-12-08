import tkinter as tk
from tkinter import messagebox


# Function to collect and display data
def submit_form():
    employee_data = {
        "Full Name": entry_name.get(),
        "Start Date": entry_start_date.get(),
        "Address": entry_address.get(),
        "Phone Number": entry_phone.get(),
        "Email Address": entry_email.get(),
        "Bank Name": entry_bank_name.get(),
        "Account Number": entry_account_number.get(),
        "Emergency Contact Name": entry_emergency_name.get(),
        "Emergency Contact Phone": entry_emergency_phone.get()
    }

    # Display collected data in a message box for confirmation
    confirmation_message = "\n".join(f"{key}: {value}" for key, value in employee_data.items())
    messagebox.showinfo("Submitted Data", confirmation_message)


# Create main application window
app = tk.Tk()
app.title("EdgeGate Employee Data Form")
app.geometry("600x1000")

# Labels and Entry widgets for each field
tk.Label(app, text="Full Name:").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Start Date (YYYY-MM-DD):").pack()
entry_start_date = tk.Entry(app)
entry_start_date.pack()

tk.Label(app, text="Address:").pack()
entry_address = tk.Entry(app)
entry_address.pack()

tk.Label(app, text="Phone Number:").pack()
entry_phone = tk.Entry(app)
entry_phone.pack()

tk.Label(app, text="Email Address:").pack()
entry_email = tk.Entry(app)
entry_email.pack()

tk.Label(app, text="Bank Name:").pack()
entry_bank_name = tk.Entry(app)
entry_bank_name.pack()

tk.Label(app, text="Account Number:").pack()
entry_account_number = tk.Entry(app)
entry_account_number.pack()

tk.Label(app, text="Emergency Contact Name:").pack()
entry_emergency_name = tk.Entry(app)
entry_emergency_name.pack()

tk.Label(app, text="Emergency Contact Phone:").pack()
entry_emergency_phone = tk.Entry(app)
entry_emergency_phone.pack()

# Submit button
tk.Button(app, text="Submit", command=submit_form).pack(pady=20)

# Run the application
app.mainloop()
