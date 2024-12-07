from interface import ChatInterface
import tkinter as tk
from llama_cpp import Llama

class LLMChatApp(ChatInterface):
    def __init__(self, root):
        super().__init__(root)
        self.model = Llama(model_path="SmolLM2.gguf", n_ctx=4096, verbose=False)
        self.system_prompt = "Reply concisely."
        
        # Override send button command
        self.send_button.configure(command=self.send_to_llm)
        
        # Display system prompt
        self.chat_display.configure(state='normal')
        #self.chat_display.insert(tk.END, f"System: {self.system_prompt}\n\n")
        self.chat_display.configure(state='disabled')
        
    def generate_response(self, prompt):
        output = self.model.create_completion(
            prompt,
            max_tokens=4096,
            stop=["Human:", "\n\n"],
            echo=False
        )
        return output['choices'][0]['text'].strip()
    
    def send_to_llm(self):
        message = self.input_field.get()
        if message and message != "Enter your questions...":
            # Display user message
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.chat_display.configure(state='disabled')
            
            # Generate and display response
            prompt = f"{self.system_prompt}\n\nHuman: {message}\nAssistant:"
            response = self.generate_response(prompt)
            
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, f"Assistant: {response}\n\n")
            self.chat_display.configure(state='disabled')
            
            # Clear input and scroll to bottom
            self.input_field.delete(0, tk.END)
            self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LLMChatApp(root)
    root.mainloop()