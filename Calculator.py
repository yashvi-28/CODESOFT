import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Set up the display
        self.display = tk.Entry(root, font=('Arial', 20), bd=10, relief="ridge", justify='right', bg="#f2f2f2", fg="#000")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Define button texts
        self.buttons = [
            ('7', '#e0e0e0'), ('8', '#e0e0e0'), ('9', '#e0e0e0'), ('/', '#f39c12'),
            ('4', '#e0e0e0'), ('5', '#e0e0e0'), ('6', '#e0e0e0'), ('*', '#f39c12'),
            ('1', '#e0e0e0'), ('2', '#e0e0e0'), ('3', '#e0e0e0'), ('-', '#f39c12'),
            ('C', '#c0392b'), ('0', '#e0e0e0'), ('=', '#27ae60'), ('+', '#f39c12')
        ]
        
        # Create buttons
        self.create_buttons()
    
    def create_buttons(self):
        row_val = 1
        col_val = 0
        for text, color in self.buttons:
            tk.Button(
                self.root, text=text, padx=20, pady=20, font=('Arial', 18), 
                bg=color, fg="#000", relief="raised", command=lambda b=text: self.on_button_click(b)
            ).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Make buttons expand with the window
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_rowconfigure(i + 1, weight=1)
    
    def on_button_click(self, button_text):
        current = self.display.get()
        if button_text == 'C':
            self.display.delete(0, tk.END)
        elif button_text == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
calc = Calculator(root)
root.mainloop()




