# Yamzy: An Agentic Augmented Development Kata

Yamzy is a dice game designed specifically as a software craftsmanship exercise to practice **Agentic Augmented Development**.

## 🎯 The Goal
Implement the scoring engine and dice mechanics for Yamzy while collaborating with an AI agent. The exercise focuses on preventing **AI hallucinations** by providing precise context and using Test-Driven Development (TDD).

## 🚀 Getting Started
To begin the kata, follow the step-by-step curriculum in the guide:

👉 **[KATA_GUIDE.md](./KATA_GUIDE.md)**

### Key Learning Objectives
- **Context Management**: Master context to prime the AI.
- **Red-Green-Refactor**: Lead the AI through a TDD loop.
- **Hallucination Prevention**: Identify and neutralize logic "traps".
- **Verification at Scale**: Understand feedback loops harness.

## 📜 Rules
Yamzy is played with 5 dice and 3 rolls per turn. While it looks like Yahtzee, many categories have specific formulas designed to test your precision.

## 🛠️ Requirements
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) for dependency management.

### Project Setup
Let `uv` create the virtual environment and install all dependencies (runtime + dev group):

```bash
uv sync
```

Optionally, install the pre-commit hooks:

```bash
uv run pre-commit install
```

Then verify everything works:

```bash
uv run pytest
```
