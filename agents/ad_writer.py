# ─────────────────────────────────────
# agents/ad_writer.py

from autogen import AssistantAgent

class AdWriterAgent(AssistantAgent):
    def __init__(self):
        super().__init__(name="AdWriter")

    def generate_response(self, messages, sender, config):
        product = messages[-1]['content']['product']
        price = messages[-1]['content']['price']
        location = messages[-1]['content']['location']
        audience = messages[-1]['content']['target_audience']

        ad_copy = f"\n🔥 Great Deal in {location}! 🔥\n{product} for just {price}!\nPerfect for {audience}.\nDM now or call to grab it! 💻"
        return {"ad_copy": ad_copy}