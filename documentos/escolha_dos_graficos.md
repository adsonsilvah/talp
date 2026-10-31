# Fundamentação Teórica e Justificativa de Escolha dos Gráficos

**Projeto:** IA no Ensino Superior — Percepções Estudantis e Integridade Acadêmica  
**Base de dados:** Pesquisa de Liverpool 2023 ($n = 2.555$ respondentes; Johnston et al., 2024; DOI: 10.1007/s40979-024-00149-4)  
**Referencial Teórico:** MUNZNER, Tamara. *Visualization Analysis and Design*. CRC Press, 2014; CLEVELAND, William S.; McGILL, Robert. *Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods*, 1984; WARE, Colin. *Information Visualization: Perception for Design*, 2012.

---

## 1. Princípios de Design e Enquadramento Metodológico

A concepção das visualizações deste projeto fundamenta-se no princípio da **correspondência expressiva e eficaz de canais perceptuais** formalizado por Tamara Munzner e nos estudos empíricos clássicos de William Cleveland e Robert McGill. Segundo essa hierarquia, a acuidade com que o cérebro humano decodifica informações quantitativas decresce na seguinte ordem:

$$\text{Posição em escala comum alinhada} > \text{Posição em escala comum não alinhada} > \text{Comprimento} > \text{Ângulo/Arco} > \text{Área 2D} > \text{Luminância/Saturação} > \text{Matiz de Cor}$$

Para cada pergunta do questionário de Liverpool, a escolha do tipo visual considerou três restrições fundamentais:

1. **Adequação estrita à tipologia dos atributos:** 
   - Atributos ordinais (grau de confiança $1\text{–}5$ e escalas de concordância Likert) nunca são convertidos em médias numéricas fictícias, que pressuporiam intervalos constantes e continuidade inexistente.
   - Variáveis multirresposta (ferramentas conhecidas e finalidades de uso), nas quais um mesmo estudante pode assinalar múltiplas alternativas e a soma excede $100\%$, nunca são representadas por gráficos de fechamento de todo (como pizza, rosca ou barras empilhadas a $100\%$), que violariam a matemática de conjuntos não exclusivos.
2. **Preservação de denominadores e transparência amostral:**
   - Todo percentual reportado baseia-se em um denominador explícito informado na legenda ou no tooltip.
   - Categorias como *"Outro"* e *"Prefere não informar"* são mantidas visíveis, evitando que a recusa seja silenciosamente confundida com ausência de uso.
3. **Identidade cromática sóbria e semântica:**
   - Paleta inspirada na identidade acadêmica: branco de fundo, azul-marinho (`#0c3064`) para categorias afirmativas e institucionais, vermelho carmim (`#ed1c24`) para oposição ética e alertas, cinzas neutros (`#cbd5e1` e `#e2e8f0`) para categorias neutras e residuais, e azul intermediário (`#4d79b1`, `#8caed6`) para gradações ordinais e multissegmentos.

---

## 2. Análise Individual dos Gráficos do Dashboard

O dashboard organiza as 13 visualizações em quatro seções analíticas: **Perfil dos Respondentes**, **Conhecimento e Finalidades**, **Integridade Acadêmica** e **Políticas Institucionais**. A seguir, detalha-se a justificativa técnica de cada gráfico.

---

### Seção 1: Perfil dos Respondentes

#### Gráfico 1 — Quem respondeu: faculdades (`profile.faculty`)
- **Pergunta de domínio:** Como os $2.555$ estudantes respondentes estão distribuídos entre as três grandes faculdades da universidade?
- **Abstração de dados:** Atributo categórico nominal (`faculty` com 4 valores) e atributo derivado quantitativo (frequência absoluta $n$ e proporção percentual $\%$ no recorte).
- **Abstração de tarefa (Munzner):** *Summarize* distribuição; *Identify* ranking e proporções de participação.
- **Codificação visual:** **Gráfico de Barras Horizontais** alinhadas na mesma base zero, com ordenação decrescente de frequência.
- **Por que esta escolha?**
  - O canal de comprimento de barra em base alinhada fornece leitura instantânea e sem viés de estimativa.
  - A orientação horizontal acomoda rótulos textuais longos (ex.: *"Humanidades e Ciências Sociais"*, *"Saúde e Ciências da Vida"*) em linha reta, eliminando a rotação de texto a 45° ou 90° que sabidamente atrasa a leitura em cerca de $30\%$ (Ware, 2012).
