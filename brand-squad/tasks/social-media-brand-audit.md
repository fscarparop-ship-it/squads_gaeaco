---
task: socialMediaBrandAudit()
responsavel: "@marty-neumeier"
responsavel_type: Agent
atomic_layer: Task
elicit: true

Entrada:
  - campo: brand
    tipo: string
    origem: User Input
    obrigatorio: true
  - campo: social_channels
    tipo: list
    origem: User Input
    obrigatorio: true
  - campo: brand_assets
    tipo: object
    origem: "branding-strategy-guide output OR User Input"
    obrigatorio: false

Saida:
  - campo: Social Media Brand Audit Report
    tipo: string
    destino: Console
    persistido: false

Checklist:
  - "[ ] Swap Test aplicado a cada canal"
  - "[ ] Hand Test aplicado a cada canal"
  - "[ ] Gap entre percepção desejada e percepção real mapeado"
  - "[ ] Plano de correção com prioridades definido"
---

# Task: Social Media Brand Audit

**Task ID:** BRAND-011
**Version:** 1.0.0
**Command:** `*social-media-brand-audit`
**Agent:** Marty Neumeier (marty-neumeier)
**Purpose:** Auditar a presença de uma marca nas redes sociais usando os frameworks de Neumeier — verificando se cada canal reforça ou destrói a percepção desejada, e produzindo um plano de correção priorizado.

---

## Filosofia Central

> "Design is the conscious management of perception."
> — Marty Neumeier

Redes sociais são touchpoints. Cada post, stories, bio, foto de perfil e interação nos comentários é uma oportunidade de reforçar OU destruir a percepção da marca. Esta auditoria aplica os testes de Neumeier a cada canal para identificar onde o Brand Gap está aberto.

---

## Inputs

| Campo | Tipo | Origem | Obrigatório | Validação |
|-------|------|--------|-------------|-----------|
| brand | string | User prompt | Sim | Nome da marca e descrição |
| social_channels | list | User prompt | Sim | Canais a auditar (Instagram, LinkedIn, TikTok, YouTube, X, etc.) |
| brand_assets | object | branding-strategy-guide output | Não | Onlyness Statement, diretrizes visuais, Brand Commitment Matrix |
| competitors | list | User prompt | Não | Concorrentes para benchmark |
| current_metrics | object | User prompt | Não | Métricas atuais (engajamento, alcance, sentimento) |

---

## Precondições

- Pelo menos 1 canal social identificado
- Marca em operação com presença digital existente (ou planejada)
- Idealmente: branding-strategy-guide já executado (fornece o Onlyness Statement como referência)

---

## Fases de Execução

### Fase 1: Diagnóstico Rápido — Brand Gap nas Redes

Antes de auditar canal por canal, identifique o gap macro:

1. **Percepção desejada:** O que a marca QUER que as pessoas sintam?
2. **Percepção real:** O que as redes sociais comunicam HOJE?
3. **Brand Gap:** Qual a distância entre as duas?
4. **Consistência cross-canal:** Os canais contam a mesma história?

Se não houver Onlyness Statement definido, construa um provisório usando a fórmula:
```
Nossa [marca] é a única [categoria] que [benefício único] para [público específico]
```

### Fase 2: Auditoria por Canal — Os 4 Testes de Neumeier

Para CADA canal, aplique:

#### Swap Test
- Substitua mentalmente o logo/nome da marca pelo de um concorrente
- O conteúdo ainda faz sentido? Se sim: o canal é genérico demais
- Avalie: bio, posts recentes, stories, visual geral, tom de voz

#### Hand Test
- Cubra o logo/nome em cada post
- É possível identificar que é ESTA marca? Se não: a identidade visual/verbal é fraca
- Avalie: cores, tipografia, estilo fotográfico, linguagem

#### Concept Test (análise de comentários e DMs)
- O que o público DIZ sobre a marca nas interações?
- As palavras que usam estão alinhadas com o Onlyness Statement?
- Sentimento dominante: positivo, neutro, negativo, indiferente?

#### Field Test (análise de performance)
- Quais posts geram mais reconhecimento (não engajamento — RECONHECIMENTO)
- Posts "on-brand" performam melhor ou pior que posts genéricos?
- O algoritmo está recompensando ou punindo a consistência de marca?

### Fase 3: Análise das 5 Disciplinas por Canal

Para cada canal, avalie o status de cada disciplina:

| Disciplina | Pergunta-Chave |
|-----------|----------------|
| Diferenciação | O conteúdo é reconhecível como ÚNICO neste canal? |
| Colaboração | Quem produz o conteúdo? Há alinhamento com a estratégia? |
| Inovação | O formato é MAYA — avançado mas aceitável para o público? |
| Validação | Os testes acima passaram? |
| Cultivo | Há consistência ao longo do tempo? As "regras tribais" são seguidas? |

### Fase 4: Mapa de Problemas e Priorização

Classifique cada problema encontrado:

| Severidade | Critério | Ação |
|-----------|----------|------|
| **Crítico** | Falha no Swap Test ou Hand Test — identidade genérica | Redesenhar imediatamente |
| **Alto** | Inconsistência cross-canal — cada rede conta uma história diferente | Unificar diretrizes |
| **Médio** | Conceito fraco — público não articula o posicionamento | Ajustar messaging |
| **Baixo** | Oportunidade MAYA — conteúdo correto mas convencional | Inovar dentro da estratégia |

