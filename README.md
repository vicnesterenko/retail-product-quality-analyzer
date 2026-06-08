# retail-product-quality-analyzer

Аналізатор якості товарів роздрібного магазину [avrora.ua](https://avrora.ua/).

Скрипт `scraper.py` збирає товари з низьким рейтингом (≤ 3.5) із категорії
сайту та надсилає їх у воркфлоу **n8n** через webhook. Якщо сайт недоступний
або змінив верстку, скрапер автоматично перемикається в **Mock Mode** і
надсилає реалістичні тест-дані, щоб можна було продемонструвати пайплайн n8n.

## Архітектура

```
scraper.py  ──POST /webhook-test/avrora-bad-products──►  n8n workflow
                                                          ├─ Webhook
                                                          ├─ Split Out (body.bad_products)
                                                          ├─ Code (пріоритизація за рейтингом)
                                                          ├─ AI Agent Analyst (Simulation)
                                                          └─ Send to Slack/Telegram (Production Only)
```

Воркфлоу n8n імпортується з файлу `retail-product-quality-analyzer.json`.

## Вимоги

- Python 3.9+
- Docker (для локального запуску n8n)

Залежності Python — у `requirements.txt`:

```
httpx>=0.27
beautifulsoup4>=4.12
```

## 1. Локальний запуск n8n (Docker)

Підняти n8n локально однією командою:

```bash
docker run -d --name n8n -p 5678:5678 \
  -e N8N_PYTHON_ENABLED=true \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Пояснення прапорців:

| Прапорець | Призначення |
|-----------|-------------|
| `-d` | запуск у фоновому режимі (detached) |
| `--name n8n` | ім'я контейнера |
| `-p 5678:5678` | проброс порту, UI доступний на http://localhost:5678 |
| `-e N8N_PYTHON_ENABLED=true` | дозволяє виконання Python-коду в нодах |
| `-v n8n_data:/home/node/.n8n` | том для збереження воркфлоу та налаштувань між перезапусками |

Після старту відкрийте **http://localhost:5678** у браузері та створіть локальний акаунт.

Корисні команди керування контейнером:

```bash
docker logs -f n8n        # дивитися логи
docker stop n8n           # зупинити
docker start n8n          # запустити знову
docker rm -f n8n          # видалити контейнер (том n8n_data лишається)
```

## 2. Імпорт воркфлоу

1. Відкрийте n8n UI → **Workflows** → **Import from File**.
2. Виберіть `retail-product-quality-analyzer.json`.
3. Активуйте воркфлоу або натисніть **Execute Workflow** / **Listen for test event**,
   щоб увімкнути тестовий webhook на шляху `avrora-bad-products`.

> URL webhook у скрапері — `http://localhost:5678/webhook-test/avrora-bad-products`
> (тестовий). Для продакшн-режиму змініть `N8N_WEBHOOK_URL` у `scraper.py` на
> `http://localhost:5678/webhook/avrora-bad-products`.

## 3. Запуск скрапера

Створіть та активуйте віртуальне середовище, встановіть залежності й запустіть:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scraper.py
```

Скрапер обійде категорію, відфільтрує товари з рейтингом ≤ 3.5 і надішле їх у n8n.
У консолі ви побачите статус відповіді від n8n.

## Налаштування

- `target_url` у `scraper.py` — категорія для аналізу
  (за замовчуванням `https://avrora.ua/ximiya-zasobi-dlya-prannya/`).
- `N8N_WEBHOOK_URL` — адреса webhook n8n.