- **Alternativas descartadas:**
  - *Gráfico de Pizza:* Foi descartado porque a comparação de fatias com tamanhos relativamente próximos ($40,4\%$, $29,7\%$ e $26,6\%$) força o usuário a julgar ângulos e áreas curvas, canal menos preciso que o alinhamento linear.

---

#### Gráfico 2 — Quem respondeu: níveis de estudo (`profile.study_level`)
- **Pergunta de domínio:** Qual é a predominância de alunos de graduação versus pós-graduação e outros níveis na pesquisa?
- **Abstração de dados:** Atributo categórico nominal de partição única (`study_level` com 5 categorias mutuamente exclusivas que somam exatamente $100\%$) e proporção percentual.
- **Abstração de tarefa (Munzner):** *Identify* relação parte-todo (*part-to-whole*) e sintetizar a dominância categórica da amostra.
- **Codificação visual:** **Gráfico de Rosca (*Donut Chart*)** com abertura central de $55\%$, rótulos externos com valor e percentual, e ordenação decrescente de arcos.
- **Por que esta escolha?**
  - Diferente do gráfico de faculdades (onde as grandezas são próximas), aqui há uma dominância esmagadora de uma categoria sobre as demais: a *Graduação* concentra $69,7\%$ da amostra ($1.782$ alunos), seguida por pós-graduação por disciplinas ($22,7\%$), pós-graduação por pesquisa ($6,5\%$), preparatório ($0,7\%$) e não identificado ($0,4\%$).
  - O formato de rosca evidencia a estrutura de fechamento em $100\%$ sem a sensação de "torta maciça", e os arcos transmitem imediatamente a noção intuitiva de que a graduação ocupa mais de dois terços de todo o corpo respondente.
- **Alternativas descartadas:**
  - *Barras simples:* Embora também precisas, manter apenas barras em todos os gráficos do dashboard geraria fadiga visual ("cegueira de formato"). A rosca neste ponto específico funciona porque os dados cumprem rigorosamente os critérios clássicos para gráficos circulares: poucas categorias, escolha única, fechamento estrito em $100\%$ e forte assimetria entre fatias.

---

#### Gráfico 3 — Composição demográfica: faculdade × nível de estudo (`profile.faculty_study_level`)
- **Pergunta de domínio:** Como o perfil de nível de estudo varia entre as diferentes faculdades da universidade?
- **Abstração de dados:** Dois atributos categóricos nominais (`faculty` e `study_level`) e atributos quantitativos derivados ($n$ e $\%$ relativo à faculdade).
- **Abstração de tarefa (Munzner):** *Compare* distribuições entre categorias; *Identify* a composição interna de cada faculdade.
- **Codificação visual:** **Gráfico de Colunas Verticais Agrupadas (*Grouped Column Chart*)**, com Faculdades no eixo horizontal, níveis de estudo diferenciados por matizes da paleta azul-marinho, e valores exatos ($n$) acompanhados de porcentagens no topo de cada coluna (`textposition="outside"`).
- **Por que esta escolha?**
  - Cada faculdade forma um cluster no eixo horizontal, permitindo inspecionar lado a lado suas colunas de graduação ($72,2\%$, $72,2\%$, $65,6\%$, $50,6\%$) e pós-graduação ($20,9\%$, $19,6\%$, $26,8\%$, $38,6\%$).
  - Os rótulos numéricos no topo (`n=746 (72.2%)`, `n=216 (20.9%)`, etc.) garantem que o leitor acesse a **quantidade exata** sem esforço cognitivo e sem depender exclusivamente do hover.
