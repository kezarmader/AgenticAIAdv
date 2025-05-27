# ─────────────────────────────────────
# agents/platform_selector.py

from autogen import AssistantAgent

class PlatformSelectorAgent(AssistantAgent):
    def __init__(self):
        super().__init__(name="PlatformSelector")

    def generate_response(self, messages, sender, config):
        return {"platforms": ["Craigslist", "Reddit"]}