# ─────────────────────────────────────
# agents/poster_agent.py

from autogen import AssistantAgent
from tools.post_to_facebook import post_to_facebook

class PosterAgent(AssistantAgent):
    def __init__(self):
        super().__init__(name="Poster")

    def generate_response(self, messages, sender, config):
        ad_text = messages[-2]['content']['ad_copy']
        platforms = messages[-1]['content']['platforms']
        post_links = []

        for platform in platforms:
            if platform == "Facebook":
                # Assuming post_to_facebook is a function that posts to Facebook and returns the link
                link = post_to_facebook(ad_text)
                post_links.append(link)

        return '\n'.join(post_links)