- **Por que o Treemap anterior foi descartado?**
  - O *Treemap* (áreas 2D retangulares aninhadas) gerava retângulos grandes para a graduação e fatias extremamente espremidas para pós-graduação por pesquisa e preparatório. Como resultado, os textos das categorias menores ficavam sobrepostos ou truncados (ex.: *"Pós-graduação... 2%"*).
  - Além disso, a literatura empírica (Cleveland & McGill, 1984) comprova que o julgamento de área retangular tem erro perceptual muito superior ao julgamento de comprimento em escala alinhada. As colunas agrupadas eliminaram qualquer ambiguidade.

---

#### Gráfico 4 — Confiança na escrita acadêmica · 1–5 (`profile.confidence`)
- **Pergunta de domínio:** Como os estudantes autoavaliam sua própria capacidade de escrita acadêmica formal antes do advento das IAs?
- **Abstração de dados:** Atributo ordenado ordinal (`confidence` na escala discreta de $1$ a $5$, onde $1 =$ nada confiante e $5 =$ muito confiante) e frequência quantitativa ($n$ e $\%$).
- **Abstração de tarefa (Munzner):** *Summarize* forma da distribuição ordinal; *Identify* mediana e assimetria.
- **Codificação visual:** **Gráfico de Colunas Verticais Ordinais** alinhadas rigidamente na ordem numérica $1 \to 5$, partindo da base zero.
- **Por que esta escolha?**
  - A disposição espacial esquerda-direita reflete a metáfora cognitiva universal de progressão escalar ($1 \to 5$).
  - A altura das colunas demonstra com clareza a assimetria positiva moderada da amostra: a confiança concentra-se nos níveis $3$ ($37,3\%$) e $4$ ($41,4\%$), enquanto os extremos de insegurança severa (nível 1: $1,7\%$) e autoconfiança plena (nível 5: $10,7\%$) são minoritários.
- **Alternativas descartadas:**
  - *Média numérica ponderada:* Calcular uma "média de confiança $= 3,49$" seria um erro metodológico clássico, pois a escala ordinal não garante que a distância entre 1 e 2 seja equivalente à distância entre 4 e 5.
  - *Curva de densidade contínua (KDE) ou linha:* Sugeriria que existem valores intermediários contínuos (como $3,2$ ou $4,7$), o que é inverídico para respostas inteiras de questionário.

---

### Seção 2: Conhecimento e Finalidades

#### Gráfico 5 — Ferramentas conhecidas (`awareness.awareness`)
- **Pergunta de domínio:** Quais tecnologias assistivas e sistemas de IA eram previamente conhecidos pelos estudantes universitários em março–abril de 2023?
- **Abstração de dados:** Atributo categórico multirresposta (`awareness`, com 8 opções nominais possíveis por respondente) e proporção percentual sobre os $2.555$ estudantes.
- **Abstração de tarefa (Munzner):** *Identify* extremos e ranking de popularidade tecnológica.
- **Codificação visual:** **Gráfico de Barras Horizontais** ordenadas pela frequência, com base comum zero e denominador fixo em $2.555$.
- **Por que esta escolha?**
  - Sendo uma pergunta multirresposta, um mesmo respondente pode conhecer simultaneamente *Grammarly*, *ChatGPT* e *QuillBot*. Consequentemente, a soma das porcentagens ultrapassa $100\%$ ($88,5\% + 68,9\% + 27,1\% + \dots = 208,6\%$).
  - O gráfico de barras alinhadas em base zero é a **única** codificação visual matematicamente válida para esse tipo de dado, pois cada barra representa a frequência marginal independente de um subconjunto.
