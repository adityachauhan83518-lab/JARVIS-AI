# ECC integration in JARVIS-AI

JARVIS-AI references the official upstream [ECC repository](https://github.com/affaan-m/ECC) as a Git submodule at `vendor/ECC`. The submodule is pinned to upstream commit `4adeee6732a12d1540f49a4d50a38ce8c97f9a53` so builds are reproducible rather than silently following a moving branch.

## Initialize the submodule

When cloning JARVIS-AI:

```bash
git clone --recurse-submodules https://github.com/adityachauhan83518-lab/JARVIS-AI.git
```

If JARVIS-AI is already cloned:

```bash
git submodule update --init --recursive
```

## Use ECC with Codex while developing JARVIS

ECC supports Codex as a development harness. In Codex CLI, add the official marketplace and plugin using the upstream documented commands:

```bash
codex plugin marketplace add affaan-m/ECC
codex plugin add ecc@ecc
codex plugin list --json
```

Review the official [ECC Codex instructions](https://github.com/affaan-m/ECC/blob/main/.codex/AGENTS.md) and the project-local instructions in the root `AGENTS.md`. Use the relevant ECC skills for test-driven development, security review, API design, and verification. Avoid layering multiple ECC installation methods into the same Codex environment.

## What this integration does — and does not do

- Keeps the official ECC source connected to the JARVIS repository as a pinned submodule.
- Gives developers a documented path to use ECC skills and workflows when working on JARVIS in Codex.
- Adds JARVIS-specific development and safety instructions in `AGENTS.md`.
- Does **not** fork or copy all 6,000+ ECC files into the JARVIS repository.
- Does **not** install ECC into a user's Codex account automatically.
- Does **not** add an LLM provider, API key, runtime tools, memory, autonomous computer control, or new chat capabilities to the deployed JARVIS application.

ECC is MIT-licensed. Its original source and license remain in the upstream submodule; see `vendor/ECC/LICENSE` after initializing the submodule.
