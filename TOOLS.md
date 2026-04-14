# TOOLS.md — Environment Cheat Sheet

> Environment-specific facts about THIS machine. Loaded every turn by all agents. Keep it short.

---

## SSH / VM Access

```
Host sowork-vm
  HostName YOUR_VM_IP
  User ubuntu
  IdentityFile ~/.ssh/your_key

ssh sowork-vm                          # connect
pm2 status                             # check agent processes
pm2 restart openclaw                   # restart gateway
tail -f ~/.openclaw/logs/gateway.log   # watch logs
```

## OpenClaw Gateway

```
Port:      18789
Start:     openclaw gateway --port 18789
Daemon:    openclaw onboard --install-daemon
Config:    ~/.openclaw/openclaw.json
Workspace: ~/.openclaw/workspace/
Skills:    ~/.openclaw/workspace/skills/
```

## TTS

```
Provider: openai
Voice ID: alloy
```

## Active Channels

```
Telegram   | @your_bot_name
WhatsApp   | +YOUR_NUMBER
```

## Cost Reference

```
VM:         ~$6-24/mo
AI tokens:  ~$25/mo (Claude Sonnet, 3 agents, 13 markets)
Total:      ~$31-50/mo
```

---

*Replace all placeholders. Do NOT put API keys here.*

*Part of [openclaw-workspace-sowork](https://github.com/cj-wang-sowork/openclaw-workspace-sowork)*
