# 🌧️ Rain Alert

A Python script that checks the weather forecast for your location and sends you a Twilio SMS alert if it's going to rain in the next 3 hours. Runs automatically every 3 hours via GitHub Actions.

## How It Works

- Fetches hourly weather data from [Open-Meteo](https://open-meteo.com/) (free, no API key needed)
- Checks the next 3 hours for rain using weather codes
- If rain is detected, sends an SMS via [Twilio](https://www.twilio.com/)
- Scheduled to run every 3 hours using GitHub Actions

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/RainAlertWithTwilio.git
cd RainAlertWithTwilio
```

### 2. Install dependencies

```bash
pip install requests twilio
```

### 3. Set up environment variables

Create a `.env` file in the root directory (never commit this):

```
LAT=your_latitude
LON=your_longitude
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=your_twilio_number
TWILIO_TO_NUMBER=your_personal_number
```

### 4. Run locally

```bash
python main.py
```

## GitHub Actions Setup

To run this automatically every 3 hours in the cloud:

1. Go to your GitHub repo → **Settings → Secrets and variables → Actions**
2. Add the following secrets one by one:

| Secret Name | Value |
|---|---|
| `LAT` | Your latitude |
| `LON` | Your longitude |
| `ACCOUNT_SID` | Twilio Account SID |
| `AUTH_TOKEN` | Twilio Auth Token |
| `TWILIO_FROM_NUMBER` | Your Twilio number |
| `TWILIO_TO_NUMBER` | Your personal number |

The workflow file is already included at `.github/workflows/main.yml` and will trigger automatically.

## GitHub Actions Workflow

Create `.github/workflows/main.yml`:

```yaml
name: Rain Alert

on:
  schedule:
    - cron: '0 */3 * * *'
  workflow_dispatch:

jobs:
  run-rain-alert:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install requests twilio

      - name: Run script
        env:
          LAT: ${{ secrets.LAT }}
          LON: ${{ secrets.LON }}
          TWILIO_ACCOUNT_SID: ${{ secrets.ACCOUNT_SID }}
          TWILIO_AUTH_TOKEN: ${{ secrets.AUTH_TOKEN }}
          TWILIO_FROM_NUMBER: ${{ secrets.TWILIO_FROM_NUMBER }}
          TWILIO_TO_NUMBER: ${{ secrets.TWILIO_TO_NUMBER }}
        run: python main.py
```

## Tech Stack

- Python
- [Open-Meteo API](https://open-meteo.com/) — free weather data, no API key required
- [Twilio](https://www.twilio.com/) — SMS alerts
- GitHub Actions — automated scheduling

## .gitignore

Make sure your `.gitignore` includes:

```
.env
.venv/
__pycache__/
```

## ⚠️ Important

- Never commit your `.env` file or hardcode any credentials in your code
- With a Twilio trial account, you can only send SMS to verified numbers
- GitHub Actions schedules may have a few minutes of delay
