# Squads GAEACO — Sistema de Agentes de Marketing

Sistema multi-squad com 74 agentes especializados em marketing, branding, copywriting, design, storytelling e trafego pago.

## Squads Disponiveis

### Copy Squad (`copy-squad/`)
**Entry point:** `copy-chief` (Cyrus)
22 copywriters lendarios + 1 orquestrador. Direct response, email, funis, VSLs, cartas de vendas, ofertas.

| Tier | Agentes |
|------|---------|
| Orchestrator | `copy-chief` |
| Direct Response Legends | `gary-halbert`, `eugene-schwartz`, `claude-hopkins`, `gary-bencivenga`, `robert-collier`, `john-carlton`, `jim-rutz` |
| Modern Copy & Funnels | `dan-kennedy`, `frank-kern`, `russell-brunson`, `todd-brown`, `stefan-georgi`, `jon-benson`, `ry-schwartz` |
| Email & Relationship | `ben-settle`, `andre-chaperon`, `dan-koe` |
| Offers & Sales Pages | `joe-sugarman`, `david-ogilvy`, `clayton-makepeace`, `parris-lampropoulos`, `david-deutsch` |

### Brand Squad (`brand-squad/`)
**Entry point:** `brand-chief`
10 pensadores de branding + 4 especialistas funcionais + 1 orquestrador. Brand equity, posicionamento, identidade.

| Tier | Agentes |
|------|---------|
| Orchestrator | `brand-chief` |
| Strategy & Equity | `david-aaker`, `kevin-keller`, `jean-noel-kapferer` |
| Positioning | `al-ries`, `byron-sharp`, `marty-neumeier` |
| Building & Communication | `donald-miller`, `denise-yohn`, `emily-heyward` |
| Identity & Expression | `alina-wheeler`, `archetype-consultant`, `naming-strategist` |
| Support | `domain-scout`, `miller-sticky-brand` |

### Design Squad (`design-squad/`)
**Entry point:** `design-chief`
3 experts + 4 especialistas + 1 orquestrador. Design systems, UX, UI, visual.

| Tier | Agentes |
|------|---------|
| Orchestrator | `design-chief` |
| Experts | `brad-frost`, `dan-mall`, `dave-malouf` |
| Specialists | `ux-designer`, `design-system-architect`, `visual-generator`, `ui-engineer` |

### Storytelling Squad (`storytelling/`)
**Entry point:** `story-chief`
11 mestres do storytelling + 1 orquestrador. Mitologia, screenwriting, narrativa, pitching.

| Tier | Agentes |
|------|---------|
| Orchestrator | `story-chief` |
| Mythic & Structure | `joseph-campbell`, `dan-harmon`, `blake-snyder`, `shawn-coyne` |
| Personal & Business | `matthew-dicks`, `kindra-hall`, `nancy-duarte`, `park-howell` |
| Performance & Movement | `keith-johnstone`, `oren-klaff`, `marshall-ganz` |

### Traffic Masters (`traffic-masters/`)
**Entry point:** `traffic-chief`
15 especialistas em trafego pago + 1 orquestrador. Facebook, YouTube, Google Ads, scaling, tracking.

| Tier | Agentes |
|------|---------|
| Orchestrator | `traffic-chief` |
| Platform Experts | `molly-pittman`, `ralph-burns`, `depesh-mandalia`, `nicholas-kusmich`, `tom-breeze`, `kasim-aslam`, `pedro-sobral` |
| Functional | `ad-midas`, `media-buyer`, `performance-analyst`, `creative-analyst`, `scale-optimizer`, `pixel-specialist`, `ads-analyst`, `fiscal` |

## Como Usar

### Via Chiefs (recomendado)
O melhor caminho e chamar o chief do squad relevante. Ele faz o diagnostico e roteia para o especialista certo:
- **Copywriting:** Chame `copy-chief`
- **Branding:** Chame `brand-chief`
- **Design:** Chame `design-chief`
- **Storytelling:** Chame `story-chief`
- **Trafego pago:** Chame `traffic-chief`

### Direto ao especialista
Se voce ja sabe qual especialista precisa, chame diretamente pelo nome:
- Exemplo: `gary-halbert` para carta de vendas emocional
- Exemplo: `stefan-georgi` para VSL script
- Exemplo: `andre-chaperon` para email sequence

## Recursos por Squad

Cada squad tem:
- `agents/` — Definicoes completas de cada agente
- `tasks/` — Templates de tarefas com inputs, outputs e checklists
- `workflows/` — Fluxos multi-fase orquestrados pelo chief
- `data/` — Catalogos de routing, frameworks e benchmarks
- `checklists/` — Criterios de qualidade para validacao
- `config/` — Configuracao do squad (tiers, handoffs, routing)

## Routing Rapido

| Preciso de... | Squad | Chief | Especialistas-chave |
|---------------|-------|-------|---------------------|
| Carta de vendas | Copy | `copy-chief` | `gary-halbert`, `john-carlton` |
| VSL script | Copy | `copy-chief` | `stefan-georgi`, `jon-benson` |
| Email sequence | Copy | `copy-chief` | `andre-chaperon`, `ben-settle` |
| Headlines | Copy | `copy-chief` | `eugene-schwartz`, `gary-bencivenga` |
| Funnel copy | Copy | `copy-chief` | `russell-brunson`, `frank-kern` |
| Ad copy | Copy | `copy-chief` | `dan-kennedy`, `frank-kern` |
| Brand strategy | Brand | `brand-chief` | `david-aaker`, `kevin-keller` |
| Posicionamento | Brand | `brand-chief` | `al-ries`, `marty-neumeier` |
| Naming | Brand | `brand-chief` | `naming-strategist`, `domain-scout` |
| Brand story | Brand | `brand-chief` | `donald-miller` |
| Design system | Design | `design-chief` | `brad-frost`, `dan-mall` |
| UX flow | Design | `design-chief` | `ux-designer` |
| Narrativa | Story | `story-chief` | `joseph-campbell`, `blake-snyder` |
| Pitch | Story | `story-chief` | `oren-klaff`, `nancy-duarte` |
| Facebook Ads | Traffic | `traffic-chief` | `molly-pittman`, `depesh-mandalia` |
| YouTube Ads | Traffic | `traffic-chief` | `tom-breeze` |
| Google Ads | Traffic | `traffic-chief` | `kasim-aslam` |
| Scaling | Traffic | `traffic-chief` | `scale-optimizer`, `depesh-mandalia` |
