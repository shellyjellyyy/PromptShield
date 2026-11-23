# Changelog

All notable changes to the PromptShield project will be documented in this file.

## [1.0.0] - 2026-11-23

### Added
- **Core Architecture & Configuration:**
  - `code/config.py` with path resolution and synthetic canary tokens (`SECRET_ADMIN_TOKEN`, `INTERNAL_DB_HOST`, `VIP_DISCOUNT_CODE`).
  - `.env.example` and `.gitignore` for zero-leak security.
- **Security Taxonomy & Rubrics:**
  - `docs/security_categories.md` covering 6 attack vectors (instruction override, prompt leaking, confidential data disclosure, jailbreak roleplay, edge cases, normal utility).
  - `docs/evaluation_rubric.md` with mathematical formulations of ASR, ARR, FPR, and NSR.
  - `test-data/test_cases.json` containing 15 categorized synthetic tests with canary triggers.
- **Defensive Prompt Iterations:**
  - `prompts/v1/system_prompt.txt` (Naive baseline with raw canaries).
  - `prompts/v2/system_prompt.txt` (Basic directive constraints).
  - `prompts/v3/system_prompt.txt` (Delimited with XML context encapsulation).
  - `prompts/final/system_prompt.txt` (Hardened defense-in-depth with context-aware refusal).
- **Execution & Evaluation Engines:**
  - `code/llm_runner.py` supporting Gemini, OpenAI, Groq, and a high-fidelity local simulation engine.
  - `code/evaluator.py` with automatic pass/fail tagging against confidential triggers and refusal patterns.
  - `code/metrics.py` computing ASR (88.9% down to 0.0%) and ARR (0.0% up to 100.0%).
- **Modern React Security Dashboard:**
  - `dashboard.html` with cyber-grid aesthetic, glassmorphism, Lucide icons, KPI cards, prompt matrix inspection, filterable audit log, and live interactive lab simulator.
  - `code/app.py` standalone zero-dependency HTTP server launcher.
