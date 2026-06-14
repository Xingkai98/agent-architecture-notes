# Two fundamental core loop architectures identified

Analysis of 7 production agent codebases reveals two dominant loop architectures: nested two-loop (pi-mono, openclaw) and flat while-true (claude-code, hermes-agent). The key driver is recovery complexity — flat loops make cascading fallback paths visible in one place; nested loops provide cleaner separation when recovery is simple. A third pattern (explicit state machine, as in nanobot's 7-state TurnState) is viable but less common.

Also identified: batch vs streaming tool execution as a secondary dimension orthogonal to loop structure.

Evidence: direct code reading of all 7 core loop implementations (files and line numbers documented in lesson 0001).
Implications: future lessons on tool systems and context management should analyze whether these architectural choices correlate with specific tool execution or compaction strategies.
