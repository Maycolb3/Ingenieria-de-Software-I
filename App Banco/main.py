import tkinter as tk
from ui import BancoView

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoView(root)
    root.mainloop()