# openclaw-workspace-sowork

A reference workspace template for running OpenClaw agents on a VM.
Built and maintained by SoWork (https://sowork.ai).

License: MIT

---

## What is this?

This repository is a community workspace template for teams using OpenClaw on a virtual machine. It provides a standardized directory structure for organizing agent skills, memory, automation scripts, and generated outputs.

Use this as a starting point to set up your own OpenClaw VM agent workspace.

---

## Quick Start

Clone this repo to your VM:

    git clone https://github.com/biombacj-cell/openclaw-workspace-sowork.git ~/.openclaw

---

## Directory Structure

    openclaw-workspace-sowork/
    ├── skills/        # Agent skill definitions and configurations
    ├── memory/        # Agent memory files (conversation history, context)
    ├── scripts/       # Automation and helper scripts
    ├── outputs/       # Generated outputs from agent tasks
    ├── .gitignore     # Excludes sensitive files
    └── README.md

### skills/
Place your OpenClaw skill configs here. Each skill defines what your agent can do.

### memory/
Persistent memory files for your agents. Never commit sensitive conversation data.

### scripts/
Shell scripts and automation tools for managing your workspace or triggering agent tasks.

### outputs/
Agents write their results here. Git-ignored by default.

---

## Configuration

OpenClaw reads its main config from ~/.openclaw/openclaw.json.

**Important:** Never commit openclaw.json or any file containing API keys, tokens, or credentials. The included .gitignore covers most cases.

---

## Contributing

Contributions are welcome! Please read CONTRIBUTING.md first.

Ideas for contributions:
- Example skill configs
- Automation scripts
- Documentation improvements
- Multi-language README translations

---

## License

MIT License. See LICENSE for details.

---

## Related Projects

- OpenClaw (https://github.com/openclaw/openclaw) - The agent runtime
- SoWork (https://sowork.ai) - AI marketing platform built on OpenClaw
