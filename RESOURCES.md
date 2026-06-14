# Agent Architecture Resources

## Knowledge — Primary Codebases

### Coding Agents

- [GitHub: openai/codex](https://github.com/openai/codex)
  OpenAI's open-source coding agent CLI written in Rust (Apache 2.0). ~90k stars. Multi-provider, sandboxed execution, multimodal input support. Use for: studying a production-grade Rust agent harness with strong sandboxing primitives.

- [GitHub: anomalyco/opencode](https://github.com/anomalyco/opencode) (formerly sst/opencode)
  Open-source (MIT) terminal coding agent. TypeScript server + Go TUI (Bubble Tea). Client/server architecture, built-in LSP, ACL permissions, plugin system. ~26k stars. Use for: studying a client/server agent architecture with LSP integration and plugin system.

- [GitHub: badlogic/pi-mono](https://github.com/badlogic/pi-mono)
  Minimalist terminal coding harness by Mario Zechner. TypeScript monorepo with four primitive tools (read/write/edit/bash). Philosophy: "primitives, not features." Use for: studying a maximally minimal agent harness design — the lower bound of complexity.

- [GitHub: Njengah/claude-code-source-code-leak](https://github.com/Njengah/claude-code-source-code-leak) (mirror)
  Claude Code source recovered from npm source map leak (March 2026). ~1,900 TypeScript files, ~512k LOC. React + Ink TUI. Use for: studying Anthropic's production agent architecture — tool loop, permissions, context management, subagent spawning, memory consolidation. *Note: Anthropic proprietary code.*

### General Agents

- [GitHub: openclaw/openclaw](https://github.com/openclaw/openclaw)
  Personal AI assistant. Node/TypeScript. 25+ messaging channels, multi-agent routing, isolated workspaces, Voice Wake + Talk Mode, cron/heartbeat. 13,000+ community skills. Use for: studying a multi-channel, multi-agent personal assistant harness.

- [GitHub: NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
  Self-evolving AI agent framework. Python. ~23k stars. Three-layer memory (MEMORY.md + USER.md + SQLite FTS5), skill creation from experience, sub-agent parallelism, cron scheduler, 40+ tools, MCP integration. Use for: studying memory architecture, skill auto-creation, and self-evolution loops.

- [GitHub: HKUDS/nanobot](https://github.com/HKUDS/nanobot)
  Ultra-lightweight personal AI agent. Python, ~3.5k LOC. WebUI, multi-channel (Telegram/Slack/Discord/Feishu/Matrix/Email/WeChat/DingTalk), MCP integration, persistent memory. Use for: studying a minimal general-agent codebase where the entire system can be read in one session.

## Knowledge — Papers

### Foundational (2022–2023)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — Yao et al., ICLR 2023. The interleaved reasoning-and-action paradigm used by virtually all modern agents.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — Shinn et al., NeurIPS 2023. Self-reflection mechanism for agents to learn from failure.
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) — Yao et al., NeurIPS 2023. Tree-search reasoning for deliberate problem-solving.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — Schick et al., NeurIPS 2023. Demonstrated LLMs can autonomously learn tool use.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — Park et al., ICLR 2023. Agent-based social simulation with memory, planning, and reflection architectures.
- [Cognitive Architectures for Language Agents (CoALA)](https://arxiv.org/abs/2309.02427) — Sumers et al., TMLR 2023. Unified cognitive architecture blueprint for language agents.

### Surveys (2023–2025)
- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — Wang et al., Frontiers of CS. Unified framework: profile, memory, planning, action. One of the most cited surveys.
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) — Xi et al. Three-component framework: Brain, Perception, Action.
- [The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey](https://arxiv.org/abs/2404.11584) — Masterman et al., 2024. Focuses on architectural patterns specifically.
- [Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460) — Luo et al., 2025. Latest methodology-centered taxonomy.
- [Understanding the Planning of LLM Agents: A Survey](https://arxiv.org/abs/2402.02716) — Huang et al., 2024. Dedicated to planning capabilities.
- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13543) — Zhang et al., 2024. Memory design patterns exclusively.

## Knowledge — Books

- [Agentic Design Patterns](https://github.com/Mathews-Tom/Agentic-Design-Patterns) — Antonio Gulli & Mauro Sauco (2024–2025). 21 patterns across 4 sections: Foundational, Advanced Systems, Production Concerns, Multi-Agent Architectures. Free on GitHub. Use for: the most comprehensive pattern catalog available.
- [Building Applications with AI Agents](https://www.oreilly.com/library/view/building-applications-with/9781098163532/) — Michael Albada (O'Reilly, Sep 2025). 354 pages. Single- and multi-agent systems, tools, memory, orchestration patterns, UX design. Use for: broad practical coverage from a major publisher.
- [AI Agent System Design](https://www.amazon.com/dp/B0DR3B5X6V) — Julian F. Faraday (Dec 2025). End-to-end engineering: RAG, function calling, safety, orchestration, evaluation, observability, deployment. Use for: production engineering from scratch.
- [AI Agent Architecture: A Practical Guide to MCP](https://www.amazon.com/dp/B0F2VH6ZK5) — Domenic D. Wood (Aug 2025). Deep dive into MCP as an architectural standard. Use for: understanding MCP protocol design and deployment.

## Knowledge — Technical Blog Posts & Deep Dives

- [The Claude Code source map leak analysis](https://www.secrss.com/articles/88999) — Detailed analysis of what the Claude Code source revealed about Anthropic's agent architecture. Use for: context on Claude Code's internal architecture (dream system, buddy system, ultaplan, etc.).

## Gaps

- No comprehensive comparative analysis of the agent harness design space across these specific codebases exists — that is what this learning track will produce.
- No book-length treatment of agent harness architecture (as distinct from agent application development) was found.
- The pi-mono codebase has limited documentation beyond the README — architecture understanding will require direct code reading.
