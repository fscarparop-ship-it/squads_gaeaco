---
task: brandingStrategyGuide()
responsavel: "@marty-neumeier"
responsavel_type: Agent
atomic_layer: Task
elicit: true

Entrada:
  - campo: brand
    tipo: string
    origem: User Input
    obrigatorio: true
  - campo: audience
    tipo: string
    origem: User Input
    obrigatorio: true
  - campo: channels
    tipo: list
    origem: User Input
    obrigatorio: true

Saida:
  - campo: Branding Strategy Guide
    tipo: string
    destino: Console
    persistido: false
  # Named outputs consumed by other squads.
  # Contract: brand-squad/data/cross-squad-handoffs.yaml
  - campo: onlyness_statement
    tipo: string
    destino: "copy-squad, storytelling, traffic-masters"
    persistido: false
  - campo: visual_guidelines
    tipo: object
    destino: "design-squad (create-design-system)"
    persistido: false
  - campo: channel_application
    tipo: object
    destino: "traffic-masters (create-ad-strategy), copy-squad (write-ad-copy)"
    persistido: false
  - campo: commitment_matrix
    tipo: object
    destino: "storytelling (wf-brand-narrative)"
    persistido: false
  - campo: five_disciplines
    tipo: object
    destino: Console
    persistido: false

Checklist:
  - "[ ] Onlyness Statement definido e validado"
  - "[ ] 5 Disciplinas aplicadas ao contexto da marca"
  - "[ ] Diretrizes visuais estratégicas com justificativas"
  - "[ ] Guia de aplicação por canal (feed, stories, identidade)"
---

# Task: Branding Strategy Guide

**Task ID:** BRAND-010
**Version:** 1.0.0
**Command:** `*branding-strategy-guide`
**Agent:** Marty Neumeier (marty-neumeier)
**Purpose:** Criar um guia completo de estratégia de branding que conecta posicionamento radical, identidade visual e execução em canais — bridging the Brand Gap entre estratégia e design.

---

## Filosofia Central

> "Uma marca não é o que você diz que é. É o que ELES dizem que é."
> — Marty Neumeier

Este guia aplica os frameworks de Neumeier — The Brand Gap, Zag, The Brand Flip — para criar uma estratégia de marca onde **design e estratégia não são separados: o design É a estratégia.** Cada post, cor, fonte e tom de voz reforça a mesma percepção.

---

## Inputs

| Campo | Tipo | Origem | Obrigatório | Validação |
|-------|------|--------|-------------|-----------|
| brand | string | User prompt | Sim | Nome da marca e descrição atual |
| audience | string | User prompt | Sim | Público-alvo com perfil psicográfico |
| channels | list | User prompt | Sim | Canais onde a marca aparece (feed, stories, logo, site, etc.) |
| competitors | list | User prompt | Não | Concorrentes e como se posicionam |
| current_perception | string | User prompt | Não | Percepção atual do público sobre a marca |
| desired_perception | string | User prompt | Não | Percepção desejada na mente do público |
| brand_values | list | User prompt | Não | Valores fundamentais da marca |

---

## Precondições

- Público-alvo identificado com contexto emocional e aspiracional
- Pelo menos 1 canal definido para aplicação
- Disposição para diferenciação radical (não apenas incremental)

---

## Perguntas Diagnósticas

Antes de executar, Neumeier sempre faz 4 perguntas:

1. **Qual é a percepção que você quer criar na cabeça do público?**
   - Não o que você quer dizer — o que você quer que ELES sintam
   - Uma marca é um sentimento visceral (gut feeling)

2. **Quem é o público e o que eles já sentem sobre marcas parecidas?**
   - Mapeie as percepções existentes
   - Identifique fadiga, ceticismo e espaços emocionais vazios

3. **O que torna essa marca a ÚNICA no seu espaço?**
   - Se não consegue usar a palavra "única", não tem um Zag
   - Aplique o Onlyness Test imediatamente

4. **Onde vai aparecer?**
   - Feed, stories, identidade visual, logo, site, embalagem
   - Cada touchpoint reforça ou destrói a percepção

---

## Fases de Execução

### Fase 1: Onlyness Statement — A Base de Tudo

