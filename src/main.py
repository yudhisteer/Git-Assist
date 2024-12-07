from llama_cpp import Llama

# Initialize the model
model = Llama(model_path="SmolLM2.q8.gguf", n_ctx=4096, verbose=False)

# Define the system prompt
system_prompt = "Reply with the git commands asked only."

def generate_response(prompt):
    # Generate a response using create_completion instead of direct call
    output = model.create_completion(
        prompt,
        max_tokens=4096,
        stop=["Human:", "\n\n"],
        echo=False  # Changed to False to avoid echoing the prompt
    )
    return output['choices'][0]['text'].strip()

# Main interaction loop
print("Chat with SmolLM2 Git Expert (type 'quit' to exit)")
print("System: " + system_prompt)

while True:
    user_input = input("Human: ")
    if user_input.lower() == 'quit':
        break
    
    prompt = f"{system_prompt}\n\nHuman: {user_input}\nAssistant:"
    response = generate_response(prompt)
    print("Assistant:", response)