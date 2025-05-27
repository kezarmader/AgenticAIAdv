# ─────────────────────────────────────
# agents/platform_selector.py

from autogen import AssistantAgent

class PlatformSelectorAgent(AssistantAgent):
    def __init__(self):
        super().__init__(
            name="PlatformSelector",
            description="Selects platforms for ad posting based on the campaign details.",
            system_message="You are an expert in social media marketing. Based on the product details and target audience, suggest suitable platforms for posting ads.",
            llm_config={
                    "model": "llama2:latest",  # Change to your local model name
                    "base_url": "http://localhost:11434/v1",  # Ollama/LM Studio OpenAI-compatible endpoint
                    "api_key": "ollama",  # Use a dummy key if required by your server
                    "temperature": 0.7,
                    "max_tokens": 1500
                })

    def generate_response(self, messages, sender, config):
        return {"platforms": ["Facebook"]}