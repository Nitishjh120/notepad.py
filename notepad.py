import tkinter as tk
from tkinter import filedialog, messagebox


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")
        
        # Text Widget
        self.text_area = tk.Text(self.root, wrap="word", font=("Arial", 12))
        self.text_area.pack(expand=1, fill="both")
        
        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        
        # Initialize file name
        self.file_name = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_name = None
        self.root.title("Notepad - New File")

    def open_file(self):
        self.file_name = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_name:
            with open(self.file_name, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
            self.root.title(f"Notepad - {self.file_name}")

    def save_file(self):
        if self.file_name:
            with open(self.file_name, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Save", "File saved successfully!")
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_name = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_name:
            with open(self.file_name, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Notepad - {self.file_name}")
            messagebox.showinfo("Save As", "File saved successfully!")

    def show_about(self):
 messagebox. showinfo("About Notepad")
(Python Developer Task 3")


if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
