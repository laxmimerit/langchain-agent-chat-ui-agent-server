# Environment Setup - Linux

Complete setup for Langchain Agent Server on Ubuntu/Linux.

## Prerequisites

- Ubuntu 20.04+ or compatible Linux distribution
- 8GB RAM minimum
- 100GB free disk space
- Internet connection

## 1. Update System

```bash
sudo apt update && sudo apt upgrade -y
cd ~
```

## 2. Install uv (Python Package Manager)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

Verify installation:
```bash
uv --version
```

## 3. Install LangGraph CLI

```bash
pip install -U langgraph-cli
# Optional: with in-memory server support
pip install -U "langgraph-cli[inmem]"
```

Verify:
```bash
langgraph --help
```

## 4. Install Node.js via nvm

Install nvm:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
```

Install Node.js 24 LTS (latest):
```bash
nvm install 24
nvm use 24
```

Install Yarn:
```bash
npm install -g yarn
# Or use Corepack (built into Node.js 16.9+)
corepack enable
corepack prepare yarn@stable --activate
```

Verify:
```bash
node --version
npm --version
yarn --version
```

## 5. Configure API Keys

Create `.env` file in your project root:

```bash
# LangSmith (recommended for tracing)
LANGSMITH_API_KEY="lsv2_your-key-here"
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="multi-agent-research"

# Optional API keys
GOOGLE_API_KEY="your-google-key-here"
OLLAMA_API_KEY="your-ollama-key-here"
WEATHER_API_KEY="your-weather-key-here"
OPENAI_API_KEY="your-opneai-keys"
```

Get API keys from:
- LangSmith: https://smith.langchain.com/
- Google: https://makersuite.google.com/app/apikey

## 6. Clone and Setup Backend

```bash
git clone https://github.com/laxmimerit/langchain-agent-server-template.git
cd langchain-agent-server-template
uv sync --upgrade
```

Start LangGraph server:
```bash
langgraph dev --host 0.0.0.0 --allow-blocking
```

Server runs on http://localhost:2024

**Port conflicts:**
```bash
# Backend on different port
langgraph dev --port 8080

# Frontend on different port
PORT=3001 yarn dev
```"# langchain-agent-server-template" 



#### Lib Setup

uv python install 3.13
uv venv --python 3.13
uv sync --upgrade
uv add -U "langgraph-cli[inmem]"
uv add -U langgraph-api