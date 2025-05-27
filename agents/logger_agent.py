# ─────────────────────────────────────
# agents/logger_agent.py

from autogen import AssistantAgent
import csv
import os

class LoggerAgent(AssistantAgent):
    def __init__(self):
        super().__init__(
            name="Logger",
            description="Logs posted ad links to a CSV file.",
            llm_config={
                    "model": "llama2:latest",  # Change to your local model name
                    "base_url": "http://localhost:11434/v1",  # Ollama/LM Studio OpenAI-compatible endpoint
                    "api_key": "ollama",  # Use a dummy key if required by your server
                    "temperature": 0.7,
                    "max_tokens": 1500
                })

    def generate_response(self, messages, sender, config):
        links = messages[-1]['content']['posted_links']
        with open("logs/ad_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for link in links:
                writer.writerow([link])
        return {"log_status": "Logged to ad_log.csv"}