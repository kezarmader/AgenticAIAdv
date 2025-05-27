### Project: Agentic Ads AutoGen
# Description: AutoGen-powered multi-agent system to generate and post free ads

# ─────────────────────────────────────
# main.py

from agents.ad_writer import AdWriterAgent
from agents.platform_selector import PlatformSelectorAgent
from agents.poster_agent import PosterAgent
from agents.logger_agent import LoggerAgent
from autogen import GroupChat, GroupChatManager

def main():
    # Setup agents
    ad_writer = AdWriterAgent()
    platform_selector = PlatformSelectorAgent()
    poster = PosterAgent()
    logger = LoggerAgent()

    # Group chat manager to coordinate agents
    group_chat = GroupChat([ad_writer, platform_selector, poster, logger])
    manager = GroupChatManager(group_chat)

    # Start campaign
    campaign_input = {
        "product": "PlastiDip Blue",
        "location": "Dallas, TX",
        "target_audience": "Automobile DIY",
        "price": "$25 each"
    }

    manager.initiate_chat(campaign_input)

if __name__ == '__main__':
    main()