O Onlyness Statement é o filtro decisório para TODAS as decisões da marca.

1. Construa o statement usando a fórmula:

   ```
   Nossa [marca] é a única [categoria] que [benefício único] para [público específico]
   ```

2. Expanda para as 6 dimensões:
   - **O QUÊ:** O que a marca oferece
   - **COMO:** Como entrega de forma única
   - **QUEM:** Para quem especificamente
   - **ONDE:** Em que contexto/mercado
   - **POR QUÊ:** Propósito além do lucro
   - **QUANDO:** Em que momento da vida do público

3. Valide com o teste:
   - É verdadeiro? A marca entrega isso?
   - É relevante? O público se importa?
   - É único? Nenhum concorrente pode dizer o mesmo?
   - É verificável? Há evidências?

4. Se falhar no teste: **volte ao início**. Não adianta construir identidade sobre fundações genéricas.

### Fase 2: As 5 Disciplinas Aplicadas

Aplique cada disciplina ao contexto específico da marca:

#### Disciplina 1: Diferenciação
- Responda: Quem é você? O que você faz? Por que importa?
- Mapeie o "category ladder" — como o público organiza mentalmente as opções
- Identifique onde ZAG: quando todos fazem X, faça o oposto
- O sucesso depende de senso de pertencimento, não de features

#### Disciplina 2: Colaboração
- Defina o modelo de equipe criativa:
  - One-stop shop (tudo interno)
  - Brand agency (parceiro externo)
  - Integrated marketing team (híbrido)
- "É preciso uma vila para construir uma marca"
- Identifique os colaboradores necessários por canal

#### Disciplina 3: Inovação
- Aplique o princípio MAYA — Most Advanced Yet Acceptable
- O design mais inovador rejeita conscientemente a opção padrão
- Para cada canal, pergunte: o que seria radical mas ainda aceitável?
- Mapeie o espectro: convencional ←→ radical. Posicione no ponto MAYA.

#### Disciplina 4: Validação
- Aplique os 4 testes de validação a cada elemento da marca:
  - **Swap Test:** Troque o logo por um concorrente. Alguém nota?
  - **Hand Test:** Cubra o logo. O conteúdo é reconhecível?
  - **Concept Test:** Teste o conceito com o público antes de lançar
  - **Field Test:** Teste no ambiente real (feed, stories, ponto de venda)
- Se falhar no Swap Test ou Hand Test: a identidade é genérica demais

#### Disciplina 5: Cultivo
- Marcas exigem comportamento humano consistente alinhado aos valores
- Defina as "regras tribais" — como a marca se comporta sempre
- Crie o guia de cultivo: o que fazer e o que NUNCA fazer
- Uma marca carismática é aquela para a qual as pessoas acreditam que não há substituto

### Fase 3: Diretrizes Visuais Estratégicas

Cada decisão visual é uma decisão estratégica. Neumeier dá diretrizes visuais estratégicas, não apenas estéticas. Explique o PORQUÊ de cada escolha criativa.

#### Cores
| Decisão | Critério Estratégico |
|---------|---------------------|
| Cor primária | Que emoção precisa dominar a percepção? |
| Cores secundárias | Que nuances da personalidade precisam aparecer? |
| Cores proibidas | Que associações a marca precisa EVITAR? |

- Justifique cada cor pela percepção que cria, não pela estética
- Teste: se um concorrente usasse essas cores, haveria confusão?

#### Tipografia
| Decisão | Critério Estratégico |
|---------|---------------------|
| Fonte primária | Que personalidade a forma das letras comunica? |
| Fonte de apoio | Que equilíbrio cria com a primária? |
| Hierarquia | Como guia o olho para a mensagem mais importante? |

- Uma marca Sage (sabedoria) pede serifas clássicas; uma Outlaw (rebeldia) pede sans-serif agressiva
- O peso (bold, light) comunica autoridade vs. delicadeza

#### Estilo Visual
- Fotografia: mood, iluminação, enquadramento, presença humana
- Composição: grid, espaço negativo, densidade informacional
- Iconografia: minimalista vs. detalhado, geométrico vs. orgânico
- Cada decisão deve passar pelo filtro: "isso reforça o Onlyness Statement?"

