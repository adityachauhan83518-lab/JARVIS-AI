# JARVIS-AI — Agent Instructions

## Project purpose
JARVIS is a mobile-first personal AI assistant with a static PWA frontend and a FastAPI backend. Keep the existing architecture unless a change is justified by a concrete requirement.

## Required development workflow
1. Inspect the current implementation and relevant ECC guidance before editing.
2. For bug fixes and features, follow test-driven development: reproduce the issue, add a focused test, implement the smallest safe fix, then run relevant tests.
3. Verify API contracts between `frontend/app.js` and `backend/app`; do not assume frontend success means the provider call succeeded.
4. Review the final diff for regressions, accidental secrets, and unrelated changes.

## Security and safety
- Never commit API keys, tokens, passwords, or populated environment files.
- Keep provider credentials in Render environment variables or local ignored `.env` files.
- Validate request input and return safe client-facing errors; keep diagnostic details in server logs without leaking credentials.
- Do not add autonomous shell, browser, account, payment, or external-action execution without a separate threat model, permission model, and explicit user approval.
- Do not claim an action happened unless the relevant tool or service confirms it.

## ECC reference
The upstream ECC project is linked as a Git submodule at `vendor/ECC`. Its source is MIT-licensed. For Codex, consult `vendor/ECC/.codex/AGENTS.md` and relevant skills under `vendor/ECC/.agents/skills/`, especially:
- `tdd-workflow`
- `security-review`
- `verification-loop`
- `api-design`

The submodule is a development-time reference/toolkit. It does not automatically add agents, tools, memory, or model capabilities to the deployed JARVIS web app. See `docs/ECC-INTEGRATION.md` for setup.
