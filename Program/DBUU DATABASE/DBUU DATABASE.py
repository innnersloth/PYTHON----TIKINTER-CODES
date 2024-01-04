import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("DBUU STUDENT MANAGEMENT SYSTEM")

# background colour for our GUI
win.config(bg="lightgray")

# adding some style to our GUI
style = ttk.Style()

# pick a theme
style.theme_use("default")

style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white"
                )

style.map(
    "treeview",
    background=[("selected", "darkred")]
)

# now we will create our menu

title_label = tk.Label(
    win,
    text="DBUU STUDENT MANAGEMENT SYSTEM",
    font=("arial", 20, "bold"),
    padx=15,
    pady=15,
    border=0,
    relief=tk.GROOVE,
    bg="teal",
    foreground="white"
)
title_label.pack(side=tk.TOP, fill=tk.X)

# left menu

detail_frame = tk.LabelFrame(
    win, text="STUDENT RECORDS",
    font=("Arial", 14),
    bg="lightgray",
    foreground="black",
    relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=570)

# data frame

data_frame = tk.Frame(
    win,
    bg="teal",
    relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=830, height=565)

# label with entry
id_lab = tk.Label(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
id_lab.place(x=20, y=15)

# entry
id_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
id_ent.place(x=110, y=17, width=250, height=30)

# 2
name_lab = tk.Label(
    detail_frame,
    text="Name:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
name_lab.place(x=20, y=65)

# entry
name_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
name_ent.place(x=110, y=65, width=250, height=30)

# 3
gen_lab = tk.Label(
    detail_frame,
    text="Gender:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
gen_lab.place(x=20, y=113)

# entry
gen_ent = ttk.Combobox(
    detail_frame,
    font=("arial", 16),
)
gen_ent["values"] = ("Male", "Female", "others")
gen_ent.place(x=110, y=113, width=250, height=30)

# 4
age_lab = tk.Label(
    detail_frame,
    text="Age:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
age_lab.place(x=20, y=161)

# entry
age_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
age_ent.place(x=110, y=161, width=250, height=30)

# 5
ent_lab = tk.Label(
    detail_frame,
    text="En-date:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
ent_lab.place(x=20, y=209)

# entry
ent_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
ent_ent.place(x=110, y=209, width=250, height=30)

# 6
mid_lab = tk.Label(
    detail_frame,
    text="Mid no:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
mid_lab.place(x=20, y=257)

# entry
mid_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
mid_ent.place(x=110, y=257, width=250, height=30)

# 7
fin_lab = tk.Label(
    detail_frame,
    text="fin. no:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
fin_lab.place(x=20, y=305)

# entry
fin_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
fin_ent.place(x=110, y=305, width=250, height=30)

# 8
gpa_lab = tk.Label(
    detail_frame,
    text="GPA:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black",
)
gpa_lab.place(x=20, y=353)

# entry
gpa_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("arial", 16),
    bg="white",
    foreground="black",
)
gpa_ent.place(x=110, y=353, width=250, height=30)

# database frame

main_frame = tk.Frame(
    data_frame,
    bd=2,
    relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# treeview database

student_table = ttk.Treeview(main_frame, columns=(
    "ID", "name", "Gender", "Age", "Enroll date", "Midterm", "Final", "GPA"
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID", text="ID")
student_table.heading("name", text="Name")
student_table.heading("Gender", text="Gender")
student_table.heading("Age", text="Age")
student_table.heading("Enroll date", text="Enroll date")
student_table.heading("Midterm", text="Midterm")
student_table.heading("Final", text="Final")
student_table.heading("GPA", text="GPA")

student_table["show"] = "headings"

student_table.column("ID", width=100)
student_table.column("name", width=100)
student_table.column("Gender", width=100)
student_table.column("Age", width=100)
student_table.column("Enroll date", width=100)
student_table.column("Midterm", width=100)
student_table.column("Final", width=100)
student_table.column("GPA", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

# default database

data = [
    ["22BTCSE0200", "Anshul", "19", "Male", "2022.08.15", "87", "95", "8.5"],
    ["22BTCSE00164", "Rahul prasad", "20", "Male", "2022.08.10", "85", "96", "7.5"],
    ["22BTCSE0254", "Vaishnavi", "23", "Female", "2022.09.01", "47", "55", "4.5"],
    ["22BTCSEAI0026", "Ishika", "19", "Female", "2022.09.15", "95", "98", "9.5"],
]

# create stripped row tags
student_table.tag_configure("oddrow", background="white")
student_table.tag_configure("evenrow", background="#00AEAE")

global count
count = 0
for record in data:
    if count % 2 == 0:
        student_table.insert(parent="", index="end", iid=count, text="", values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=("evenrow")
        )
    else:
        student_table.insert(parent="", index="end", iid=count, text="", values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=("oddrow")
        )

    count += 1


# functions

# add function
def add_record():
    student_table.tag_configure("oddrow", background="white")
    student_table.tag_configure("evenrow", background="#00AEAE")

    global count
    if count % 2 == 0:
        student_table.insert(parent="", index="end", iid=count, text="", values=(
            id_ent.get(),
            name_ent.get(),
            age_ent.get(),
            gen_ent.get(),
            ent_ent.get(),
            mid_ent.get(),
            fin_ent.get(),
            gpa_ent.get()
        ),
                             tags=("evenrow")
                             )
    else:
        student_table.insert(parent="", index="end", iid=count, text="", values=(
            id_ent.get(),
            name_ent.get(),
            age_ent.get(),
            gen_ent.get(),
            ent_ent.get(),
            mid_ent.get(),
            fin_ent.get(),
            gpa_ent.get()
        ),
                             tags=("oddrow")
                             )
    count += 1


# delete all function
def delete_all():
    for record in student_table.get_children():
        student_table.delete(record)


# delete one function
def delete_one():
    x = student_table.selection()[0]
    student_table.delete(x)


# select record
def select_record():
    id_ent.delete(0, END)
    name_ent.delete(0, END)
    age_ent.delete(0, END)
    gen_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)

    selected = student_table.focus()
    values = student_table.item(selected, "values")

    id_ent.insert(0, values[0])
    name_ent.insert(0, values[1])
    age_ent.insert(0, values[2])
    gen_ent.insert(0, values[3])
    ent_ent.insert(0, values[4])
    mid_ent.insert(0, values[5])
    fin_ent.insert(0, values[6])
    gpa_ent.insert(0, values[7])


# update button
def update_record():
    selected = student_table.focus()
    student_table.item(selected, text="", values=(id_ent.get(), name_ent.get(), age_ent.get(), gen_ent.get(),
                                                  mid_ent.get(), fin_ent.get(), gpa_ent.get()))

    id_ent.delete(0, END)
    name_ent.delete(0, END)
    age_ent.delete(0, END)
    gen_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)


# clear boxes
id_ent.delete(0, END)
name_ent.delete(0, END)
age_ent.delete(0, END)
gen_ent.delete(0, END)
mid_ent.delete(0, END)
fin_ent.delete(0, END)
gpa_ent.delete(0, END)


# buttons

btn_frame = tk.Frame(
    detail_frame,
    bg="lightgray",
    bd=0,
    relief=tk.GROOVE
)
btn_frame.place(x=40, y=400, width=310, height=130)

# add button
add_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Add",
    bd=2,
    font=("arial", 13), width=15,
    command=add_record
)
add_btn.grid(row=0, column=0, padx=2, pady=2)

# update button
update_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Update",
    bd=2,
    font=("arial", 13), width=15,
    command=select_record
)
update_btn.grid(row=0, column=1, padx=2, pady=2)

# print
print_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Calculate",
    bd=2,
    font=("arial", 13), width=15,
)
print_btn.grid(row=1, column=0, padx=2, pady=2)

# save button
cal_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Save",
    bd=2,
    font=("arial", 13), width=15,
    command=update_record
)
cal_btn.grid(row=1, column=1, padx=2, pady=2)

# save button
save_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Clear",
    bd=2,
    font=("arial", 13), width=15,
    command=delete_all
)
save_btn.grid(row=2, column=0, padx=2, pady=2)

# delete button
delete_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Delete",
    bd=2,
    font=("arial", 13), width=15,
    command=delete_one
)
delete_btn.grid(row=2, column=1, padx=2, pady=2)

win.mainloop()
