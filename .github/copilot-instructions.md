# Repo-wide Copilot Review Rules

## General
- Flag missing null/None checks on external data (API, DB, file inputs).
- Flag N+1 query patterns in data pipeline / ORM code.
- Flag hardcoded secrets, API keys, or credentials.
- Prefer vectorized pandas/numpy operations over row-wise loops in ML pipeline code.

## Scope boundaries (BU ownership)
This repo is shared across multiple Business Units (BU): Aquaculture, Livestock, Food Manufacturing.
- Each BU owns its own path: `/aquaculture/**`, `/livestock/**`, `/food-mfg/**`.
- `/shared/**` contains common schemas/utils used by multiple BUs.
- A PR that modifies `/shared/**` AND is not explicitly labeled as a cross-BU change must be flagged as "out of scope / needs cross-BU review".
- A PR that modifies files under a BU path different from the PR author's stated team must be flagged as "scope mismatch — verify ownership".
