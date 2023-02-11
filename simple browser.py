
import tkinter as tk
from tkinter import ttk
import webbrowser

class Browser:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Browser")

        self.url_label = ttk.Label(self.root, text="URL:")
        self.url_entry = ttk.Entry(self.root, width=50)
        self.go_button = ttk.Button(self.root, text="Go", command=self.load_url)

        self.url_label.pack(side="left", padx=(5, 0), pady=(5, 0))
        self.url_entry.pack(side="left", fill="x", expand=True, padx=(5, 0), pady=(5, 0))
        self.go_button.pack(side="left", padx=(5, 0), pady=(5, 0))

    def load_url(self):
        url = self.url_entry.get()
        if not url.startswith("http"):
            url = "http://" + url
        webbrowser.open_new(url)

if __name__ == "__main__":
    root = tk.Tk()
    browser = Browser(root)
    root.mainloop()
