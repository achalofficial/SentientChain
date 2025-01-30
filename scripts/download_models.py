import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login, hf_hub_download

# ✅ Securely get the Hugging Face token from an environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("❌ Hugging Face token not found. Please set HF_TOKEN in your environment.")

# ✅ Log in to Hugging Face
login(token=HF_TOKEN)

# ✅ Define models to download
models = [
    {"repo_id": "NousResearch/Nous-Hermes-2-Mistral-7B", "filename": "pytorch_model.bin"},
]

# ✅ Create models directory if it doesn't exist
download_dir = "models"
os.makedirs(download_dir, exist_ok=True)

# ✅ Download each model
for model in models:
    try:
        print(f"🔄 Downloading {model['repo_id']} ...")

        # Download model and tokenizer
        model_path = AutoModelForCausalLM.from_pretrained(model["repo_id"], cache_dir=download_dir)
        tokenizer_path = AutoTokenizer.from_pretrained(model["repo_id"], cache_dir=download_dir)

        print(f"✅ {model['repo_id']} successfully downloaded!")
    except Exception as e:
        print(f"❌ ERROR downloading {model['repo_id']}: {e}")
