# openclaw-workspace-sowork

> A production-ready workspace template for running [OpenClaw](https://github.com/openclaw/openclaw) agents on a VM — with real-world skills for marketing, research, and content.

Built and battle-tested by [SoWork](https://sowork.ai) across 13 markets. Open-sourced for the OpenClaw community.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/Built%20for-OpenClaw-orange)](https://github.com/openclaw/openclaw)
[![SoWork](https://img.shields.io/badge/by-SoWork.ai-blue)](https://sowork.ai)

---

## What is this?

Most OpenClaw workspaces are empty scaffolding. This one has **actual content you can use immediately:**

- ✅ **3 ready-to-use skills** — brand positioning, web research, content writing
- ✅ **AGENTS.md + SOUL.md templates** — real boot sequences and 5 persona examples
- ✅ **A complete marketing team example** — 3 agents running on 1 VM, with cost breakdown
- ✅ **VM setup guide** — step-by-step from a $6/mo VPS to a running OpenClaw agent
- ✅ **Brand-in-SOUL guide** — how to embed brand positioning into your agent's identity

Clone it. Customize it. Run it.

---

## Quick Start

```bash
# Clone to your VM's OpenClaw workspace directory
git clone https://github.com/biombacj-cell/openclaw-workspace-sowork.git ~/.openclaw/workspace

# Or clone and copy files manually
git clone https://github.com/biombacj-cell/openclaw-workspace-sowork.git
cp -r openclaw-workspace-sowork/skills ~/.openclaw/workspace/
cp openclaw-workspace-sowork/AGENTS.md ~/.openclaw/workspace/
cp openclaw-workspace-sowork/SOUL.md ~/.openclaw/workspace/
```

Then start OpenClaw:

```bash
openclaw onboard --install-daemon
openclaw gateway --port 18789
```

---

## What's Included

### Skills (drop into `~/.openclaw/workspace/skills/`)

| Skill | What it does | Trigger |
|-------|-------------|---------|
| `skills/brand-positioning.md` | Brand analysis + campaign strategy | `@assistant Run brand positioning for [Brand]` |
| `skills/web-research.md` | Market research + competitor analysis | `@assistant Research [topic]` |
| `skills/content-writer.md` | Social posts, blog, email, ad copy | `@assistant Write a LinkedIn post about [topic]` |

### Workspace Templates

| File | What it does |
|------|-------------|
| `AGENTS.md` | Boot sequence template — customize for your agent |
| `SOUL.md` | 5 persona templates: strategist, writer, devops, coach, analyst |

### Examples

| Example | What it shows |
|---------|--------------|
| `examples/marketing-team/` | 3-agent marketing team setup, architecture, cost breakdown, workflows |

### Docs

| Doc | What it covers |
|-----|---------------|
| `docs/vm-setup-guide.md` | Full guide: VM provisioning → OpenClaw running → agent connected |
| `docs/brand-in-soul.md` | How to embed brand positioning into SOUL.md |

---

## Directory Structure

```
openclaw-workspace-sowork/
├── skills/
│   ├── brand-positioning.md    # Brand analysis + campaign strategy
│   ├── web-research.md         # Market + competitor research
│   └── content-writer.md       # Content generation for any platform
├── examples/
│   └── marketing-team/
│       └── README.md           # 3-agent marketing team: setup + workflows
├── docs/
│   ├── vm-setup-guide.md       # VM provisioning to running agent
│   └── brand-in-soul.md        # Embedding brand identity into SOUL.md
├── memory/                     # Agent memory files (git-ignored by default)
├── outputs/                    # Agent-generated outputs (git-ignored)
├── scripts/                    # Automation and helper scripts
├── AGENTS.md                   # Boot sequence template
├── SOUL.md                     # Agent persona templates (5 options)
├── CONTRIBUTING.md
├── LICENSE                     # MIT
└── README.md
```

---

## Real-World Use Case

This workspace was built to power SoWork's AI marketing operations:

> **3 agents. 1 VM. 13 markets. ~$50/mo.**
>
> - **CMO Agent** handles brand strategy and campaign briefs
> - **Content Agent** writes social posts, emails, and ad copy
> - **Intel Agent** monitors competitors and market news weekly
>
> Total cost: ~$24/mo VM + ~$25/mo AI tokens = less than a single freelance hour.

See [examples/marketing-team/](examples/marketing-team/) for the full setup.

---

## Who This Is For

- **OpenClaw users** who want a workspace with real content, not just empty folders
- **Marketing teams** exploring AI-assisted content and strategy workflows
- **Developers** building on OpenClaw who want reference skill implementations
- **Anyone** running a self-hosted AI assistant on a VM

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

Ideas:
- New skill prompts (devops, customer support, data analysis)
- Additional SOUL.md persona examples
- More example setups (solo developer, customer service team, etc.)
- Translations of skill prompts into other languages

---

## Related Projects

- [OpenClaw](https://github.com/openclaw/openclaw) — the agent runtime this workspace runs on
- [SoWork](https://sowork.ai) — AI marketing platform built on OpenClaw

---

## License

MIT License. See [LICENSE](LICENSE) for details.
