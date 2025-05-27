# ─────────────────────────────────────
# agents/platform_selector.py

from autogen import AssistantAgent

class PlatformSelectorAgent(AssistantAgent):
    def __init__(self):
        super().__init__(name="PlatformSelector")

    def generate_response(self, messages, sender, config):
        return ','.join(["Facebook"])  # Currently hardcoded to Facebook, can be extended to select multiple platforms