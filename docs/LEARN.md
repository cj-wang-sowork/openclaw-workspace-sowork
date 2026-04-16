# Five-Layer Learning System

The openclaw-workspace-sowork implements a **Hermes-inspired five-layer learning architecture** that enables agents to learn and improve across enterprise, brand, departmental, team, and personal levels — while maintaining security boundaries and preventing data leakage.

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│ Enterprise Level (learn/enterprise/)                │
│ Organization-wide patterns, no PII, shared knowledge│
├─────────────────────────────────────────────────────┤
│ Brand Level (learn/brand/)                          │
│ Brand guidelines, positioning, public-safe content │
├─────────────────────────────────────────────────────┤
│ Department Level (learn/department/)                │
│ Team-specific strategies, internal-only knowledge  │
├─────────────────────────────────────────────────────┤
│ Team Level (learn/team/)                            │
│ Direct team learnings, member-access restricted    │
├─────────────────────────────────────────────────────┤
│ Personal Level (learn/personal/)                    │
│ Individual patterns, completely private            │
└─────────────────────────────────────────────────────┘
```

## Layer-by-Layer Design

### 1. **Enterprise Level** (`learn/enterprise/`)

**Purpose**: Organization-wide learnings that benefit all teams

**What to Store**:
- Industry patterns and trends
- - Best practices (non-sensitive)
  - - Cross-market insights
    - - Technical learnings
      - - Process improvements
       
        - **Access Control**: `@public` marker
        - **Storage**: Version-controlled, shared across all agents
        - **Example**: `learn/enterprise/marketing-patterns.md`
       
        - **Security**: No PII, no credentials, no confidential information
       
        - ### 2. **Brand Level** (`learn/brand/`)
       
        - **Purpose**: Brand-specific identity, positioning, and guardrails
       
        - **What to Store**:
        - - Brand positioning statement
          - - Tone of voice guidelines
            - - Visual identity guidelines
              - - Product positioning
                - - Messaging frameworks
                  - - Approved brand assets
                   
                    - **Access Control**: `@public` or `@internal` marker
                    - **Storage**: Version-controlled (can be public repository)
                    - **Example**: `learn/brand/voice-and-tone.md`
                   
                    - **Security**: Public-safe content only (DeepEval 0.940 consistency across 13 markets)
                   
                    - ### 3. **Department Level** (`learn/department/`)
                   
                    - **Purpose**: Department-specific knowledge and strategies
                   
                    - **What to Store**:
                    - - Marketing ops workflows
                      - - Campaign templates
                        - - Departmental KPIs
                          - - Team-specific processes
                            - - Internal guidelines
                             
                              - **Access Control**: `@internal` marker (member-only)
                              - **Storage**: Version-controlled but access-restricted
                              - **Example**: `learn/department/content-calendar-template.md`
                             
                              - **Security**: Internal-only, not for public sharing
                             
                              - ### 4. **Team Level** (`learn/team/`)
                             
                              - **Purpose**: Direct team learnings and experimentation results
                             
                              - **What to Store**:
                              - - A/B test results
                                - - Campaign post-mortems
                                  - - Team-specific preferences
                                    - - Experimentation logs
                                      - - Team rituals and workflows
                                       
                                        - **Access Control**: `@team-private` marker
                                        - **Storage**: Local version control, member-access restricted
                                        - **Example**: `learn/team/q2-growth-experiments.md`
                                       
                                        - **Security**: Visible to team members only
                                       
                                        - ### 5. **Personal Level** (`learn/personal/`)
                                       
                                        - **Purpose**: Individual agent and human learnings
                                       
                                        - **What to Store**:
                                        - - Personal preferences
                                          - - Learning journals
                                            - - Individual experiment notes
                                              - - Coaching feedback
                                                - - Personal development goals
                                                 
                                                  - **Access Control**: `@private` marker (NEVER committed)
                                                  - **Storage**: **NOT version-controlled** (covered by .gitignore)
                                                  - **Example**: Not stored in git
                                                 
                                                  - **Security**: Completely private, deleted after sessions
                                                 
                                                  - ---

                                                  ## Security Model

                                                  ### Access Control Markers

                                                  Every learning file should include an access control marker in the metadata:

                                                  ```markdown
                                                  ---
                                                  title: "Learning Title"
                                                  level: "brand"           # enterprise | brand | department | team | personal
                                                  access: "@public"        # @public | @internal | @team-private | @private
                                                  created: "2026-04-17"
                                                  author: "Agent-Name"
                                                  ---
                                                  ```

                                                  ### Enforcement

                                                  - **Enterprise**: No authentication needed (public)
                                                  - - **Brand**: Same authentication as project (internal team)
                                                    - - **Department**: Department-level access control
                                                      - - **Team**: Team-level access control
                                                        - - **Personal**: Local storage only, never git-tracked
                                                         
                                                          - ### Never Shared
                                                         
                                                          - Files with these markers are NEVER:
                                                          - - Committed to git: `.gitignore` blocks `learn/personal/`
                                                            - - Shared in group chats: MEMORY.md isolation applies
                                                              - - Leaked to sub-agents: Access controls enforced
                                                                - - Exposed in logs: Sanitized before logging
                                                                 
                                                                  - ---

                                                                  ## Integration with MEMORY.md

                                                                  **Key Principle**: LEARN is different from MEMORY

                                                                  | Aspect | LEARN | MEMORY |
                                                                  |--------|-------|--------|
                                                                  | **Purpose** | Systematic knowledge building | Contextual session history |
                                                                  | **Scope** | Persistent, cross-session | Session-specific |
                                                                  | **Access** | Layer-based controls | Main-session-only gate |
                                                                  | **Privacy** | Mix of public/private | Always private |
                                                                  | **Usage** | Query and improve | Context injection |

                                                                  Example:
                                                                  - **LEARN**: "Users in market X prefer concise headlines (enterprise learning)"
                                                                  - - **MEMORY**: "In this session, client ABC gave negative feedback on length"
                                                                   
                                                                    - ---

                                                                    ## File Structure

                                                                    ```
                                                                    learn/
                                                                    ├── enterprise/
                                                                    │   ├── industry-trends.md
                                                                    │   ├── marketing-patterns.md
                                                                    │   └── technical-insights.md
                                                                    ├── brand/
                                                                    │   ├── voice-and-tone.md
                                                                    │   ├── positioning-framework.md
                                                                    │   └── visual-guidelines.md
                                                                    ├── department/
                                                                    │   ├── content-calendar-template.md
                                                                    │   ├── seo-best-practices.md
                                                                    │   └── campaign-workflows.md
                                                                    ├── team/
                                                                    │   ├── q2-growth-experiments.md
                                                                    │   ├── team-preferences.md
                                                                    │   └── meeting-notes.md
                                                                    └── personal/              (⚠️ NOT GIT-TRACKED)
                                                                        ├── agent-learnings.md
                                                                        └── personal-notes.md
                                                                    ```

                                                                    ---

                                                                    ## Best Practices

                                                                    ### Creating Learning Files

                                                                    1. **Determine the level**: Ask "Who needs to use this?"
                                                                    2.    - Everyone → Enterprise
                                                                          -    - Brand team → Brand
                                                                               -    - Department team → Department
                                                                                    -    - Direct team → Team
                                                                                         -    - Only me → Personal
                                                                                          
                                                                                              - 2. **Add metadata**: Always include access marker and author
                                                                                               
                                                                                                3. 3. **Make it queryable**: Use clear headings and structure
                                                                                                  
                                                                                                   4. 4. **Version control**: Keep enterprise/brand/department/team in git
                                                                                                      5.    - Personal: `.gitignore` → never committed
                                                                                                        
                                                                                                            - ### Querying Learnings
                                                                                                        
                                                                                                            - Agents should query learnings at startup:
                                                                                                        
                                                                                                            - ```markdown
                                                                                                              ## Bootstrap Sequence

                                                                                                              1. Load SOUL.md (personality)
                                                                                                              2. Load TOOLS.md (environment)
                                                                                                              3. Query learn/brand/*.md (brand consistency)
                                                                                                              4. Query learn/[department]/*.md (department learnings)
                                                                                                              5. Query learn/team/*.md (team context)
                                                                                                              6. Load MEMORY.md (main session only)
                                                                                                              ```
                                                                                                              
                                                                                                              ### Preventing Leakage
                                                                                                              
                                                                                                              - ✅ Check `.gitignore` blocks `learn/personal/`
                                                                                                              - - ✅ Verify MEMORY.md is main-session-only
                                                                                                                - - ✅ Tag all files with access markers
                                                                                                                  - - ✅ Sanitize logs before sharing
                                                                                                                    - - ✅ Review quarterly for accidental credentials
                                                                                                                     
                                                                                                                      - ---
                                                                                                                      
                                                                                                                      ## Cross-Market Scalability
                                                                                                                      
                                                                                                                      This design enables the workspace to scale across **13+ markets simultaneously** without:
                                                                                                                      
                                                                                                                      - Leaking market-specific learnings to other markets
                                                                                                                      - - Exposing personal agent data
                                                                                                                        - - Fragmenting brand consistency
                                                                                                                          - - Requiring separate deployments
                                                                                                                           
                                                                                                                            - Each market:
                                                                                                                            - - Uses shared `learn/enterprise/` and `learn/brand/`
                                                                                                                              - - Maintains separate `learn/department/` (market-specific)
                                                                                                                                - - Has isolated `learn/team/` per market team
                                                                                                                                  - - Keeps `learn/personal/` local-only
                                                                                                                                   
                                                                                                                                    - Result: **DeepEval 0.940 brand consistency across all 13 markets**
                                                                                                                                   
                                                                                                                                    - ---
                                                                                                                                    
                                                                                                                                    ## Integration with Other Workspace Files
                                                                                                                                    
                                                                                                                                    | File | Usage | Connection |
                                                                                                                                    |------|-------|------------|
                                                                                                                                    | SOUL.md | Agent personality | Brand learnings inform SOUL |
                                                                                                                                    | AGENTS.md | Routing rules | Query learnings in routing decisions |
                                                                                                                                    | HEARTBEAT.md | Periodic tasks | Review learnings every 24h |
                                                                                                                                    | MEMORY.md | Session context | Separate from learnings (session-specific) |
                                                                                                                                    | TOOLS.md | API config | Environment-specific learning queries |
                                                                                                                                    
                                                                                                                                    ---
                                                                                                                                    
                                                                                                                                    ## Maintenance & Auditing
                                                                                                                                    
                                                                                                                                    ### Weekly Audit
                                                                                                                                    ```bash
                                                                                                                                    # Check for accidental credentials
                                                                                                                                    grep -r "password\|api_key\|token" learn/

                                                                                                                                    # Check for PII
                                                                                                                                    grep -r "email\|phone\|ssn" learn/

                                                                                                                                    # Verify .gitignore is working
                                                                                                                                    git status learn/personal/
                                                                                                                                    ```
                                                                                                                                    
                                                                                                                                    ### Monthly Review
                                                                                                                                    - Delete stale learnings
                                                                                                                                    - - Archive completed experiments
                                                                                                                                      - - Update access markers if needed
                                                                                                                                        - - Review cross-market learnings for conflicts
                                                                                                                                         
                                                                                                                                          - ### Quarterly Compliance
                                                                                                                                          - - Ensure no personal data in shared layers
                                                                                                                                            - - Verify GDPR/SOC2 compliance
                                                                                                                                              - - Audit access control enforcement
                                                                                                                                                - - Update learning guidelines
                                                                                                                                                 
                                                                                                                                                  - ---
                                                                                                                                                  
                                                                                                                                                  ## Questions?
                                                                                                                                                  
                                                                                                                                                  For more information, see:
                                                                                                                                                  - **Security**: See SECURITY.md for data isolation and access controls
                                                                                                                                                  - - **Workspace Design**: See AGENTS.md for integration points
                                                                                                                                                    - - **Memory System**: See MEMORY.md for session-specific context (different from learnings)
