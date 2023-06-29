import tkinter as tk
from tkinter import messagebox, filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")

        self.textarea = tk.Text(self.root, undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Dosya", menu=self.file_menu)
        self.file_menu.add_command(label="Yeni", command=self.new_file)
        self.file_menu.add_command(label="Aç", command=self.open_file)
        self.file_menu.add_command(label="Kaydet", command=self.save_file)
        self.file_menu.add_command(label="Farklı Kaydet", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Çıkış", command=self.exit_app)

        self.edit_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Düzenle", menu=self.edit_menu)
        self.edit_menu.add_command(label="Geri Al", command=self.undo)
        self.edit_menu.add_command(label="Yinele", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Kes", command=self.cut)
        self.edit_menu.add_command(label="Kopyala", command=self.copy)
        self.edit_menu.add_command(label="Yapıştır", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Tümünü Seç", command=self.select_all)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.textarea.delete(1.0, tk.END)
                    self.textarea.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Hata", str(e))

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                content = self.textarea.get(1.0, tk.END)
                with open(file_path, "w") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Hata", str(e))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                content = self.textarea.get(1.0, tk.END)
                with open(file_path, "w") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Hata", str(e))

    def exit_app(self):
        self.root.quit()

    def undo(self):
        try:
            self.textarea.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.textarea.edit_redo()
        except tk.TclError:
            pass

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def select_all(self):
        self.textarea.tag_add(tk.SEL, 1.0, tk.END)
        self.textarea.mark_set(tk.INSERT, 1.0)
        self.textarea.see(tk.INSERT)

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
