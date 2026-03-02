import os
from tkinter import *
from tkinter import filedialog
import pandas as pd
# need `pip install openpyxl`

# core
def select_folder():
    restore_results()
    # for select folder in dialog
    folder_path = filedialog.askdirectory()

    # if not selected
    if not folder_path:
        return

    total_rows = 0
    excel_files = []
    errors = []

    # find all excel files in directory and save in list
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            excel_files.append(os.path.join(folder_path, file))

    # if not files in directory
    if not excel_files:
        show_results()
        results_output_frame["text"] = "No excel files in folder"
        return

    # work on files with pandas
    for file in excel_files:
        try:
            df = pd.read_excel(file)
            total_rows += len(df)
        except Exception as e:
            show_results()
            errors.append(e)
            results_output_frame["text"] = f"Error reading file: {file}: {e}"

    # if not errors we show results
    if not errors:
        show_results()
        results_output_frame["text"] = f"Total rows: {total_rows} in {len(excel_files)} excel files"
    else:
        print(errors)


# for show result label
def show_results():
    select_button.pack()
    results_output_frame.pack(expand=True)

# for hide result label (user friendly)
def restore_results():
    results_output_frame.pack_forget()
    results_output_frame["text"] = ""

# GUI init
root = Tk()
root.title("Count rows in excel files in folder")
root.geometry("800x600")

# add frame for paddings
main_frame = Frame(root, padx=56, pady=56)
main_frame.pack(fill="both", expand=True)

# create select button
select_button = Button(
    main_frame,
    text="select folder",
    command=select_folder,
    width=20,
    height=4,
    bg="#D9D9D9",
    fg="black",
    font=("Inter", 12),
    border=0)
select_button.pack(expand=True)

# create text for results output
results_output_frame = Label(
    main_frame,
    text="123",
    font=("Inter", 24))
results_output_frame.pack_forget()

root.mainloop()