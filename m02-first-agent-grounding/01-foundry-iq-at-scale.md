# Background: Foundry IQ and Knowledge at Scale

- Optional segment: explained, not practised today
- Covers the Microsoft module "Build knowledge-enhanced AI agents with Foundry IQ"
- Product details are version-sensitive; verify before use in a project

## Per-agent files versus a shared knowledge platform

| Aspect                | Per-agent files (today)          | Shared knowledge platform (Foundry IQ)              |
| --------------------- | -------------------------------- | --------------------------------------------------- |
| Where knowledge lives | each agent attaches its own copy | several agents share governed sources and retrieval |
| Fits when             | one agent and one document       | many agents, many sources, several owners           |
| Risk                  | copies drift apart               | misconfigured shared source affects every agent     |
| Fixing and auditing   | per agent                        | one place to fix and audit                          |
| Citation quality      | agent-level concern              | platform-level concern                              |

## What changes at scale

- Data sources are configured once and reused by several agents
- Retrieval configuration (what is searched, how many passages) becomes a shared setting
- Citation quality stops being a property of one agent and becomes a property of the platform
- Ownership of each source must be named, as in the single-document case

## When to move

- More than one agent needs the same documents
- Documents change often and must reach every agent at once
- Several teams need governed access to different parts of the knowledge

Applied in Lab 2.2 (file grounding at single-agent scale).
