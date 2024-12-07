import tkinter as tk
from tkinter import ttk

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Interface")
        
        # Configure main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Chat display area
        self.chat_display = tk.Text(self.main_frame, height=15, width=50, wrap=tk.WORD, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Scrollbar for chat display
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient='vertical', command=self.chat_display.yview)
        self.scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S))
        self.chat_display['yscrollcommand'] = self.scrollbar.set
        
        # Input field
        self.input_field = ttk.Entry(self.main_frame, width=40)
        self.input_field.grid(row=1, column=0, padx=(0, 5))
        self.input_field.insert(0, "Enter your questions...")
        self.input_field.bind('<FocusIn>', self.clear_placeholder)
        
        # Send button
        self.send_button = ttk.Button(self.main_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)
        
    def clear_placeholder(self, event):
        if self.input_field.get() == "Enter your questions...":
            self.input_field.delete(0, tk.END)
            
    def send_message(self):
        message = self.input_field.get()
        if message and message != "Enter your questions...":
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, f"You: {message}\n\n")
            self.chat_display.configure(state='disabled')
            self.chat_display.see(tk.END)
            self.input_field.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatInterface(root)
    root.mainloop()