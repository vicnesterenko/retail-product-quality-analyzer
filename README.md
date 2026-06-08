# retail-product-quality-analyzer

A product-quality analyzer for the retail store [avrora.ua](https://avrora.ua/).

The `scraper.py` script collects low-rated products (rating ≤ 3.5) from a site
category and sends them to an **n8n** workflow via webhook. If the site is
unavailable or has changed its markup, the scraper automatically falls back to
**Mock Mode** and sends realistic test data so the n8n pipeline can still be
demonstrated.

## Architecture

```
scraper.py  ──POST /webhook-test/avrora-bad-products──►  n8n workflow
                                                          ├─ Webhook
                                                          ├─ Split Out (body.bad_products)
                                                          ├─ Code (prioritization by rating)
                                                          ├─ AI Agent Analyst (Simulation)
                                                          └─ Send to Slack/Telegram (Production Only)
```

The n8n workflow is imported from `retail-product-quality-analyzer.json`.

## Requirements

- Python 3.9+
- Docker (to run n8n locally)

Python dependencies are in `requirements.txt`:

```
httpx>=0.27
beautifulsoup4>=4.12
```

## 1. Run n8n locally (Docker)

Start n8n locally with a single command:

```bash
docker run -d --name n8n -p 5678:5678 \
  -e N8N_PYTHON_ENABLED=true \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Flag explanation:

| Flag | Purpose |
|------|---------|
| `-d` | run in the background (detached) |
| `--name n8n` | container name |
| `-p 5678:5678` | port mapping; the UI is available at http://localhost:5678 |
| `-e N8N_PYTHON_ENABLED=true` | allows running Python code inside nodes |
| `-v n8n_data:/home/node/.n8n` | volume that persists workflows and settings across restarts |

Once it has started, open **http://localhost:5678** in your browser and create a local account.

Useful container management commands:

```bash
docker logs -f n8n        # follow logs
docker stop n8n           # stop
docker start n8n          # start again
docker rm -f n8n          # remove the container (the n8n_data volume stays)
```

## 2. Import the workflow

1. Open the n8n UI → **Workflows** → **Import from File**.
2. Select `retail-product-quality-analyzer.json`.
3. Activate the workflow, or click **Execute Workflow** / **Listen for test event**
   to enable the test webhook on the `avrora-bad-products` path.

> The webhook URL in the scraper is `http://localhost:5678/webhook-test/avrora-bad-products`
> (test). For production mode, change `N8N_WEBHOOK_URL` in `scraper.py` to
> `http://localhost:5678/webhook/avrora-bad-products`.

## 3. Run the scraper

Create and activate a virtual environment, install the dependencies, and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scraper.py
```

The scraper crawls the category, filters products with a rating ≤ 3.5, and sends
them to n8n. The response status from n8n is printed to the console.

## Configuration

- `target_url` in `scraper.py` — the category to analyze
  (defaults to `https://avrora.ua/ximiya-zasobi-dlya-prannya/`).
- `N8N_WEBHOOK_URL` — the n8n webhook address.