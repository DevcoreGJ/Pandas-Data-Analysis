import pandas as pd
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Function to select file

def select_file():
	file_path = filedialog.askopenfilename()
	file_entry.delete(0, tk.END)
	file_entry.insert(0, file_path)

#Function to generate plot

def generate_plot():
	category = category_entry.get()
	data = pd.read_csv(file_entry.get())
	grouped_data = data.groupby(category).mean()
	fig = Figure(figsize=(5, 4), dpi=100)
	plot = fig.add_subplot(111)
	plot.bar(grouped_data.index, grouped_data['value'])
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.draw()
	canvas.get_tk_widget().grid(row=8, column=0, columnspan=3)

def main():

	#Create the GUI

	root = tk.Tk()
	root.title("Data Analysis")

	#Select file section

	file_label = tk.Label(root, text="Choose a dataset")
	file_label.grid(row=1, column=0)
	file_entry = tk.Entry(root)
	file_entry.grid(row=2, column=0)
	file_button = tk.Button(root, text="Select File", command=select_file)
	file_button.grid(row=2, column=1)

	#Group by category section

	category_label = tk.Label(root, text="Group by Category")
	category_label.grid(row=3, column=0)
	category_entry = tk.Entry(root)
	category_entry.grid(row=4, column=0)

	#Statistics section

	statistics_label = tk.Label(root, text="Statistics")
	statistics_label.grid(row=5, column=0)
	mean_label = tk.Label(root, text="Mean")
	mean_label.grid(row=6, column=0)
	median_label = tk.Label(root, text="Median")
	median_label.grid(row=6, column=1)
	mode_label = tk.Label(root, text="Mode")
	mode_label.grid(row=6, column=2)
	mean_entry = tk.Entry(root)
	mean_entry.grid(row=7, column=0)
	median_entry = tk.Entry(root)
	median_entry.grid(row=7, column=1)
	mode_entry = tk.Entry(root)
	mode_entry.grid(row=7, column=2)

	#Data Visualization section

	visualization_label = tk.Label(root, text="Data Visualization")
	visualization_label.grid(row=8, column=0)
	plot_button = tk.Button(root, text="Generate Plot", command=generate_plot)
	plot_button.grid(row=9, column=0)

	#Run Analysis button

	run_button = tk.Button(root, text="Run Analysis")
	run_button.grid(row=10, column=0)

	root.mainloop()

if __name__ == "__main__":
	main()
