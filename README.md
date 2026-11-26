# JARVIS AI

Mobile-first personal AI assistant.

## Project status
Initial repository setup. The starter scaffold provides a responsive PWA frontend and a FastAPI backend with a configurable AI provider adapter.

## ECC development toolkit
The official [ECC agent harness toolkit](https://github.com/affaan-m/ECC) is linked as a pinned Git submodule at `vendor/ECC`. It provides development workflows and reusable skills for Codex and other coding-agent harnesses.

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/adityachauhan83518-lab/JARVIS-AI.git
```

See [ECC integration notes](docs/ECC-INTEGRATION.md) for setup and limitations.

## Safety
No autonomous shell or browser execution is enabled in this initial scaffold. Never commit API keys or other secrets. ECC is a development-time toolkit; it does not automatically add runtime AI capabilities to the deployed JARVIS app.
