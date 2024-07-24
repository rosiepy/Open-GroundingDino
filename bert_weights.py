from transformers import AutoTokenizer, AutoModel

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

tokenizer.save_pretrained(".")
model.save_pretrained(".")

print("Tokenizer and model saved successfully.")
