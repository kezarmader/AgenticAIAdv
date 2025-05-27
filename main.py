### Project: Agentic Ads AutoGen
# Description: AutoGen-powered multi-agent system to generate and post free ads

# ─────────────────────────────────────
# main.py

from agents.ad_writer import AdWriterAgent
from agents.platform_selector import PlatformSelectorAgent
from agents.poster_agent import PosterAgent
from agents.logger_agent import LoggerAgent
from autogen import GroupChat, GroupChatManager
from tools.post_to_facebook import post_to_facebook

def main():
    # Setup agents
    ad_writer = AdWriterAgent()
    platform_selector = PlatformSelectorAgent()
    poster = PosterAgent()
    logger = LoggerAgent()

    # Group chat manager to coordinate agents
    group_chat = GroupChat([ad_writer, platform_selector, poster, logger])
    manager = GroupChatManager(
                groupchat=group_chat,
                llm_config={
                    "model": "llama2:latest",  # Change to your local model name
                    "base_url": "http://localhost:11434/v1",  # Ollama/LM Studio OpenAI-compatible endpoint
                    "api_key": "ollama",  # Use a dummy key if required by your server
                    "temperature": 0.7,
                    "max_tokens": 1500
                })

    # Start campaign
    campaign_input = {
        "product": "PlastiDip Blue",
        "location": "Dallas, TX",
        "target_audience": "Automobile DIY",
        "price": "$25 each"
    }

    manager.initiate_chat(
        message="Help me with Ad generation and posting. Use agents like platform selector, ad writer, poster, and logger.",
        recipient=ad_writer)

if __name__ == '__main__':
    main()