### Fase 4: Aplicação por Canal

Para cada canal identificado, crie diretrizes específicas:

#### Feed (Instagram, LinkedIn, etc.)
- Grid visual: padrão de cores, ritmo de conteúdo
- Tipografia em posts: hierarquia de leitura
- Fórmula de post que reforça o posicionamento
- O que NUNCA postar (proteção da percepção)

#### Stories
- Estilo de capas de destaques
- Paleta de elementos interativos
- Tom de voz em tempo real (mais casual vs. curado)
- Como manter reconhecibilidade em formato efêmero

#### Identidade Visual / Logo
- Conceito do logo e o que ele comunica
- Variações (primário, secundário, ícone, monocromático)
- Regras de espaçamento e tamanho mínimo
- Aplicação em dark mode e fundos variados

#### Outros Touchpoints
- Site: como a identidade se traduz em experiência digital
- Embalagem: hierarquia visual e primeiro impacto
- Materiais impressos: adaptação do sistema para print
- Vídeo: motion identity, transições, lower thirds

### Fase 5: Brand Commitment Matrix

Aplique o framework do The Brand Flip:

#### Lado do Cliente (I.A.M.)
| Dimensão | Pergunta |
|----------|----------|
| **Identity** (Identidade) | Quem são e quem aspiram ser? |
| **Aims** (Objetivos) | Que "jobs" estão tentando realizar? |
| **Mores** (Valores tribais) | O que acreditam ser certo/errado? |

#### Lado da Marca (P.O.V.)
| Dimensão | Pergunta |
|----------|----------|
| **Purpose** (Propósito) | Por que existimos além de lucrar? |
| **Onlyness** (Unicidade) | Nosso ___ é o único ___ que ___ |
| **Values** (Valores) | Crenças que guiam cultura e comportamento |

#### Alinhamento
- Purpose ↔ Identity
- Onlyness ↔ Aims
- Values ↔ Mores

Se não houver alinhamento: a marca não será uma tribo. E "pessoas não compram marcas — elas SE JUNTAM a marcas."

---

## Formato de Output

```markdown
## Guia de Estratégia de Branding: {Nome da Marca}

**Metodologia:** Marty Neumeier — The Brand Gap + Zag + The Brand Flip
**Data:** {data}

---

### 1. Diagnóstico

**Percepção atual:** {o que o público sente hoje}
**Percepção desejada:** {o que a marca quer que sintam}
**Gap identificado:** {distância entre atual e desejado}

### 2. Onlyness Statement

> Nossa {marca} é a única {categoria} que {benefício único} para {público específico}

**Dimensões expandidas:**
| Dimensão | Definição |
|----------|-----------|
| O QUÊ | {offering} |
| COMO | {método único} |
| QUEM | {público específico} |
| ONDE | {contexto/mercado} |
| POR QUÊ | {propósito} |
| QUANDO | {momento} |

**Validação:**
- [x/] Verdadeiro | [x/] Relevante | [x/] Único | [x/] Verificável

### 3. As 5 Disciplinas — Aplicação

#### Diferenciação
- **Quem somos:** {identidade}
- **O que fazemos:** {oferta}
- **Por que importa:** {relevância}
- **Nosso ZAG:** {quando todos fazem X, nós fazemos Y}

#### Colaboração
- **Modelo:** {one-stop / agency / hybrid}
- **Equipe necessária:** {papéis}

#### Inovação
- **Princípio MAYA aplicado:** {o mais avançado mas aceitável}
- **Rejeição do padrão:** {o que estamos fazendo diferente}

#### Validação
| Teste | Resultado | Ação |
|-------|-----------|------|
| Swap Test | {pass/fail} | {ajuste} |
| Hand Test | {pass/fail} | {ajuste} |
| Concept Test | {feedback} | {ajuste} |
| Field Test | {resultado} | {ajuste} |

#### Cultivo
- **Regras tribais:** {comportamentos obrigatórios}
- **Nunca fazer:** {comportamentos proibidos}

### 4. Diretrizes Visuais Estratégicas

#### Paleta de Cores
| Papel | Cor | Hex | Justificativa Estratégica |
|-------|-----|-----|--------------------------|
| Primária | {cor} | #{hex} | {por que essa emoção} |
| Secundária | {cor} | #{hex} | {por que esse complemento} |
| Proibida | {cor} | — | {por que evitar} |

#### Tipografia
| Papel | Fonte | Peso | Justificativa Estratégica |
|-------|-------|------|--------------------------|
| Primária | {fonte} | {peso} | {personalidade} |
| Apoio | {fonte} | {peso} | {equilíbrio} |

#### Estilo Visual
- **Fotografia:** {mood, iluminação, enquadramento}
- **Composição:** {grid, espaço negativo}
- **Iconografia:** {estilo}

### 5. Aplicação por Canal

#### Feed
- **Grid visual:** {padrão}
- **Fórmula de post:** {estrutura}
- **Tom:** {voz no feed}
- **Nunca postar:** {proibições}

#### Stories
- **Estilo de destaques:** {direção}
- **Elementos interativos:** {paleta}
- **Tom em tempo real:** {voz nos stories}

#### Identidade Visual / Logo
- **Conceito:** {o que comunica}
- **Variações:** {lista}
- **Regras:** {espaçamento, tamanho mínimo}

### 6. Brand Commitment Matrix

| Cliente (I.A.M.) | ↔ | Marca (P.O.V.) |
|-------------------|---|-----------------|
| Identity: {quem são} | ↔ | Purpose: {por que existimos} |
| Aims: {o que buscam} | ↔ | Onlyness: {nossa unicidade} |
| Mores: {o que valorizam} | ↔ | Values: {nossos valores} |

**Alinhamento:** {análise de fit entre cliente e marca}

### 7. Escala de Compromisso

| Nível | Status | Próximo Passo |
|-------|--------|---------------|
| Satisfação | {análise} | {como avançar} |
| Encantamento | {análise} | {como avançar} |
| Engajamento tribal | {análise} | {como avançar} |

### 8. Plano de Cultivo

**Cadência de revisão:** {frequência}
**Métricas de percepção:** {como medir}
**Riscos à marca:** {ameaças identificadas}
```

