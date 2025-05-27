# ─────────────────────────────────────
# agents/poster_agent.py

from autogen import AssistantAgent
from tools.post_to_craigslist import post_to_craigslist

class PosterAgent(AssistantAgent):
    def __init__(self):
        super().__init__(name="Poster")

    def generate_response(self, messages, sender, config):
        ad_text = messages[-2]['content']['ad_copy']
        platforms = messages[-1]['content']['platforms']
        post_links = []

        for platform in platforms:
            if platform == "Craigslist":
                link = post_to_craigslist(ad_text)
                post_links.append(link)

        return {"posted_links": post_links}