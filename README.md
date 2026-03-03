---
AIGC:
    ContentProducer: Minimax Agent AI
    ContentPropagator: Minimax Agent AI
    Label: AIGC
    ProduceID: "00000000000000000000000000000000"
    PropagateID: "00000000000000000000000000000000"
    ReservedCode1: 3046022100c801b8099e212121fbe35447a6d52783f373b8142883af8d165e97b9a47b6be7022100ed77eb952b217cc3074faf8b239f63c0392942b64bcc515882741a6fc73d5010
    ReservedCode2: 304502210096029ebb7a478e4ca131bb93bff6146ab379923054c53e87f80934f3186d57a902200ded198fbcbba4ca0e7874799f36298361701941e4144cdfe7e2c4708efc4518
---

# Feishu Integration Gateway

Enterprise integration gateway for Feishu (飞书) - Messages, Calendar, and Approvals

## Features

- **Message Management**: Send and receive text, rich text, and interactive card messages
- **Calendar Integration**: Create, read, update, and delete calendar events
- **Approval Workflow**: Create and manage approval instances
- **Webhook Support**: Receive real-time events from Feishu

## Quick Start

### Prerequisites

- Python 3.8+
- Feishu Developer Account

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd feishu_integration

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Feishu App credentials
```

### Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Service info |
| `GET /health` | Health check |
| `POST /api/v1/webhook` | Feishu webhook endpoint |
| `POST /api/v1/messages/text` | Send text message |
| `POST /api/v1/messages/card` | Send interactive card |
| `POST /api/v1/calendar/events` | Create calendar event |
| `POST /api/v1/approval/instances` | Create approval instance |

## Feishu Configuration

1. Create an app at [Feishu Open Platform](https://open.feishu.cn/)
2. Get App ID and App Secret
3. Enable required permissions:
   - im.message:send_as_bot
   - im.message:receive
   - calendar:* (for calendar features)
   - approval:* (for approval features)
4. Configure webhook URL in developer console

## License

MIT
