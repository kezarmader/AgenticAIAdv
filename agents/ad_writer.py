# ─────────────────────────────────────
# agents/ad_writer.py

from autogen import AssistantAgent

class AdWriterAgent(AssistantAgent):
    def __init__(self):
        print("Initializing AdWriterAgent...")
        # Initialize the agent with a name
        super().__init__(
            name="AdWriter",
            system_message="You are an expert advertise copywriter. Generate engaging ad copy based on product details and target audience.",
            description="Generates social media post based on product details and target audience. Discuss with platform selector to choose platforms for posting.",
            llm_config={
                    "model": "llama2:latest",  # Change to your local model name
                    "base_url": "http://localhost:11434/v1",  # Ollama/LM Studio OpenAI-compatible endpoint
                    "api_key": "ollama",  # Use a dummy key if required by your server
                    "temperature": 0.7,
                    "max_tokens": 1500
                })

    def generate_response(self, messages, sender, config):
        print("Generating ad copy...")
        # Extract product details from the last message
        product = messages[-1]['content']['product']
        price = messages[-1]['content']['price']
        location = messages[-1]['content']['location']
        audience = messages[-1]['content']['target_audience']

        ad_copy = f"\n🔥 Great Deal in {location}! 🔥\n{product} for just {price}!\nPerfect for {audience}.\nDM now or call to grab it! 💻"
        return {"ad_copy": ad_copy}