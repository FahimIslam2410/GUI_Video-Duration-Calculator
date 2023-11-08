import tkinter as tk
import ttkbootstrap as ttk

duration_list = []
total_seconds = 0

def add_Duration_to_List():
    duration_input = duration_int.get()
    duration_list.append(duration_input)
    add_Duration_Total(duration_input) # Calls add_Duration_Total Function
    output_list = '\n'.join(map(str, duration_list))
    output_string.set(output_list)
    print(duration_list)

def calculate_time(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    total_duration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return total_duration

def add_Duration_Total(duration):
    try:
        global total_seconds
        minutes, seconds = map(int, duration.split(':'))
        converted_seconds = (minutes * 60) + seconds
        total_seconds += converted_seconds
        print(total_seconds) 
        output_total_string.set(f"Total: {calculate_time(total_seconds)}")
        sub_title.config(foreground='black')
    except ValueError:
        sub_title.config(foreground='red')

        def flash_label_color(count):
            if count % 2 == 0:
                sub_title.config(foreground='black')
            else:
                sub_title.config(foreground='red')
            
            if count < 8:  # Flash 8 times (4 times red, 4 times black)
                window.after(500, flash_label_color, count + 1)
            else:
                sub_title.config(foreground='black')

        flash_label_color(0)

        

# window
window = ttk.Window()
window.title('Video Duration Calculator')
window.geometry('400x700')

# title
title_label = ttk.Label(master = window, text = 'Video Duration Calculator', font = 'Calibri 24 bold')
title_label.pack()

# sub title
sub_title = ttk.Label(master = window, text = 'Enter video duration (mm:ss):', font = 'Calibri 12' )
sub_title.pack()

# input field
input_frame = ttk.Frame(master = window)
duration_int = tk.StringVar()
duration_entry = ttk.Entry(master = input_frame, textvariable = duration_int)
button = ttk.Button(master = input_frame, text = 'Add', command = add_Duration_to_List)
duration_entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output list of duration input by user
output_string = tk.StringVar()
number_label = ttk.Label(master = window, 
                         text = 'Output', 
                         font = 'Calibri 16 bold', 
                         textvariable = output_string)
number_label.pack(pady = 10) 

# output current duration total
output_total_string = tk.StringVar()
total_duration_label = ttk.Label(master = window, 
                         text = 'Output', 
                         font = 'Calibri 24 bold', 
                         textvariable = output_total_string)
total_duration_label.pack(pady = 4)


# run
window.mainloop()

