import tkinter as tk
import subprocess
from tkinter import messagebox

# Functions to run external Python files or commands
def run_script1():
    try:
        # Replace 'your_script.bat' with the actual path to your .bat file
        subprocess.run(["F:\Science Fair\web.bat"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run your_script.bat\n{e}")

def run_script2():
    try:
        subprocess.run(["python", "weather.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script2.py\n{e}")

def run_script3():
    try:
        subprocess.run(["python", "applicationcontrol.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script3.py\n{e}")

def run_script4():
    try:
        subprocess.run(["python", "face_rec.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script4.py\n{e}")

def run_script5():
    try:
        subprocess.run(["python", "gazecontrol.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script5.py\n{e}")

# Setting up the main tkinter window
root = tk.Tk()
root.title("Run External Scripts")
root.geometry("300x200")

# Creating buttons for each script
button1 = tk.Button(root, text="Movie Recomendation", command=run_script1)
button1.pack(pady=5)

button2 = tk.Button(root, text="Weather", command=run_script2)
button2.pack(pady=5)

button3 = tk.Button(root, text="Application Control", command=run_script3)
button3.pack(pady=5)

button4 = tk.Button(root, text="Face Lock", command=run_script4)
button4.pack(pady=5)

button5 = tk.Button(root, text="Gaxe Control", command=run_script5)
button5.pack(pady=5)

# Running the tkinter event loop
root.mainloop()