- **Alternativas descartadas:**
  - *Gráficos circulares ou empilhados a 100%:* Impossíveis para multirresposta, pois assumem partição exclusiva de um total de $100\%$.
  - *Nuvem de palavras:* Fraca acuidade perceptual (área e orientação aleatória de palavras dificultam qualquer comparação quantitativa precisa).

---

#### Gráfico 6 — Finalidades de utilização ou consideração do uso (`awareness.purposes`)
- **Pergunta de domínio:** Para quais propósitos os estudantes já usaram ou consideraram usar tais ferramentas (acadêmico, pessoal, profissional ou nenhum)?
- **Abstração de dados:** Atributo categórico multirresposta (`purposes`) e percentual de adesão no recorte amostral.
- **Abstração de tarefa (Munzner):** *Compare* proporções de finalidade e quantificar o índice de não utilização.
- **Codificação visual:** **Gráfico de Barras Horizontais** com barras individuais para cada categoria, preservando opções de recusa e não uso.
- **Por que esta escolha?**
  - Permite verificar diretamente que a finalidade acadêmica lidera ($51,0\%$), mas que há uma expressiva parcela de estudantes que nunca utilizou nem considerou utilizar as ferramentas ($35,1\%$).
  - A transparência de manter a barra *"Prefere não informar"* ($1,5\%$) e *"Outro"* ($1,7\%$) evita que essas recusas sejam confundidas com uso negativo.
- **Alternativas descartadas:**
  - *Excluir quem não usou:* Omitir a categoria *"Não utilizou nem considerou"* inflacionaria artificialmente os percentuais das outras finalidades, gerando falsa impressão de adesão generalizada.

---

#### Gráfico 7 — Conhecimento da ferramenta × conversão para finalidade acadêmica (`awareness.tools_academic`)
- **Pergunta de domínio:** As ferramentas mais populares em conhecimento geral são também as mais convertidas em uso acadêmico efetivo?
- **Abstração de dados:** Atributo quantitativo no eixo X (% que conhece a ferramenta na amostra), atributo quantitativo no eixo Y (% que selecionou finalidade acadêmica entre os que conhecem a ferramenta), atributo quantitativo no tamanho da bolha ($n$ absoluto de usuários acadêmicos) e rótulo nominal da ferramenta.
- **Abstração de tarefa (Munzner):** *Explore* correlação/associação entre popularidade de marca e vocação acadêmica; *Identify* casos discrepantes (*outliers*).
- **Codificação visual:** **Gráfico de Dispersão de Bolhas (*Bubble Scatter Plot*)**.
- **Por que esta escolha?**
  - Utiliza os canais de posição ortogonal bidimensional (X e Y), considerados os mais precisos da percepção humana, para cruzar duas métricas quantitativas contínuas.
  - Revela uma descoberta analítica crucial que ficaria oculta em barras comuns: enquanto *Grammarly* e *ChatGPT* dominam em volume total (bolhas grandes no quadrante direito), o *QuillBot* apresenta a mais alta taxa de conversão acadêmica proporcional ($65,2\%$ dos estudantes que o conhecem o aplicam aos estudos).

---

#### Gráfico 8 — Repertório: número de ferramentas conhecidas por estudante (`awareness.repertoire`)
- **Pergunta de domínio:** O estudante universitário médio tem um repertório diversificado de ferramentas ou seu conhecimento limita-se a uma ou duas aplicações?
- **Abstração de dados:** Atributo ordenado ordinal discreto derivado (`tool_count` com valores `0`, `1`, `2`, `3`, `4+`) e proporção percentual da amostra.
- **Abstração de tarefa (Munzner):** *Summarize* a forma e a dispersão do repertório individual de ferramentas.
- **Codificação visual:** **Polígono de Frequência / Gráfico de Área Preenchida com Marcadores Pontuais**, com área sombreada suave em azul-marinho (`rgba(12, 48, 100, 0.12)`) até a base zero.
- **Por que esta escolha?**
  - A linha contínua entre pontos ordinais discretos com área preenchida guia o olhar pela forma global da distribuição, destacando visualmente seu pico unimodal centrado em **2 ferramentas** ($39,8\%$).
  - O gráfico quebra o ritmo visual de barras da seção e reforça a percepção de que a ampla maioria dos estudantes conhecia exatamente o binômio *Grammarly + ChatGPT* no início de 2023.

