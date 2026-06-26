# AGENTS.md

## Project

Pure Python 3 CLI to convert between Euro Truck Simulator 2 game time and real time. No external dependencies.

## Entrypoints

- `main.py` — entrypoint; run with `python main.py`
- `modules.py` — `ets_time()` contains all conversion logic

## Conversion factor

ETS2 time runs 3× faster than real time.

## State

- Mode 1 (ETS2 → Real) is implemented.
- Mode 2 (Real → ETS2) is **not implemented** — no `elif` branch exists.

## Tooling

No tests, linter, formatter, type checker, build system, or CI are configured. No README exists.
