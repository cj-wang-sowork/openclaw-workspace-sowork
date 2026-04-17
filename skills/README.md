# Atlas Skills Library

Complete local implementation of 1000+ agent skills from official dev teams and the community.

## Directory Structure

```
skills/
├── official-anthropic/          # Anthropic's official Claude Code skills (20+)
│   ├── docx-skill/
│   ├── pptx-skill/
│   ├── xlsx-skill/
│   └── ...
├── official-google/             # Google Gemini & Workspace CLI skills (20+)
│   ├── gemini-api-dev/
│   ├── workspace-cli-drive/
│   └── ...
├── official-microsoft/          # Microsoft Azure & 365 skills (40+)
│   ├── azure-ai-projects/
│   ├── azure-ai-openai/
│   └── ...
├── official-openai/             # OpenAI official skills (30+)
│   ├── figma-integration/
│   ├── doc-tools/
│   └── ...
├── official-vercel/             # Vercel Next.js & React skills (10+)
├── official-cloudflare/         # Cloudflare Workers & AI skills (10+)
├── official-netlify/            # Netlify deployment skills (10+)
├── official-firebase/           # Firebase backend skills (10+)
├── marketing-skills/            # Marketing frameworks (100+)
│   ├── corey-haines/            # SaaS marketing (31 skills)
│   ├── kim-barrett/             # Direct response ads (11 skills)
│   └── ...
├── security-skills/             # Security & compliance (80+)
│   ├── trail-of-bits/           # Smart contracts & threat analysis (18 skills)
│   ├── auth0/                   # Authentication frameworks (13 skills)
│   └── ...
├── development-skills/          # Dev tools & frameworks (150+)
│   ├── hashicorp-terraform/     # Infrastructure (10+ skills)
│   ├── github-workflows/        # CI/CD patterns
│   └── ...
├── data-skills/                 # Data & analytics (50+)
│   ├── duckdb/
│   ├── mongodb/
│   └── ...
├── ai-ml-skills/                # AI/ML platforms (100+)
│   ├── huggingface/             # (12+ skills)
│   ├── openai-models/           # (40+ skills)
│   └── ...
├── design-skills/               # Design & UX (40+)
│   ├── figma/                   # (7+ skills)
│   ├── gsap/                    # Animations (8 skills)
│   └── ...
├── productivity-skills/          # Productivity tools (50+)
│   ├── notion/
│   ├── linear/
│   └── ...
├── community-skills/            # Community-contributed skills (200+)
└── INDEX.json                   # Machine-readable skills catalog
```

## Skills Categories (1000+)

