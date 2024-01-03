import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def parcel_bill():
    customer_name = customer_name_var.get()
    parcel_type = parcel_type_var.get()
    weight = float(weight_entry.get())
    service_type = service_type_var.get()
    distance = float(distance_entry.get())

    weight_per_kg = {
        "envelope": 0.1,
        "small box": 0.5,
        "medium box": 1,
        "large box": 2
    }
    price_per_kg = {
        "envelope": 5,
        "small box": 8,
        "medium box": 12,
        "large box": 15
    }
    service_cost = {
        "express": 10,
        "standard": 4.50
    }

    weight_cost = price_per_kg[parcel_type] * weight
    service_cost = service_cost[service_type]
    distance_cost = distance * weight_per_kg[parcel_type]
    total_bill = weight_cost + service_cost + distance_cost

    print(f"Customer Name: {customer_name}")
    print(f"Parcel Type: {parcel_type}")
    total_bill_var.set(f"Total Bill: RM {total_bill:.2f}")
    total_bill_label.config(textvariable=total_bill_var)

    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="parcel_bill"
    )
    cursor = mydb.cursor()

    # Insert data into the MySQL table
    try:
        sql = "INSERT INTO `courier_info` (customer_name, parcel_type, weight, service_type, distance, total_bill) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (customer_name, parcel_type, weight, service_type, distance, total_bill)
        cursor.execute(sql, val)
        mydb.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()

    cursor.close()
    mydb.close()

    if weight <= 0 or distance <= 0:
        messagebox.showerror("Error", "Please enter positive values for weight and distance.")


# Create the main Tkinter window
root = tkinter.Tk()
root.title("Parcel Bill")
root.geometry("300x400")
root.config(bg="#b9d8e4")

style = ttk.Style()
style.theme_use("default")
style.configure("Pink.TLabelframe", background="#f6cab7")
style.configure("Pink.TLabel", background="#f6cab7")

parcel_bill_frame = ttk.LabelFrame(root, text="Parcel Bill", style="Pink.TLabelframe")
title_label = ttk.Label(parcel_bill_frame, text="Parcel Bill")
parcel_bill_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")  # Added sticky to expand frame
title_label.grid(row=0, column=0, sticky="nsew")  # Position the label within the frame

# Spacing and centering elements within the frame
for widget in parcel_bill_frame.winfo_children():
    if isinstance(widget, (ttk.Label, ttk.Entry)):  # Check if widget is Label or Entry
        widget.grid_configure(padx=20, pady=5, sticky="nsew")

customer_name_label = ttk.Label(parcel_bill_frame, text="Customer Name:", style="Pink.TLabel")
customer_name_label.grid(row=0, column=0, padx=5, pady=5)
customer_name_var = tkinter.StringVar()
customer_name_entry = ttk.Entry(parcel_bill_frame)
customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

parcel_type_label = ttk.Label(parcel_bill_frame, text="Parcel Type:", style="Pink.TLabel")
parcel_type_label.grid(row=1, column=0, padx=5, pady=5)
parcel_type_var = tkinter.StringVar(value="choose your parcel type")
parcel_types = ["envelope", "small box", "medium box", "large box"]
parcel_type_combobox = ttk.Combobox(parcel_bill_frame, textvariable=parcel_type_var, values=parcel_types)
parcel_type_combobox.grid(row=1, column=1, padx=5, pady=5)

weight_label = ttk.Label(parcel_bill_frame, text="Weight (kg):", style="Pink.TLabel")
weight_label.grid(row=2, column=0, padx=5, pady=5)
weight_entry = ttk.Entry(parcel_bill_frame)
weight_entry.grid(row=2, column=1, padx=5, pady=5)

service_type_label = ttk.Label(parcel_bill_frame, text="Service Type:", style="Pink.TLabel")
service_type_label.grid(row=3, column=0, padx=5, pady=5)
service_type_var = tkinter.StringVar(value="standard")
service_types = ["express", "standard"]
service_type_combobox = ttk.Combobox(parcel_bill_frame, textvariable=service_type_var, values=service_types)
service_type_combobox.grid(row=3, column=1, padx=5, pady=5)

distance_label = ttk.Label(parcel_bill_frame, text="Distance (km):", style="Pink.TLabel")
distance_label.grid(row=4, column=0, padx=5, pady=5)
distance_entry = ttk.Entry(parcel_bill_frame)
distance_entry.grid(row=4, column=1, padx=5, pady=5)

total_bill_var = tkinter.StringVar()
total_bill_label = ttk.Label(parcel_bill_frame, textvariable=total_bill_var)
total_bill_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create update button
style.configure("Red.TButton", foreground="white", background="red")
update_button = ttk.Button(root, text="Update", command=parcel_bill, style="Red.TButton")
update_button.grid(row=1, column=0, pady=10)

# Centering elements within the root window
root.columnconfigure(0, weight=1)  # Allow the column to expand
root.rowconfigure(0, weight=1)  # Allow the row to expand

root.mainloop()