---

#### Gráfico 9 — Confiança na escrita × finalidade acadêmica (`awareness.confidence_academic`)
- **Pergunta de domínio:** Estudantes com menor confiança na própria escrita são os que mais buscam apoio de IA para fins acadêmicos?
- **Abstração de dados:** Atributo ordinal de confiança ($1\text{–}5$, eixo X), atributo categórico binário de seleção acadêmica (Selecionou / Não selecionou, eixo Y) e proporção percentual condicional dentro de cada nível de confiança (matriz $2 \times 5$).
- **Abstração de tarefa (Munzner):** *Compare* taxas condicionais entre subgrupos ordinais; *Discover* padrões de dependência.
- **Codificação visual:** **Mapa de Calor (*Heatmap*) Matricial $2 \times 5$** com escala cromática sequencial de luminância azul (`#ffffff` $\to$ `#0c3064`), rótulos numéricos impressos nas células e normalização estrita por coluna.
- **Por que esta escolha?**
  - A normalização independente por coluna de confiança resolve o problema crítico do tamanho desigual das faixas (já que o nível 4 tem $1.059$ estudantes e o nível 1 tem apenas $43$). Cada coluna soma $100\%$, tornando as taxas diretamente comparáveis.
  - O mapa de calor evidencia que a adesão acadêmica é mais intensa nos níveis intermediários de confiança (nível 2 com $57,5\%$ e nível 3 com $53,9\%$), decrescendo conforme a autoconfiança atinge o topo (nível 5 com $45,8\%$).

---

### Seção 3: Integridade Acadêmica

#### Gráfico 10 — Aceitação: apoio gramatical × redação integral (`academic_integrity.acceptance`)
- **Pergunta de domínio:** Onde os estudantes traçam a fronteira da integridade ética quando outro aluno utiliza IA: na revisão gramatical ou na geração completa do texto?
- **Abstração de dados:** Dois atributos ordinais de 5 níveis de concordância Likert (`grammar_attitude` e `essay_attitude`) acrescidos de categoria independente (`Other`), e percentual sobre o total de $2.555$ respostas.
- **Abstração de tarefa (Munzner):** *Compare* distribuições divergentes e contrastar cenários éticos opostos.
- **Codificação visual:** **Barras Horizontais Empilhadas Divergentes a 100%**, com paleta cromática semântica divergente:
  - Azul escuro (`#0c3064`): Favorável
  - Azul claro (`#8caed6`): Parcialmente favorável
  - Cinza neutro (`#cbd5e1`): Neutro
  - Salmão claro (`#f5a1a5`): Parcialmente contrário
  - Vermelho institucional (`#ed1c24`): Contrário
  - Cinza claro hachurado (`#e2e8f0` com textura `/`): Outro
- **Por que esta escolha?**
  - Coloca os dois cenários exatamente na mesma régua percentual de $0\%$ a $100\%$.
  - O contraste cromático salta aos olhos: no **apoio gramatical**, predomina a massa azul à esquerda ($53,5\%$ de apoio); na **redação integral**, a massa vermelha toma conta da barra ($70,5\%$ de oposição, sendo $48,5\%$ estritamente contrários).
  - A hachura no cinza claro (`#e2e8f0`) resolveu com elegância o problema visual de não confundir *"Outro"* nem com a posição *"Neutra"* nem com o fundo branco da página.

---