### Official Organization Skills
- **Anthropic** (20+) - Document tools, design, frontend, integrations
- - **Google** (40+) - Gemini API, Workspace, Cloud, Labs
  - - **Microsoft** (140+) - Azure SDK, 365, Copilot, Foundry
    - - **OpenAI** (40+) - Document tools, deployment, security, media
      - - **Vercel** (10+) - React, Next.js, web design
        - - **Cloudflare** (10+) - Workers, AI, Web Performance
          - - **Netlify** (10+) - Deployment, functions, database
            - - **Firebase** (10+) - Authentication, Firestore, hosting
              - - **Stripe, Supabase, Neon, MongoDB, etc.** (100+)
               
                - ### Category Breakdown
                - - 🔒 **Security & Compliance** (80+ skills)
                  - - 💻 **Development & DevOps** (150+ skills)
                    - - 📊 **Data & Analytics** (50+ skills)
                      - - 🎨 **Design & UX** (40+ skills)
                        - - 📱 **Mobile & Frontend** (60+ skills)
                          - - 🤖 **AI/ML & Data Science** (100+ skills)
                            - - 📈 **Marketing & Growth** (100+ skills)
                              - - 🔧 **DevTools & Platforms** (150+ skills)
                                - - 📚 **Enterprise & Productivity** (100+ skills)
                                  - - 🎬 **Content & Media** (30+ skills)
                                   
                                    - ## Using Skills with ATLAS
                                   
                                    - ### 1. Load a Local Skill
                                    - ```bash
                                      # Skills are auto-discovered from atlas/skills/ directory
                                      # Copy to your IDE's skills folder:

                                      cp -r atlas/skills/official-anthropic/docx-skill ~/.claude/skills/
                                      ```

                                      ### 2. Use in Claude Code / Codex / Cursor
                                      ```python
                                      # Skills auto-load from .claude/skills/, .agents/skills/, etc.
                                      # They're immediately available in your IDE

                                      # Example: Document skill
                                      doc = create_word_document("Report.docx")
                                      doc.add_heading("Market Analysis")
                                      doc.add_table(data)
                                      doc.save()
                                      ```

                                      ### 3. Track with ATLAS Learning System
                                      ```python
                                      from atlas import HermesAdapter, MarketRouter

                                      router = MarketRouter()
                                      adapter = HermesAdapter(market_router=router)

                                      # After skill execution, ATLAS learns:
                                      # - Which skills work best per market
                                      # - Success/failure patterns
                                      # - Confidence scores
                                      # - Cross-market recommendations

                                      adapter.observe_access("us-en", "team", "docx_skill", success=True)
                                      recommendations = adapter.get_adaptive_recommendations("us-en", {})
                                      ```

                                      ## Skill Structure

                                      Each skill follows a standard structure:

                                      ```
                                      skill-name/
                                      ├── README.md           # Purpose, keywords, prerequisites
                                      ├── SKILL.md           # Detailed skill specification
                                      ├── manifest.json      # Metadata for IDE discovery
                                      ├── examples/          # Usage examples
                                      │   ├── basic.py
                                      │   ├── advanced.py
                                      │   └── integration.md
                                      ├── tests/             # Test cases
                                      │   └── test_skill.py
                                      └── src/               # Source code (if applicable)
                                          └── implementation.py
                                      ```

                                      ### README.md Template
                                      ```markdown
                                      # Skill Name

                                      **Category**: [Category]
                                      **Keywords**: skill, tool, purpose, related-terms
                                      **Compatibility**: Claude Code, Codex, Cursor, Gemini CLI
                                      **Dependencies**: None (zero-dependency preferred)

                                      ## Purpose
                                      Brief description of what this skill does and when to use it.

                                      ## Usage
                                      ```

                                      ## Contributing Skills

                                      ### Add a New Skill
                                      1. Create directory: `skills/[category]/[skill-name]/`
                                      2. 2. Copy template structure above
                                         3. 3. Fill README.md with clear purpose & keywords
                                            4. 4. Add usage examples
                                               5. 5. Submit PR with description
                                                 
                                                  6. ### Quality Standards
                                                  7. - ✅ Real-world tested (not AI-generated)
                                                     - - ✅ Clear keywords for discovery
                                                       - - ✅ Minimal dependencies
                                                         - - ✅ Works offline
                                                           - - ✅ Cross-platform compatible
                                                            
                                                             - See [../CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.
                                                            
                                                             - ## ATLAS Integration
                                                            
                                                             - Skills integrate seamlessly with ATLAS's five-layer learning:
                                                            
                                                             - ```
                                                               User executes skill
                                                                   ↓
                                                               [SecurityChecker] - Validates access
                                                                   ↓
                                                               [LearnSystem] - Records in five layers
                                                                   ↓
                                                               [HermesAdapter] - Learns patterns
                                                                   ↓
                                                               [MarketRouter] - Isolates per market
                                                                   ↓
                                                               [MarketIntelligence] - Cross-market insights
                                                               ```

                                                               Each execution teaches ATLAS:
                                                               - Which skills succeed in which markets
                                                               - - Patterns that work best
                                                                 - - When to recommend alternatives
                                                                   - - How to adapt automatically
                                                                    
                                                                     - ## Skill Discovery
                                                                    
                                                                     - ### By Category
                                                                     - - `skills/security-skills/` - Security, auth, compliance
                                                                       - - `skills/marketing-skills/` - Marketing, growth, copywriting
                                                                         - - `skills/development-skills/` - Dev tools, frameworks
                                                                           - - `skills/ai-ml-skills/` - AI models, ML workflows
                                                                            
                                                                             - ### By Source
                                                                             - - `skills/official-*/` - Official dev team skills
                                                                               - - `skills/community-skills/` - Community-contributed
                                                                                
                                                                                 - ### By Tools
                                                                                 - - Find skills for Claude Code: `skills/official-anthropic/`
                                                                                   - - Find skills for Next.js: `skills/official-vercel/`
                                                                                     - - Find skills for Azure: `skills/official-microsoft/`
                                                                                      
                                                                                       - ## Performance
                                                                                      
                                                                                       - All local skills in this library are optimized for:
                                                                                       - - **Zero dependencies** (mostly) - Minimal external APIs
                                                                                         - - **Offline operation** - Work without internet
                                                                                           - - **Fast execution** - <1s startup per skill
                                                                                             - - **Low memory** - Lightweight implementations
                                                                                              
                                                                                               - ## Skill Statistics
                                                                                              
                                                                                               - - **Total Skills**: 1000+ (and growing)
                                                                                                 - - **Official Team Skills**: 400+
                                                                                                   - - **Community Skills**: 200+
                                                                                                     - - **Source Repos**: 100+
                                                                                                       - - **Last Updated**: April 17, 2026
                                                                                                        
                                                                                                         - ## Related Documentation
                                                                                                        
                                                                                                         - - **Main ATLAS**: [../README.md](../README.md) - Enterprise learning system
                                                                                                           - - **Skills Hub**: [../SKILLS_HUB.md](../SKILLS_HUB.md) - Skills index & references
                                                                                                             - - **Contributing**: [../CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
                                                                                                               - - **Official Sources**: [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
                                                                                                                
                                                                                                                 - ---
                                                                                                                 
                                                                                                                 **License**: MIT
                                                                                                                 **Maintained by**: ATLAS Team & Community
                                                                                                                 **Last Updated**: April 17, 2026
