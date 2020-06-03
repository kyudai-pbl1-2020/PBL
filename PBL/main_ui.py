import tkinter as tk

class Application:
    def __init__(self,window):
        window.geometry("600x500")
        window.title("PBL 1 Application")
        self.menu = tk.Menu()

        window.config(menu=self.menu)
        self.subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)  # Main Menu
        self.subMenu.add_command(label="Temporary Menu", command=None)  # Submenus under File
        self.subMenu.add_command(label="Quit", command=window.quit)



def main():
    window = tk.Tk()
    Application(window)
    window.mainloop()

if __name__ == "__main__":
    main()