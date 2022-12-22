
import tkinter as tk
import time

root = tk.Tk()
root.geometry("500x200")

time_limit = 30
start_time = time.time()


while True:
    # Check if the time limit has been reached
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        break
    
    root.title("Program1 Elapsed Time: {:.2f} seconds".format(elapsed_time))

    # Update the UI and process events
    root.update()

# Close the window
root.destroy()