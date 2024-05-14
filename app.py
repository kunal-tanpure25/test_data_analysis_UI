import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from filter_data import filter_program_data
from plot_data import plotting



class DataAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Analyzer")

        self.filepath = ""

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.label = ttk.Label(master, text="Select a file:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.select_button = ttk.Button(master, text="Select File", command=self.select_file)
        self.select_button.grid(row=0, column=1, padx=10, pady=10)

        self.analyze_button = ttk.Button(master, text="Analyze Data", command=self.analyze_data)
        self.analyze_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.plot_button = ttk.Button(master, text="Plot Graphs", command=self.plot_graphs)
        self.plot_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.insights_button = ttk.Button(master, text="Show Insights", command=self.show_insights)
        self.insights_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def select_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if self.filepath:
            messagebox.showinfo("File Selected", f"Selected file: {self.filepath}")

    def analyze_data(self):
        if self.filepath:
            try:
                self.filtered_data = filter_program_data(self.filepath)
                messagebox.showinfo("Analysis", "Data has been analyzed successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during data analysis: {str(e)}")
        else:
            messagebox.showerror("Error", "Please select a file first!")

    def plot_graphs(self):
        if hasattr(self, 'filtered_data'):
            # Plot graphs using filtered data
            try:
                # Clear any previous plots
                plt.close('all')

                # Plotting
                plotting(self.filtered_data)

                # Show plots in Tkinter window
                self.show_plots()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during plotting: {str(e)}")
        else:
            messagebox.showerror("Error", "Please analyze data first!")

    def show_plots(self):
        # Show plots in a new window
        self.plot_window = tk.Toplevel(self.master)
        self.plot_window.title("Plots")

        # Create a canvas to display plots
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.plot_window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add a toolbar for navigation
        self.toolbar = ttk.Frame(self.plot_window)
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.toolbar_btn = ttk.Button(self.toolbar, text="Close", command=self.plot_window.destroy)
        self.toolbar_btn.pack()

    def show_insights(self):
        if hasattr(self, 'filtered_data'):
            # Perform insights analysis
            try:
                rpm_above_200 = [rpm for rpm in self.filtered_data["rpm"].iloc[:200] if rpm > 200]
                insights = ""
                if rpm_above_200:
                    if rpm_above_200[0] < 230:
                        insights = f"Load sensing rpm is {rpm_above_200} and load size is 10kg"
                    elif rpm_above_200[0] < 260:
                        insights = f"Load sensing rpm is {rpm_above_200} and load size is 8kg"
                    elif rpm_above_200[0] < 290:
                        insights = f"Load sensing rpm is {rpm_above_200} and load size is 5kg"
                    else:
                        insights = "Load Sensing skipped"
                else:
                    insights = "No RPM data above 200 found in the first 200 entries."

                # Show insights in message box
                messagebox.showinfo("Insights", insights)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during insights analysis: {str(e)}")
        else:
            messagebox.showerror("Error", "Please analyze data first!")


def main():
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
