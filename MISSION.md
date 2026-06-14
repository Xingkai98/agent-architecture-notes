# Mission: Agent Architecture from First Principles

## Why
I want to deeply understand the architectural design space of AI agents — how their harnesses, tool loops, context management, and safety layers are built — so I can make informed architectural decisions when building or evaluating agent systems. I need this grounded in real codebases, not blog-post summaries.

## Success looks like
- I can whiteboard the core loop and component topology of 5+ production agent systems from memory
- I can articulate the key tradeoffs between different harness designs (e.g., structured output vs. free-form, state machine vs. LLM-as-router, implicit vs. explicit context management)
- I can map any new agent system I encounter onto the taxonomy I've built
- I have a curated reference library of canonical papers, books, and codebase links as primary sources

## Constraints
- All claims must be backed by a primary source: codebase (committed to a repo), published paper, technical book, or official documentation
- Learning is structured around studying actual implementations first, then generalizing
- Category split: "general agents" vs. "coding agents" as a working hypothesis

## Out of scope
- Prompt engineering techniques (except where they interact with architecture)
- Model training, fine-tuning, or RLHF
- Agent evaluation/benchmarking frameworks
- Multi-agent swarm/orchestration systems (single-agent focus)
