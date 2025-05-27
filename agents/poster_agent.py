# ─────────────────────────────────────
# agents/poster_agent.py

from autogen import AssistantAgent
from tools.post_to_facebook import post_to_facebook

class PosterAgent(AssistantAgent):
    def __init__(self):
        super().__init__(
            name="Poster",
            system_message="You are an expert in posting ads on social media platforms. Post the ad copy to the selected platforms and return the links to the posts.",
            description="Posts ad copy to selected platforms and returns links to the posts.",
            llm_config={
                    "model": "llama2:latest",  # Change to your local model name
                    "base_url": "http://localhost:11434/v1",  # Ollama/LM Studio OpenAI-compatible endpoint
                    "api_key": "ollama",  # Use a dummy key if required by your server
                    "temperature": 0.7,
                    "max_tokens": 1500
                })

    def generate_response(self, messages, sender, config):
        ad_text = messages[-2]['content']['ad_copy']
        platforms = messages[-1]['content']['platforms']
        post_links = []

        for platform in platforms:
            if platform == "Facebook":
                # Assuming post_to_facebook is a function that posts to Facebook and returns the link
                link = post_to_facebook(ad_text)
                post_links.append(link)

        return {"posted_links": post_links}