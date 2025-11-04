import tkinter as tk
from tkinter import ttk, messagebox

class QuizBotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Bot")
        self.geometry("500x500")
        self.create_initial_frame()

    def create_initial_frame(self):
        # Clear any existing widgets
        for w in self.winfo_children():
            w.destroy()

        label = ttk.Label(self, text="Coffee piyoge? (yes / no)", font=("Arial", 14))
        label.pack(pady=20)

        yes_button = ttk.Button(self, text="Yes", command=self.on_yes)
        no_button = ttk.Button(self, text="No", command=self.on_no)
        yes_button.pack(pady=5)
        no_button.pack(pady=5)

    def on_no(self):
        messagebox.showinfo("Order", "Okay, maybe next time.")
        self.create_initial_frame()

    def on_yes(self):
        self.choose_coffee_type()

    def choose_coffee_type(self):
        for w in self.winfo_children():
            w.destroy()

        label = ttk.Label(self, text="Options: [1] Black coffee  [2] Regular coffee  [3] Both", font=("Arial", 12))
        label.pack(pady=20)

        btn1 = ttk.Button(self, text="1 – Black coffee", command=lambda: self.black_coffee_flow())
        btn2 = ttk.Button(self, text="2 – Regular coffee", command=lambda: self.regular_coffee_flow())
        btn3 = ttk.Button(self, text="3 – Both", command=lambda: self.both_coffee_flow())
        btn1.pack(pady=5)
        btn2.pack(pady=5)
        btn3.pack(pady=5)

    def black_coffee_flow(self):
        # Step through black coffee selections
        for w in self.winfo_children():
            w.destroy()

        ttk.Label(self, text="Black coffee selected.", font=("Arial", 12)).pack(pady=10)
        ttk.Label(self, text="Choose size: [1] Medium  [2] Large").pack(pady=5)

        btn_med = ttk.Button(self, text="Medium", command=lambda: self.black_size("Medium"))
        btn_large = ttk.Button(self, text="Large", command=lambda: self.black_size("Large"))
        btn_med.pack(pady=5)
        btn_large.pack(pady=5)

    def black_size(self, size):
        for w in self.winfo_children():
            w.destroy()
        if size == "Medium":
            ttk.Label(self, text="30 ml espresso shot for Medium.").pack(pady=5)
        else:
            ttk.Label(self, text="60 ml espresso shot for Large.").pack(pady=5)

        ttk.Label(self, text="Choose sweetener: [1] Stevia  [2] Sugar  [3] None").pack(pady=10)
        btn1 = ttk.Button(self, text="Stevia", command=lambda: self._black_sweetener("Stevia"))
        btn2 = ttk.Button(self, text="Sugar", command=lambda: self._black_sweetener("Sugar"))
        btn3 = ttk.Button(self, text="None", command=lambda: self._black_sweetener("None"))
        btn1.pack(pady=5)
        btn2.pack(pady=5)
        btn3.pack(pady=5)

    def _black_sweetener(self, sweetener):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"{sweetener} selected.").pack(pady=5)
        ttk.Label(self, text="Add ice? (yes / no)").pack(pady=10)
        btn_yes = ttk.Button(self, text="Yes", command=lambda: self._black_ice(True))
        btn_no  = ttk.Button(self, text="No",  command=lambda: self._black_ice(False))
        btn_yes.pack(pady=5)
        btn_no.pack(pady=5)

    def _black_ice(self, ice):
        for w in self.winfo_children():
            w.destroy()
        if ice:
            ttk.Label(self, text="Ice added.").pack(pady=5)
        else:
            ttk.Label(self, text="No ice.").pack(pady=5)
        ttk.Label(self, text="\nYour order has been placed! Thank You!!", font=("Arial", 12, "bold")).pack(pady=20)
        ttk.Button(self, text="Start Over", command=self.create_initial_frame).pack(pady=10)

    def regular_coffee_flow(self):
        # Similar to black but with milk step
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text="Regular coffee selected.", font=("Arial", 12)).pack(pady=10)
        ttk.Label(self, text="Choose size: [1] Medium  [2] Large").pack(pady=5)
        btn_med = ttk.Button(self, text="Medium", command=lambda: self.regular_size("Medium"))
        btn_large = ttk.Button(self, text="Large", command=lambda: self.regular_size("Large"))
        btn_med.pack(pady=5)
        btn_large.pack(pady=5)

    def regular_size(self, size):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"{size} size selected.").pack(pady=5)
        ttk.Label(self, text="Choose milk type: [1] Soy  [2] Almond  [3] Regular").pack(pady=10)
        btn1 = ttk.Button(self, text="Soy",     command=lambda: self._regular_milk("Soy"))
        btn2 = ttk.Button(self, text="Almond",  command=lambda: self._regular_milk("Almond"))
        btn3 = ttk.Button(self, text="Regular", command=lambda: self._regular_milk("Regular"))
        btn1.pack(pady=5)
        btn2.pack(pady=5)
        btn3.pack(pady=5)

    def _regular_milk(self, milk_type):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"{milk_type} milk selected.").pack(pady=5)
        ttk.Label(self, text="Choose sweetener: [1] Stevia  [2] Sugar  [3] None").pack(pady=10)
        btn1 = ttk.Button(self, text="Stevia", command=lambda: self._regular_sweetener("Stevia"))
        btn2 = ttk.Button(self, text="Sugar",  command=lambda: self._regular_sweetener("Sugar"))
        btn3 = ttk.Button(self, text="None",   command=lambda: self._regular_sweetener("None"))
        btn1.pack(pady=5)
        btn2.pack(pady=5)
        btn3.pack(pady=5)

    def _regular_sweetener(self, sweetener):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"{sweetener} selected.").pack(pady=5)
        ttk.Label(self, text="Add ice? (yes / no)").pack(pady=10)
        btn_yes = ttk.Button(self, text="Yes", command=lambda: self._regular_ice(True))
        btn_no  = ttk.Button(self, text="No",  command=lambda: self._regular_ice(False))
        btn_yes.pack(pady=5)
        btn_no.pack(pady=5)

    def _regular_ice(self, ice):
        for w in self.winfo_children():
            w.destroy()
        if ice:
            ttk.Label(self, text="Ice added.").pack(pady=5)
        else:
            ttk.Label(self, text="No ice.").pack(pady=5)
        ttk.Label(self, text="\nYour order has been placed! Thank You!!", font=("Arial", 12, "bold")).pack(pady=20)
        ttk.Button(self, text="Start Over", command=self.create_initial_frame).pack(pady=10)

    def both_coffee_flow(self):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text="Both Black and Regular coffee selected.", font=("Arial", 12)).pack(pady=10)
        ttk.Label(self, text="Choose the size combination:").pack(pady=5)
        btn1 = ttk.Button(self, text="Both Medium", command=lambda: self._both_size("Both Medium"))
        btn2 = ttk.Button(self, text="Both Large",  command=lambda: self._both_size("Both Large"))
        btn3 = ttk.Button(self, text="One Medium & One Large", command=lambda: self._both_size("One Medium & One Large"))
        btn1.pack(pady=5)
        btn2.pack(pady=5)
        btn3.pack(pady=5)

    def _both_size(self, size_choice):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"You have selected: {size_choice}").pack(pady=5)

        # Black coffee customization
        ttk.Label(self, text="\n--- Customizing your BLACK COFFEE ---").pack(pady=5)
        ttk.Label(self, text="Choose sweetener: [1] Stevia  [2] Sugar  [3] None").pack(pady=5)
        btn1 = ttk.Button(self, text="Stevia", command=lambda: self._both_black_sweetener("Stevia", size_choice))
        btn2 = ttk.Button(self, text="Sugar",  command=lambda: self._both_black_sweetener("Sugar", size_choice))
        btn3 = ttk.Button(self, text="None",   command=lambda: self._both_black_sweetener("None", size_choice))
        btn1.pack(pady=2)
        btn2.pack(pady=2)
        btn3.pack(pady=2)

    def _both_black_sweetener(self, sweetener_black, size_choice):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"Stevia selected for black coffee." if sweetener_black=="Stevia" 
                   else f"Sugar selected for black coffee." if sweetener_black=="Sugar" 
                   else "No sweetener for black coffee.").pack(pady=5)
        ttk.Label(self, text="Add ice to black coffee? (yes / no)").pack(pady=10)
        btn_yes = ttk.Button(self, text="Yes", command=lambda: self._both_ice_black(True, sweetener_black, size_choice))
        btn_no  = ttk.Button(self, text="No",  command=lambda: self._both_ice_black(False, sweetener_black, size_choice))
        btn_yes.pack(pady=2)
        btn_no.pack(pady=2)

    def _both_ice_black(self, ice_black, sweetener_black, size_choice):
        for w in self.winfo_children():
            w.destroy()
        if ice_black:
            ttk.Label(self, text="Ice added to black coffee.").pack(pady=5)
        else:
            ttk.Label(self, text="No ice for black coffee.").pack(pady=5)

        # Regular coffee customization
        ttk.Label(self, text="\n--- Customizing your REGULAR COFFEE ---").pack(pady=5)
        ttk.Label(self, text="Choose milk type: [1] Soy  [2] Almond  [3] Regular").pack(pady=5)
        btn1 = ttk.Button(self, text="Soy",     command=lambda: self._both_regular_milk("Soy", size_choice))
        btn2 = ttk.Button(self, text="Almond",  command=lambda: self._both_regular_milk("Almond", size_choice))
        btn3 = ttk.Button(self, text="Regular", command=lambda: self._both_regular_milk("Regular", size_choice))
        btn1.pack(pady=2)
        btn2.pack(pady=2)
        btn3.pack(pady=2)

    def _both_regular_milk(self, milk_type, size_choice):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"{milk_type} milk selected for regular coffee.").pack(pady=5)
        ttk.Label(self, text="Choose sweetener: [1] Stevia  [2] Sugar  [3] None").pack(pady=5)
        btn1 = ttk.Button(self, text="Stevia", command=lambda: self._both_regular_sweetener("Stevia", size_choice))
        btn2 = ttk.Button(self, text="Sugar",  command=lambda: self._both_regular_sweetener("Sugar", size_choice))
        btn3 = ttk.Button(self, text="None",   command=lambda: self._both_regular_sweetener("None", size_choice))
        btn1.pack(pady=2)
        btn2.pack(pady=2)
        btn3.pack(pady=2)

    def _both_regular_sweetener(self, sweetener_regular, size_choice):
        for w in self.winfo_children():
            w.destroy()
        ttk.Label(self, text=f"{sweetener_regular} selected for regular coffee.").pack(pady=5)
        ttk.Label(self, text="Add ice to regular coffee? (yes / no)").pack(pady=10)
        btn_yes = ttk.Button(self, text="Yes", command=lambda: self._both_ice_regular(True, size_choice))
        btn_no  = ttk.Button(self, text="No",  command=lambda: self._both_ice_regular(False, size_choice))
        btn_yes.pack(pady=2)
        btn_no.pack(pady=2)

    def _both_ice_regular(self, ice_regular, size_choice):
        for w in self.winfo_children():
            w.destroy()
        if ice_regular:
            ttk.Label(self, text="Ice added to regular coffee.").pack(pady=5)
        else:
            ttk.Label(self, text="No ice for regular coffee.").pack(pady=5)
        ttk.Label(self, text="\nYour order has been placed. Thank You!!", font=("Arial", 12, "bold")).pack(pady=20)
        ttk.Button(self, text="Start Over", command=self.create_initial_frame).pack(pady=10)


if __name__ == "__main__":
    app = QuizBotApp()
    app.mainloop()
