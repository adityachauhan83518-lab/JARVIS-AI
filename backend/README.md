## Backend setup

```bash
python -m venv .venv
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Set `AI_BASE_URL`, `AI_API_KEY`, and `AI_MODEL` in `.env`. Never commit `.env` or secrets.
