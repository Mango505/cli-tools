# AGENTS.md

## Project

Pure Python 3 CLI to convert between Euro Truck Simulator 2 game time and real time. No external dependencies.

## Entrypoints

- `main.py` — entrypoint; run with `python main.py`
- `modules.py` — `ets_time()` contains all conversion logic

## Conversion factor

ETS2 time runs 20× faster than real time. All values are normalized to seconds internally then converted with `real = ets2 / 20` and `ets2 = real * 20`.

## State

- Both modes are implemented.
- Helper functions: `_repr`, `_to_seconds`, `_fmt`.

## Tooling

No tests, linter, formatter, type checker, build system, or CI are configured. No README exists.
