import tkinter as tk

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # main title
        self.title = tk.Label(self, text="Welcome to my python app!")
        self.title.config(font=("Courier", 44))

        self.title2 = tk.Label(self, text="")
        self.title2.config(height = "10")

        # play game button
        self.button = tk.Button(self, text="Play game")
        self.button.config(height="5", background="blue")


        # export and show content
        self.title.pack(side = "top", fill="x")
        self.button.pack(side = "top", fill="x")

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(fill="both", expand=True)
    root.mainloop()