#### Gráfico 11 — Matriz de transição ética: apoio gramatical × redação integral (`academic_integrity.attitude_matrix`)
- **Pergunta de domínio:** Como o mesmo indivíduo combina suas opiniões sobre apoio gramatical e redação integral? Existe inconsistência ou coerência ética interna?
- **Abstração de dados:** Cruzamento bidimensional pareado dos atributos `grammar_attitude` (eixo Y) e `essay_attitude` (eixo X), gerando uma tabela de contingência $6 \times 6$ com a proporção sobre o total da amostra em cada interseção.
- **Abstração de tarefa (Munzner):** *Discover* clusters e dependência bivariada pareada (*joint distribution*).
- **Codificação visual:** **Mapa de Calor (*Heatmap*) Matricial $6 \times 6$**, com luminância azul e anotações numéricas na célula.
- **Por que esta escolha?**
  - O Gráfico 10 mostra apenas totais marginais independentes. O Gráfico 11 revela a postura individual: o grupo mais populoso de toda a universidade é composto por estudantes que são **Parcialmente favoráveis ao auxílio gramatical e terminantemente Contrários à redação integral** ($329$ estudantes; $12,9\%$).
  - Esse padrão desmistifica a ideia de que a rejeição à IA seria fruto de aversão generalizada à tecnologia: trata-se de um critério consciente de preservação da autoria intelectual.

---

### Seção 4: Políticas Institucionais

#### Gráfico 12 — Preferências de políticas institucionais (`policies.policies`)
- **Pergunta de domínio:** Qual modelo de governança os estudantes julgam que a universidade deve adotar para essas tecnologias?
- **Abstração de dados:** Atributo categórico nominal de escolha única (`policy`, com 6 opções) e percentual de respondentes.
- **Abstração de tarefa (Munzner):** *Identify* a política majoritária e classificar a adesão aos modelos de regulação.
- **Codificação visual:** **Gráfico de Barras Horizontais** ordenadas decrescentemente por adesão.
- **Por que esta escolha?**
  - Os nomes das alternativas são sentenças institucionais extensas (ex.: *"Have a university wide policy on when they are and or not appropriate to use"*). As barras horizontais permitem acomodar as traduções consolidadas com legibilidade perfeita.
  - A ordenação destaca de imediato que as três abordagens de regulação formal somam **$84,0\%$** da preferência discente (*Política única da universidade*: $41,1\%$; *Políticas por faculdade*: $26,0\%$; *Decisão de cada professor*: $16,9\%$), enquanto extremos como *Liberdade irrestrita de uso* ($9,6\%$) e *Banimento completo* ($4,5\%$) têm apoio marginal.

---

#### Gráfico 13 — Preferência de política × aceitação de uso: apoio gramatical vs. redação integral (`policies.policy_integrity`)
- **Pergunta de domínio:** A preferência de política institucional de um estudante reflete sua tolerância ética em relação à redação integral e ao auxílio gramatical?
- **Abstração de dados:** Atributo categórico nominal de política institucional (eixo Y) e dois atributos quantitativos derivados: taxa de aceitação favorável ao apoio gramatical e taxa de aceitação favorável à redação integral dentro de cada grupo de política.
- **Abstração de tarefa (Munzner):** *Compare* duas medidas quantitativas associadas a uma mesma chave nominal; examinar o contraste ético intergrupos.
- **Codificação visual:** **Gráfico de Barras Agrupadas Horizontais (*Grouped Bar Chart*)** com duas barras sólidas por política:
  - Barra Azul-marinho (`#0c3064`): Apoio gramatical (favoráveis)
  - Barra Vermelha (`#ed1c24`): Redação integral (favoráveis)
- **Por que esta escolha?**
  - Para cada política institucional, o leitor compara instantaneamente duas barras sólidas alinhadas na mesma base zero, com os valores numéricos impressos na extremidade.
  - A leitura é transparente e imediata: em quem defende *Banimento completo*, ambas as barras são residuais ($8,6\%$ e $0,9\%$); nos defensores de *Política única*, o apoio gramatical atinge $49,9\%$ enquanto a redação integral cai para apenas $8,0\%$; e no grupo de *Liberdade de uso*, a aceitação da redação integral salta para expressivos $47,2\%$.