### Fase 5: Plano de Correção

Para cada problema crítico/alto, produza:

1. **Diagnóstico:** O que está errado e por quê
2. **Referência:** Qual diretriz da branding strategy guide está sendo violada
3. **Correção:** Ação específica (não genérica — "mude X para Y porque Z")
4. **Teste:** Como validar que a correção funcionou
5. **Responsável:** Qual squad/agente pode executar (cross-squad routing)

---

## Formato de Output

```markdown
## Auditoria de Marca em Redes Sociais: {Nome da Marca}

**Metodologia:** Marty Neumeier — Brand Gap + Zag + The Brand Flip
**Canais auditados:** {lista de canais}
**Data:** {data}
**Referência:** {Onlyness Statement, se disponível}

---

### 1. Diagnóstico — Brand Gap nas Redes

**Percepção desejada:** {o que a marca quer}
**Percepção real nas redes:** {o que as redes comunicam}
**Gap identificado:** {distância}
**Consistência cross-canal:** {alta/média/baixa — com evidências}

### 2. Auditoria por Canal

#### {Canal 1: ex. Instagram}

| Teste | Resultado | Evidência | Severidade |
|-------|-----------|-----------|------------|
| Swap Test | {pass/fail} | {detalhe} | {crítico/ok} |
| Hand Test | {pass/fail} | {detalhe} | {crítico/ok} |
| Concept Test | {análise} | {detalhe} | {médio/ok} |
| Field Test | {análise} | {detalhe} | {baixo/ok} |

**5 Disciplinas:**
| Disciplina | Status | Nota |
|-----------|--------|------|
| Diferenciação | {score} | {detalhe} |
| Colaboração | {score} | {detalhe} |
| Inovação | {score} | {detalhe} |
| Validação | {score} | {detalhe} |
| Cultivo | {score} | {detalhe} |

**Veredito:** {canal reforça ou destrói a percepção}

#### {Canal 2: ex. LinkedIn}
{mesma estrutura}

### 3. Mapa de Problemas

| # | Canal | Problema | Severidade | Disciplina Violada |
|---|-------|----------|------------|-------------------|
| 1 | {canal} | {problema} | {crítico/alto/médio/baixo} | {disciplina} |

### 4. Plano de Correção

#### Problema 1: {título}
- **Diagnóstico:** {o que está errado}
- **Diretriz violada:** {referência ao branding strategy guide}
- **Correção:** {ação específica}
- **Teste de validação:** {como verificar}
- **Responsável:** {squad/agente}

### 5. Scorecard Geral

| Dimensão | Score (1-10) | Status |
|----------|-------------|--------|
| Consistência cross-canal | {score} | {emoji} |
| Diferenciação por canal | {score} | {emoji} |
| Alinhamento com Onlyness | {score} | {emoji} |
| Inovação (MAYA) | {score} | {emoji} |
| Cultivo e consistência temporal | {score} | {emoji} |
| **Score Geral** | **{média}** | **{status}** |

### 6. Próximos Passos

| Prioridade | Ação | Squad | Timeline |
|-----------|------|-------|----------|
| 1 | {ação} | {squad} | {prazo} |
```

---

## Condições de Veto

- NUNCA audite sem referência ao Onlyness Statement (mesmo que provisório)
- NUNCA avalie estética sem estratégia — "bonito" não é métrica, "reconhecível" é
- NUNCA ignore o Swap Test — é o teste mais revelador de genericidade
- NUNCA trate canais isoladamente — a consistência cross-canal é o que constrói percepção
- NUNCA produza recomendações genéricas — "melhorar o visual" não é ação, "trocar a paleta de X para Y porque Z" é
- NUNCA confunda engajamento com brand equity — likes não medem reconhecimento

---

## Critérios de Conclusão

- [ ] Brand Gap nas redes mapeado (percepção desejada vs. real)
- [ ] Swap Test e Hand Test aplicados a CADA canal auditado
- [ ] 5 Disciplinas avaliadas por canal
- [ ] Mapa de problemas priorizado por severidade
- [ ] Plano de correção com ações específicas (não genéricas)
- [ ] Scorecard geral com score numérico por dimensão
- [ ] Próximos passos com squad/agente responsável e timeline
- [ ] Cross-squad routing definido (design, copy, traffic quando aplicável)

---

## Relacionamentos com Outros Agentes

| Situação | Agente Complementar | Contexto |
|----------|---------------------|----------|
| Estratégia de base ausente | @marty-neumeier (branding-strategy-guide) | Execute o guia primeiro para ter o Onlyness Statement |
| Identidade visual precisa redesign | @alina-wheeler | Wheeler para redesenhar o sistema de identidade |
| Copy dos posts precisa revisão | @copy-chief | Redirecionar para copy-squad com brand voice definido |
| Criativos de ads genéricos | @traffic-chief | Redirecionar para traffic-masters com diretrizes |
| Narrativa de marca fraca | @story-chief | Redirecionar para storytelling com Onlyness como spine |
| Arquétipo indefinido | @archetype-consultant | Definir arquétipo antes de auditar tom e personalidade |
| Validação com dados | @byron-sharp | Sharp para mental/physical availability nas redes |