---

## Condições de Veto

- NUNCA separe estratégia de design — o Brand Gap é o inimigo
- NUNCA escolha cores, fontes ou elementos visuais sem justificativa estratégica
- NUNCA crie identidade sobre um Onlyness Statement genérico — volte e refine primeiro
- NUNCA ignore os testes de validação — uma marca que não passa no Swap Test é genérica
- NUNCA trate canais de forma isolada — cada touchpoint reforça ou destrói a mesma percepção
- NUNCA posicione sem entender o que o público JÁ sente sobre marcas parecidas
- NUNCA confunda estética com estratégia — bonito sem significado é decoração, não branding

---

## Critérios de Conclusão

- [ ] Diagnóstico de percepção atual vs. desejada realizado
- [ ] Onlyness Statement construído e validado nos 4 critérios
- [ ] 5 Disciplinas aplicadas ao contexto específico da marca
- [ ] Diretrizes visuais definidas com justificativas estratégicas (não apenas estéticas)
- [ ] Testes de validação executados (Swap, Hand, Concept, Field)
- [ ] Aplicação por canal documentada com fórmulas e proibições
- [ ] Brand Commitment Matrix preenchida com análise de alinhamento
- [ ] Escala de compromisso mapeada com próximos passos
- [ ] Plano de cultivo com cadência de revisão definida

---

## Relacionamentos com Outros Agentes

| Situação | Agente Complementar | Contexto |
|----------|---------------------|----------|
| Posicionamento de categoria | @al-ries | Ries para positioning puro, Neumeier para onlyness radical |
| Identidade visual detalhada | @alina-wheeler | Wheeler para o processo de design de identidade completo |
| Prova de evidência | @byron-sharp | Sharp para validar com dados de mental/physical availability |
| Arquétipo de marca | @archetype-consultant | Definir o arquétipo antes de aplicar as diretrizes visuais |
| Messaging e StoryBrand | @donald-miller | Miller para a narrativa, Neumeier para a identidade |
| Startup / DTC | @emily-heyward | Heyward para execução em startups, Neumeier para estratégia |
| Equity e valor | @david-aaker | Aaker para medir e gerenciar o valor da marca no tempo |
