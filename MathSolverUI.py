import customtkinter as ck
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Slider
import sympy as sp
import sys

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

sys.setrecursionlimit(1500)

class ToplevelWindow(ck.CTkToplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1280x720")
        self.title("Graph")
        self.minsize(1280, 720)
        

        self.label = ck.CTkLabel(self, text="Graph")
        self.label.pack(padx=20, pady=20)

        self.frame = ck.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_equation = ck.CTkLabel(self, text="y = a*x^2 + b*x + c")
        self.label_equation.pack(padx=20, pady=5)

        self.a_label = ck.CTkLabel(self, text="Enter value for 'a':")
        self.a_label.pack(side="left", padx=20, pady=5)

        self.a_entry = ck.CTkEntry(self)
        self.a_entry.pack(side="left", padx=20, pady=5)

        self.b_label = ck.CTkLabel(self, text="Enter value for 'b':")
        self.b_label.pack(side="left", padx=20, pady=5)

        self.b_entry = ck.CTkEntry(self)
        self.b_entry.pack(side="left", padx=20, pady=5)

        self.c_label = ck.CTkLabel(self, text="Enter value for 'c':")
        self.c_label.pack(side="left", padx=20, pady=5)

        self.c_entry = ck.CTkEntry(self)
        self.c_entry.pack(side="left", padx=20, pady=5)

        self.button = ck.CTkButton(self, text="Plot Equation", command=self.plot_equation)
        self.button.pack(padx=20, pady=20)

        self.top_label = ck.CTkLabel(self, text="")
        self.top_label.pack(padx=20, pady=5)

        self.figure = plt.figure(figsize=(5, 4))
        self.ax = self.figure.add_subplot(111)
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        self.top_x = None
        self.top_y = None

    def plot_equation(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            x_vals = np.linspace(-11, 11, 400)
            y_vals = a * x_vals ** 2 + b * x_vals + c

            self.ax.clear()
            self.ax.plot(x_vals, y_vals, label=f'{a}*x**2 + {b}*x + {c}')
            self.ax.set_xlabel('x - axis')
            self.ax.set_ylabel('y - axis')
            self.ax.legend()

            self.cal_top_point()

            self.ax.plot(self.top_x, self.top_y, 'ro')

            self.ax.grid(True)

            self.canvas.draw()

            self.ax.relim()
            self.ax.autoscale_view()

        except ValueError:
            print("Invalid values")

    def cal_top_point(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            x_top = -b / (2 * a)
            y_top = a * x_top ** 2 + b * x_top + c

            top = f"Top point: ({x_top:.2f}, {y_top:.2f})"
            self.top_label.configure(text=top)

            self.top_x = x_top
            self.top_y = y_top

        except ValueError:
            self.top_label.config(text="Invalid values")
            
class Solver(ck.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.geometry("850x400")
        self.title("Solver")
        self.minsize(850, 400)
        
        self.label = ck.CTkLabel(self, text="Solver")
        self.label.pack(padx=20, pady=20)

        self.a_label = ck.CTkLabel(self, text="Enter Equation: ")
        self.a_label.pack(side="left", padx=20, pady=5)
        
        self.a_entry = ck.CTkEntry(self)
        self.a_entry.pack(side="left", padx=20, pady=5)
        
        self.V_label = ck.CTkLabel(self, text="Enter Variable: ")
        self.V_label.pack(side="left", padx=20, pady=5)

        self.V_entry = ck.CTkEntry(self)
        self.V_entry.pack(side="left", padx=20, pady=5)

        self.button = ck.CTkButton(self, text="Solve", command=self.plot_equation)
        self.button.pack(padx=20, pady=20)

        self.Sollabel = ck.CTkLabel(self, text="")
        self.Sollabel.pack(padx=20, pady=5)

    def plot_equation(self):
        equation_str = self.a_entry.get()
        variable_str = self.V_entry.get()

        try:
            equation_parts = equation_str.split('=')
            lhs_expr = sp.sympify(equation_parts[0].strip())
            rhs_expr = sp.sympify(equation_parts[1].strip())
        
            equation = sp.Eq(lhs_expr, rhs_expr)
            variable = sp.Symbol(variable_str)
            solution = sp.solve(equation, variable)

            Solutions = f"Solutions for {variable_str}:\n"
            solutions_text = Solutions + "\n".join(map(str, solution))
            self.Sollabel.configure(text=solutions_text)

        except Exception as e:
            print("Error:", e)

class Earth(ck.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.geometry("850x400")
        self.title("Earth")
        self.minsize(500, 500)
        
        

    def plot_equation(self):
        equation_str = self.a_entry.get()
        variable_str = self.V_entry.get()

        try:
            equation_parts = equation_str.split('=')
            lhs_expr = sp.sympify(equation_parts[0].strip())
            rhs_expr = sp.sympify(equation_parts[1].strip())
        
            equation = sp.Eq(lhs_expr, rhs_expr)
            variable = sp.Symbol(variable_str)
            solution = sp.solve(equation, variable)

            Solutions = f"Solutions for {variable_str}:\n"
            solutions_text = Solutions + "\n".join(map(str, solution))
            self.Sollabel.configure(text=solutions_text)

        except Exception as e:
            print("Error:", e)
            
class App(ck.CTk):
    def __init__(self, master=None):
        self.root = master
        self.root.title("Math")
        self.root.after
        
        self.Mainlabel = ck.CTkLabel(self.root, text="Math Solver", text_color=("white"))
        self.Mainlabel.pack(padx=20, pady=20, anchor="center")

        self.button_1 = ck.CTkButton(self.root, text="Open Graph Drawer", command=self.open_toplevel)
        self.button_1.pack(padx=20, pady=20, anchor="center")
        
        self.button_2 = ck.CTkButton(self.root, text="Open Solver", command=self.open_Solverlevel)
        self.button_2.pack(padx=20, pady=20, anchor="center")
        
        self.optionmenu_var = ck.StringVar(value="500x350")
        self.optionmenu = ck.CTkOptionMenu(self.root, values=["1280x720", "500x350"],
                                           command=self.resolution_change,
                                           variable=self.optionmenu_var)
        self.optionmenu.pack()

        self.solver_instances = []

    def resolution_change(self, selected_option):
        if selected_option == "1280x720":
            self.root.geometry("1280x720")
            self.geometry("1280x720")
        elif selected_option == "500x350":
            self.root.geometry("500x350")
            self.geometry("500x350")

    def open_toplevel(self):
        toplevel_window = ToplevelWindow(self.root)
        self.toplevel_windows.append(toplevel_window)
        
    def open_Solverlevel(self):
        SolvWindow = Solver(self.root)
        self.solver_instances.append(SolvWindow)

if __name__ == "__main__":
    root = ck.CTk()
    root.geometry("500x350")
    app = App(master=root)
    root.mainloop()
