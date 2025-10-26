import os
import json
import logging
import sys
from dotenv import load_dotenv
# from fastapi import FastAPI, Request
# import uvicorn
from deepagents import create_deep_agent
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tools import *

# === Logging ===
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# === Load environment ===
load_dotenv()

# === Config ===
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20B")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "local-model")
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
LM_STUDIO_API_KEY = os.getenv("LM_STUDIO_API_KEY", "lm-studio")
DEFAULT_MODEL_PROVIDER = os.getenv("DEFAULT_MODEL_PROVIDER", "ollama")
RECURSION_LIMIT = int(os.getenv("RECURSION_LIMIT", 25))
PORT = int(os.getenv("SERVER_PORT", 8000))

# === Load core instructions ===
with open("instructions.md", "r") as f:
    CORE_INSTRUCTIONS = f.read()

# === Load subagents ===
with open("subagents.json", "r") as f:
    subagents_config = json.load(f)

fundamental_analyst = subagents_config["fundamental_analyst"]
technical_analyst = subagents_config["technical_analyst"]
risk_analyst = subagents_config["risk_analyst"]

# === Tools ===
tools = [get_stock_price, get_financial_statements, get_technical_indicators]
if web_search:
    tools.extend([search_financial_news, search_market_trends])
else:
    logging.warning("⚠️ Web search disabled (no Brave/Tavily API key found).")

# === Model ===
model = ChatOllama(model=OLLAMA_MODEL, temperature=0)

# === Create DeepAgent ===
agent = create_deep_agent(
    tools=tools,
    instructions=CORE_INSTRUCTIONS,
    subagents=[fundamental_analyst, technical_analyst, risk_analyst],
    model=model,
).with_config({"recursion_limit": RECURSION_LIMIT})


