# ─────────────────────────────────────
# agents/logger_agent.py

from autogen import AssistantAgent
import csv
import os

class LoggerAgent(AssistantAgent):
    def __init__(self):
        super().__init__(name="Logger")

    def generate_response(self, messages, sender, config):
        links = messages[-1]['content']['posted_links']
        with open("logs/ad_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for link in links:
                writer.writerow([link])
        return "Logged to ad_log.csv"