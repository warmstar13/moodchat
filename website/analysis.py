from gpt4all import GPT4All
from pathlib import Path

def analyze_chat(chat_file):
    model_path = Path(__file__).parent.parent / 'gpt4all' / 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
    model = GPT4All(str(model_path), allow_download=False, device='cpu')
    prompt = "Привет, расскажи что ты можешь"

    response = model.generate(prompt, max_tokens=100)
    return response