- **Por que o Gráfico de Halteres (*Dumbbell Plot*) foi descartado?**
  - O gráfico de halteres anterior utilizava linhas cinzas finas com pequenos círculos nas pontas e textos soltos no espaço. Em telas reais e em apresentações acadêmicas, essa representação apresentava baixa legibilidade, causava conflito com legendas e exigia esforço cognitivo desnecessário para decifrar qual ponto correspondia a qual cenário.
  - O gráfico de barras agrupadas utiliza a representação mais canônica, direta e robusta da ciência de visualização de dados para comparação bivariada entre grupos categóricos.

---

## 3. Matriz Sintética de Decisões Visuais

| ID | Nome do Gráfico | Tipo de Gráfico | Marca / Canais Primários | Justificativa Teórica Central (Munzner / Cleveland & McGill) |
|---|---|---|---|---|
| **1** | Faculdade | Barras Horizontais | Linha / Comprimento em base alinhada horizontal | Máxima precisão para dados quantitativos e acomodação de rótulos textuais longos sem inclinação. |
| **2** | Nível de estudo | Rosca (*Donut*) | Área radial / Ângulo e arco fechado a 100% | Relação parte-todo de escolha única com assimetria extrema (graduação com quase $70\%$). |
| **3** | Composição demográfica | Colunas Verticais Agrupadas | Linha / Posição vertical em escala comum + Matiz | Elimina caixas sobrepostas de treemaps; expõe os números exatos ($n$) e proporções no topo de cada coluna. |
| **4** | Confiança na escrita | Colunas Verticais Ordinais | Linha / Posição vertical + Ordem horizontal fixa $1 \to 5$ | Preserva a natureza ordinal discreta sem forçar médias numéricas ou interpolações contínuas. |
| **5** | Ferramentas conhecidas | Barras Horizontais | Linha / Comprimento em base zero comum | Única codificação matematicamente válida para multirresposta (a soma ultrapassa $100\%$). |
| **6** | Finalidades de uso | Barras Horizontais | Linha / Comprimento em base zero comum | Preserva alternativas não exclusivas, recusas e não uso sem distorcer o denominador. |
| **7** | Conhecimento × Conversão | Dispersão de Bolhas | Ponto / Posição planar 2D (X e Y) + Área da bolha | Cruza popularidade geral de marca com vocação acadêmica, evidenciando ferramentas de nicho (*QuillBot*). |
| **8** | Repertório de ferramentas | Polígono de Frequência / Área | Linha e Ponto / Posição vertical + Área sombreada | Destaca a forma unimodal e a concentração da amostra em exatamente 2 ferramentas. |
| **9** | Confiança × Finalidade | Mapa de Calor $2 \times 5$ | Área matricial / Posição 2D + Luminância sequencial | Normalização condicional por coluna de confiança contorna o desequilíbrio amostral entre os níveis ordinais. |
| **10** | Aceitação de uso | Barras Divergentes 100% | Linha / Comprimento empilhado + Matiz divergente | Coloca apoio gramatical e redação integral na mesma base, contrastando aprovação azul e rejeição vermelha. |
| **11** | Matriz de transição ética | Mapa de Calor $6 \times 6$ | Área matricial / Posição 2D + Luminância sequencial | Revela o comportamento no nível do indivíduo (forte contingência pró-gramática e anti-plágio). |
| **12** | Políticas institucionais | Barras Horizontais | Linha / Comprimento em base alinhada ordenada | Acomoda textos longos de governança e evidencia a preferência de $84\%$ por regulação equilibrada. |
| **13** | Política × Aceitação de uso | Barras Agrupadas Horizontais | Linha / Comprimento em base alinhada + Matiz contrastante | Substitui o dumbbell plot por barras sólidas azul vs. vermelho, tornando imediata a leitura dos percentuais exatos. |
