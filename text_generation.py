from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Get user input
prompt = input("Enter a prompt: ")

# Generate text
result = generator(
    prompt,
    max_length=100,
    num_return_sequences=1,
    temperature=0.7
)

# Display output
print("\nGenerated Text:\n")
print(result[0]['generated_text'])