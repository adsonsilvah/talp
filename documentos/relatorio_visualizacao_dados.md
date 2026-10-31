# Título
IA no Ensino Superior — Percepções Estudantis e Integridade Acadêmica

# Autor/equipe
Adson Silva

# 1. Caracterização do domínio
O avanço das tecnologias assistivas de escrita e de inteligência artificial generativa (como ChatGPT, Grammarly e QuillBot) no ensino superior introduziu desafios imediatos para estudantes, docentes e gestores universitários: compreender quais ferramentas já são conhecidas pelo corpo discente, para quais finalidades estão sendo utilizadas ou cogitadas, onde os próprios estudantes traçam a fronteira ética entre auxílio legítimo (como revisão gramatical) e fraude acadêmica (como redação integral de trabalhos por IA), e que tipo de regulação institucional é esperado.

A visualização desenvolvida resolve o problema de exploração descritiva e comparação multidimensional dessas percepções estudantis sem distorcer escalas ordinais, denominadores ou respostas de múltipla escolha. Os dados utilizados provêm do levantamento empírico realizado na *University of Liverpool* (Reino Unido) entre março e abril de 2023, com $n = 2.555$ estudantes respondentes voluntários, publicado por Johnston et al. (2024) no periódico *International Journal for Educational Integrity* ([DOI: 10.1007/s40979-024-00149-4](https://doi.org/10.1007/s40979-024-00149-4)) e depositado sob licença CC BY 4.0 no catálogo oficial da instituição ([DOI: 10.17638/datacat.liverpool.ac.uk/2297](https://doi.org/10.17638/datacat.liverpool.ac.uk/2297)). Por privacidade e rigor metodológico, o artefato processado (`data/processed/liverpool2023.json`) retém exclusivamente as variáveis fechadas validadas, descartando campos de texto livre e registro bruto de consentimento.

# 2. Abstração de Dados
Tipo de dataset: Tabela (*Flat Table* multidimensional com 2.555 itens/linhas representando estudantes respondentes e atributos originais fechados e derivados).

Table 1. Abstração de Dados
| Nome do atributo | Descrição do atributo | Tipo Abstrato | Domínio |
|---|---|---|---|
| `faculty` | Faculdade à qual o estudante pertence na universidade | Categórico (nominal) | `Humanities and Social Sciences`, `Health and Life Sciences`, `Science and Engineering`, `Not sure` |
| `study_level` | Nível de estudo atual do respondente | Categórico (nominal) | `Undergraduate`, `Postgraduate - Taught`, `Postgraduate - Research`, `Foundation`, `Not sure` |
| `confidence` | Grau de confiança autodeclarado na escrita acadêmica | Ordenado (ordinal) | $\{1, 2, 3, 4, 5\}$ ($1 =$ nada confiante; $5 =$ muito confiante) |
| `awareness` | Tecnologias assistivas/IA conhecidas previamente pelo estudante (multirresposta) | Categórico (conjunto de itens nominais) | Subconjuntos não vazios de `{Grammarly, Chat GPT, QuillBot, DALI-E, ChatSonic, Jasper Chat, None of the above, Other}` |
| `purposes` | Finalidades para as quais utilizou ou considerou utilizar as tecnologias (multirresposta) | Categórico (conjunto de itens nominais) | Subconjuntos não vazios de `{Academic, Personal, Professional, I have not used or considered using them, Prefer not to say, Other}` |
| `grammar_attitude` | Posição sobre o uso de tecnologia por outro estudante para auxílio gramatical em trabalho acadêmico | Ordenado (ordinal de 5 níveis) + categoria separada (`Other`) | `Supportive`, `Somewhat supportive`, `Neutral`, `Somewhat unsupportive`, `Unsupportive`, `Other` |
| `essay_attitude` | Posição sobre o uso de tecnologia por outro estudante para redigir integralmente um ensaio/trabalho | Ordenado (ordinal de 5 níveis) + categoria separada (`Other`) | `Supportive`, `Somewhat supportive`, `Neutral`, `Somewhat unsupportive`, `Unsupportive`, `Other` |
| `policy` | Preferência sobre como a universidade deve regulamentar o uso dessas tecnologias | Categórico (nominal) | `Have a university wide policy...`, `Let departments/faculties decide...`, `Let lecturers decide individual policies...`, `Allow them to be used however the students wish`, `Ban them entirely`, `Other` |
| `tool_count` | Quantidade de ferramentas conhecidas por estudante (atributo derivado a partir da cardinalidade de `awareness`, excluindo `None of the above`) | Ordenado (ordinal discreto) | `{"0", "1", "2", "3", "4+"}` |
| `count` / `percent` | Frequência absoluta e proporção percentual no recorte ou subgrupo (atributos derivados de agregação com denominador explícito) | Ordenado quantitativo (sequencial) | Contagem: $[0, 2555]$; Percentual: $[0\%, 100\%]$ |

# 3. Abstração de Tarefas
A abstração de tarefas segue a **taxonomia multinível de ações e alvos de Munzner (2014)** (*Visualization Analysis and Design*, Cap. 3 — *Why: Task Abstraction*, articulando ações de análise *Discover / Present*, busca *Lookup / Locate / Browse / Explore* e consulta *Identify / Compare / Summarize* sobre alvos de distribuições, extremos, proporções e correlações/dependências).

Table 2. Abstração de Tarefas
| Tarefa de domínio | Tarefa abstrata |
|---|---|
| **T1.** Identificar a composição demográfica da amostra de estudantes por faculdade e por nível de estudo, isolada e conjuntamente. | *Summarize* distribution; *Identify* proportions / part-to-whole relationships and hierarchical subdivisions across categorical attributes (`faculty`, `study_level`). |
| **T2.** Analisar a distribuição do nível de confiança na escrita acadêmica (1 a 5) e compará-la entre faixas ordinais da amostra. | *Summarize* ordinal distribution; *Identify* mode, dispersion and skewness across the discrete scale (`confidence`). |
| **T3.** Identificar quais ferramentas de IA são mais conhecidas e quantas ferramentas compõem o repertório típico do estudante. | *Identify* extremes (ranking of frequency) and *Summarize* discrete distribution of set cardinality (`awareness`, `tool_count`). |
| **T4.** Comparar as finalidades de uso ou consideração de uso (acadêmica, pessoal, profissional, não uso e recusa) na amostra discente. | *Compare* values across non-exclusive categorical items, preserving non-use and refusal categories (`purposes`). |
| **T5.** Explorar a relação entre o conhecimento de cada ferramenta e a conversão para finalidade acadêmica, bem como a associação entre confiança na escrita e seleção da finalidade acadêmica. | *Explore* / *Compare* correlation and joint distribution between two attributes (`awareness` × `purposes` and `confidence` × `purposes`). |
| **T6.** Comparar o contraste ético entre o apoio gramatical e a redação integral por IA, tanto nas distribuições marginais quanto na transição de opinião do mesmo indivíduo. | *Compare* diverging ordinal distributions and *Discover* joint dependency / cluster patterns in a 2D contingency matrix (`grammar_attitude` × `essay_attitude`). |
| **T7.** Identificar as políticas institucionais preferidas pelos estudantes e comparar como a aceitação do uso gramatical versus redação integral varia conforme a política defendida. | *Identify* ranking of categorical preferences and *Compare* paired quantitative values (gaps/spans) across categories (`policy` × `grammar_attitude`, `essay_attitude`). |

# 4. Codificação Visual

## 4.1. Mapeamento tarefas x codificação

Tabela 3. Lista de codificações visuais
| ID | Tarefa(s) associada (id) | Codificação visual | Atributos utilizados e Justificativa |
|---|---|---|---|
| **1** | T1 | Gráfico de Barras Horizontais (`profile.faculty`) | **Atributos:** `faculty` (categórico) e `percent`/`count` (quantitativo). **Justificativa (Munzner, 2014):** Marcas de linha com canal de posição horizontal em escala comum (canal de maior eficácia perceptual para dados quantitativos) e posição vertical ordenada por frequência, permitindo leitura imediata de rótulos longos sem inclinação de texto. |
| **2** | T1 | Gráfico de Rosca / *Donut Chart* (`profile.study_level`) | **Atributos:** `study_level` (categórico de escolha única) e `percent`/`count` (quantitativo). **Justificativa:** Marca de área radial (ângulo/arco + matiz categórico) adequada quando as categorias são mutuamente exclusivas, poucas (5 categorias) e somam exatamente 100%, evidenciando a relação parte-todo (predominância da Graduação). |
| **3** | T1 | Gráfico de Colunas Verticais Agrupadas (`profile.faculty_study_level`) | **Atributos:** `faculty` (eixo horizontal X), `study_level` (matiz categórico em subcolunas), frequência absoluta ($n$) e proporção percentual ($\%$ relativo a cada faculdade) no eixo vertical Y. **Justificativa (Munzner, 2014):** Marcas de barra com canal de posição espacial vertical em escala comum a partir de base zero para comparar a distribuição de níveis de estudo entre as faculdades. Substitui a representação em treemap (área 2D) que causava sobreposição de rótulos e esmagamento perceptual de categorias minoritárias. Com as colunas verticais agrupadas e os valores impressos no topo de cada barra (`n = ... (%...)`), o leitor tem acesso imediato à quantidade exata de respondentes sem ambiguidade. |
| **4** | T2 | Gráfico de Colunas Verticais Ordinais (`profile.confidence`) | **Atributos:** `confidence` (ordinal $1\text{–}5$) e `percent`/`count` (quantitativo). **Justificativa:** Preserva a ordem intrínseca do atributo ordinal no eixo espacial horizontal discreto ($1 \to 5$) e codifica a frequência na altura vertical a partir de base zero, evitando calcular médias numéricas indevidas em escala ordinal ou usar curvas contínuas. |
| **5** | T3 | Gráfico de Barras Horizontais (`awareness.awareness`) | **Atributos:** `awareness` (categórico multirresposta) e `percent`/`count` (quantitativo). **Justificativa:** Como o atributo admite múltiplas seleções por respondente (a soma ultrapassa 100%), gráficos de parte-todo (pizza/empilhados a 100%) seriam incorretos. Barras horizontais alinhadas na mesma base zero permitem comparar a popularidade de cada ferramenta com máxima precisão. |
| **6** | T4 | Gráfico de Barras Horizontais (`awareness.purposes`) | **Atributos:** `purposes` (categórico multirresposta) e `percent`/`count` (quantitativo). **Justificativa:** Codifica cada finalidade (incluindo não utilização e recusa) por comprimento horizontal em escala comum, preservando a natureza não exclusiva das respostas e mantendo a transparência amostral. |
| **7** | T5 | Gráfico de Dispersão de Bolhas / *Bubble Scatter Plot* (`awareness.tools_academic`) | **Atributos:** `% que conhece a ferramenta` (quantitativo, eixo X), `% com finalidade acadêmica dentre os que conhecem` (quantitativo, eixo Y), `acad_n` (quantitativo, tamanho da marca) e `awareness` (categórico, rótulo). **Justificativa:** Utiliza os dois canais mais eficazes (posição planar X e Y) combinados ao canal de área (tamanho do círculo) para cruzar alcance geral da ferramenta com sua taxa de conversão para uso acadêmico. |
| **8** | T3 | Polígono de Frequência / Gráfico de Área com Marcadores (`awareness.repertoire`) | **Atributos:** `tool_count` (ordinal discreto `0` a `4+`) e `percent`/`count` (quantitativo). **Justificativa:** Marcas de ponto conectadas por linhas e área preenchida até a base zero destacam a forma unimodal e a concentração central da distribuição discreta do tamanho do repertório de ferramentas por estudante. |
| **9** | T5 | Mapa de Calor / *Heatmap* $2 \times 5$ (`awareness.confidence_academic`) | **Atributos:** `confidence` (ordinal $1\text{–}5$, eixo X), seleção da finalidade `Academic` (categórico binário, eixo Y) e proporção condicional por coluna (quantitativo). **Justificativa:** Alinhamento matricial 2D com canal de luminância sequencial azul (`#ffffff` $\to$ `#0c3064`) normalizado por coluna de confiança, permitindo inspecionar a distribuição condicional sem viés do tamanho desigual das faixas de confiança. |
| **10** | T6 | Gráfico de Barras Empilhadas Divergentes a 100% (`academic_integrity.acceptance`) | **Atributos:** `grammar_attitude` e `essay_attitude` (ordinais de 5 níveis + `Other`) e `percent` (quantitativo). **Justificativa:** Empilhamento a 100% com escala cromática divergente (azul escuro/claro para favorável, cinza neutro `#cbd5e1` no centro, vermelho claro/escuro para contrário) e textura hachurada (`/`) em cinza claro (`#e2e8f0`) para separar semanticamente a categoria não-ordinal `Outro`. |
| **11** | T6 | Mapa de Calor / *Heatmap* $6 \times 6$ (`academic_integrity.attitude_matrix`) | **Atributos:** `grammar_attitude` (eixo Y), `essay_attitude` (eixo X) e `percent`/`count` conjunto no total da amostra (luminância + texto). **Justificativa:** Enquanto o gráfico 10 compara distribuições marginais separadas, a matriz $6 \times 6$ codifica a distribuição conjunta pareada por indivíduo, revelando em quais células a massa de respondentes se concentra. |
| **12** | T7 | Gráfico de Barras Horizontais (`policies.policies`) | **Atributos:** `policy` (categórico nominal) e `percent`/`count` (quantitativo). **Justificativa:** Posição horizontal em base comum ordenada de forma decrescente pela frequência observada, facilitando a identificação imediata da política institucional preferida pela maioria relativa. |
| **13** | T7 | Gráfico de Barras Agrupadas Horizontais (`policies.policy_integrity`) | **Atributos:** `policy` (eixo Y), `% favorável ao apoio gramatical` (barra azul `#0c3064`), `% favorável à redação integral` (barra vermelha `#ed1c24`) e `percent`/`count` (quantitativo). **Justificativa (Munzner, 2014):** Marcas de barra alinhadas em base comum zero para comparar diretamente duas métricas quantitativas associadas a uma mesma categoria nominal. Substitui o gráfico de halteres (*dumbbell plot*) que causava fricção cognitiva, pontos dispersos e textos flutuantes difíceis de inspecionar. O contraste cromático (azul vs. vermelho) torna imediata a percepção da divergência de aceitação entre os dois cenários. |

## 4.2. Gráficos produzidos

### ID 1 — Faculdade (`profile_faculty`)
![ID 1 — Faculdade (`profile_faculty`)](../exports/profile_faculty.png)
- **Insights e informações extraídas:** A amostra ($n = 2.555$) tem maior participação de estudantes de *Humanidades e Ciências Sociais* ($1.033$; $40,4\%$), seguida por *Saúde e Ciências da Vida* ($759$; $29,7\%$) e *Ciências e Engenharia* ($680$; $26,6\%$). Apenas $83$ respondentes ($3,2\%$) não souberam identificar sua faculdade. Há representação substancial das três grandes áreas acadêmicas da universidade, porém com predominância da área de Humanidades, o que deve ser considerado na leitura dos resultados globais.

### ID 2 — Nível de estudo (`profile_level`)
![ID 2 — Nível de estudo (`profile_level`)](../exports/profile_level.png)
- **Insights e informações extraídas:** Quase sete em cada dez respondentes são estudantes de *Graduação* ($1.782$; $69,7\%$), seguidos pela *Pós-graduação (disciplinas / Taught)* com $579$ ($22,7\%$) e *Pós-graduação (pesquisa / Research)* com $167$ ($6,5\%$). Estudantes de *Preparatório (Foundation)* ($17$; $0,7\%$) e *Não identificado* ($10$; $0,4\%$) somam menos de $30$ indivíduos cada, configurando grupos residuais.

### ID 3 — Composição demográfica: faculdade × nível de estudo (`profile_cross`)
![ID 3 — Composição demográfica: faculdade × nível de estudo (`profile_cross`)](../exports/profile_cross.png)
- **Insights e informações extraídas:** O gráfico de colunas agrupadas evidencia a distribuição dos níveis de estudo dentro de cada faculdade com clareza numérica direta (exibindo a contagem absoluta $n$ e o percentual no topo de cada coluna):
- A *Graduação* é predominante e uniforme em *Humanidades e Ciências Sociais* ($n = 746$; $72,2\%$) e *Saúde e Ciências da Vida* ($n = 548$; $72,2\%$), registrando menor proporção em *Ciências e Engenharia* ($n = 446$; $65,6\%$).
- Em contrapartida, a *Pós-graduação (disciplinas)* atinge sua maior concentração relativa em *Ciências e Engenharia* ($n = 182$; $26,8\%$), comparada a $20,9\%$ em *Humanidades* ($n = 216$) e $19,6\%$ em *Saúde* ($n = 149$).
- A *Pós-graduação (pesquisa)* mantém-se equilibrada entre $6\%$ e $7\%$ nas três áreas ($n = 68$ em Humanidades, $n = 51$ em Saúde e $n = 48$ em Engenharia).
- Categorias reduzidas como *Preparatório* ($n = 3$ a $11$) e *Não identificado* ($n = 0$ a $4$) são identificadas com precisão sem qualquer sobreposição de texto, corrigindo a deficiência do treemap anterior.

### ID 4 — Confiança na escrita acadêmica · 1–5 (`v2`)
![ID 4 — Confiança na escrita acadêmica · 1–5 (`v2`)](../exports/v2.png)
- **Insights e informações extraídas:** A distribuição ordinal de confiança na escrita é fortemente concentrada nos níveis intermediário e alto: o nível $4$ é o modal ($1.059$; $41,4\%$), seguido pelo nível $3$ ($952$; $37,3\%$). Juntos, os níveis $3$ e $4$ reúnem $78,7\%$ dos estudantes. Os extremos são minoritários: apenas $1,7\%$ ($43$) declararam confiança mínima ($1$) e $8,9\%$ ($228$) nível $2$, enquanto $10,7\%$ ($273$) declararam confiança máxima ($5$).

### ID 5 — Ferramentas conhecidas (`v1`)
![ID 5 — Ferramentas conhecidas (`v1`)](../exports/v1.png)
- **Insights e informações extraídas:** No momento da coleta (março–abril de 2023), o corretor e assistente de escrita *Grammarly* era a ferramenta mais conhecida ($2.260$; $88,5\%$), superando o *ChatGPT* ($1.761$; $68,9\%$). Em um segundo patamar aparece o parafraseador *QuillBot* ($693$; $27,1\%$) e o gerador de imagens *DALI-E* ($301$; $11,8\%$). Ferramentas como *ChatSonic* ($2,5\%$) e *Jasper Chat* ($2,0\%$) eram residuais, e apenas $7,0\%$ ($178$) afirmaram não conhecer nenhuma das opções listadas.

### ID 6 — Finalidades de utilização ou consideração do uso (`v3`)
![ID 6 — Finalidades de utilização ou consideração do uso (`v3`)](../exports/v3.png)
- **Insights e informações extraídas:** A finalidade *Acadêmica* (ex.: checar gramática, formatar referências) lidera com metade da amostra ($1.302$; $51,0\%$), seguida pelo não uso/não consideração (*Não utilizou nem considerou*: $898$; $35,1\%$). O uso *Pessoal* foi marcado por $763$ estudantes ($29,9\%$) e o *Profissional* por $444$ ($17,4\%$). As categorias *Outro* ($1,7\%$) e *Prefere não informar* ($1,5\%$) têm baixa incidência, mas sua preservação explícita evita confundir recusa de resposta com ausência de uso.

### ID 7 — Conhecimento da ferramenta × conversão para finalidade acadêmica (`v9`)
![ID 7 — Conhecimento da ferramenta × conversão para finalidade acadêmica (`v9`)](../exports/v9.png)
- **Insights e informações extraídas:** Embora *Grammarly* ($88,5\%$ de conhecimento) e *ChatGPT* ($68,9\%$ de conhecimento) dominem em volume absoluto de usuários acadêmicos (bolhas maiores, com $1.251$ e $920$ estudantes respectivamente), ferramentas especializadas de nicho apresentam taxas de conversão proporcional para finalidade acadêmica ainda mais altas entre quem as conhece: $65,2\%$ dos estudantes que conhecem o *QuillBot* ($452 / 693$) selecionaram finalidade acadêmica, contra $55,4\%$ no *Grammarly* e $52,2\%$ no *ChatGPT*.

### ID 8 — Repertório: número de ferramentas conhecidas por estudante (`v10`)
![ID 8 — Repertório: número de ferramentas conhecidas por estudante (`v10`)](../exports/v10.png)
- **Insights e informações extraídas:** A distribuição do repertório individual de ferramentas é simétrica e unimodal em torno de **2 ferramentas** ($1.017$ estudantes; $39,8\%$). Quase dois terços da amostra conhecem entre 1 e 2 ferramentas ($22,9\% + 39,8\% = 62,7\%$), enquanto $24,3\%$ ($622$) conhecem 3 ferramentas e apenas $6,1\%$ ($156$) conhecem 4 ou mais ferramentas. Isso mostra que, no início de 2023, o conhecimento discente estava concentrado no par *Grammarly + ChatGPT*, e não em uma adoção ampla de múltiplos sistemas de IA.

### ID 9 — Confiança na escrita × seleção da finalidade acadêmica (`v5`)
![ID 9 — Confiança na escrita × seleção da finalidade acadêmica (`v5`)](../exports/v5.png)
- **Insights e informações extraídas:** A análise condicional por coluna de confiança revela uma relação não linear interessante: a maior proporção de seleção da finalidade acadêmica ocorre entre estudantes com confiança baixa-intermediária — **nível 2** ($57,5\%$; $131/228$) e **nível 3** ($53,9\%$; $513/952$). À medida que a confiança na própria escrita sobe para o nível 4 ($48,7\%$) e nível 5 ($45,8\%$), cai a proporção dos que recorrem (ou consideram recorrer) a ferramentas assistivas para fins acadêmicos. Já no nível 1 ($n = 43$), a adesão é a menor ($39,5\%$), indicando maior afastamento geral das ferramentas nesse subgrupo reduzido.

### ID 10 — Aceitação: apoio gramatical × redação integral (`v4`)
![ID 10 — Aceitação: apoio gramatical × redação integral (`v4`)](../exports/v4.png)
- **Insights e informações extraídas:** Existe uma inversão clara de julgamento moral conforme a natureza do uso:
- No **apoio gramatical**, a maioria é favorável ou parcialmente favorável ($695 + 671 = 1.366$; $53,5\%$ do total de $2.555$, ou $54,2\%$ excluindo os $33$ casos de *Outro*), enquanto $26,2\%$ são neutros e apenas $19,0\%$ são contrários/parcialmente contrários.
- Na **redação integral de ensaios por IA**, $70,5\%$ ($1.240 + 560 = 1.800$) posicionam-se como contrários ou parcialmente contrários (sendo $48,5\%$ fortemente contrários), e apenas $13,8\%$ ($352$) aceitam a prática. Os estudantes diferenciam nitidamente assistência de revisão e terceirização de autoria.

### ID 11 — Matriz de transição ética: apoio gramatical × redação integral (`v7`)
![ID 11 — Matriz de transição ética: apoio gramatical × redação integral (`v7`)](../exports/v7.png)
- **Insights e informações extraídas:** Ao cruzar as duas respostas no nível do indivíduo, percebe-se que o perfil ético mais frequente de toda a universidade é o estudante **Parcialmente favorável ao apoio gramatical e Contrário à redação integral** ($329$ estudantes; $12,9\%$ do total), seguido por **Neutro na gramática e Contrário na redação integral** ($294$; $11,5\%$) e **Favorável na gramática e Contrário na redação integral** ($197$; $7,7\%$). Somando os quadrantes, $40,9\%$ de toda a amostra apoiam ou são neutros ao auxílio gramatical mas rejeitam terminantemente a redação integral, comprovando que a oposição à geração de ensaios não decorre de tecnofobia geral, mas de um critério específico de autoria intelectual.

### ID 12 — Preferências de políticas institucionais (`v6`)
![ID 12 — Preferências de políticas institucionais (`v6`)](../exports/v6.png)
- **Insights e informações extraídas:** Há forte demanda por regulamentação clara em vez de extremos: $41,1\%$ ($1.049$) preferem uma **política única da universidade**, $26,0\%$ ($665$) defendem **políticas definidas por faculdade/departamento** e $16,9\%$ ($433$) preferem a **decisão de cada professor por avaliação**. Somadas, as três opções de regulação institucional calibrada representam **$84,0\%$** dos respondentes, enquanto a **liberdade irrestrita de uso** ($246$; $9,6\%$) e o **banimento completo** ($116$; $4,5\%$) são amplamente minoritários.

### ID 13 — Preferência de política × aceitação de uso (`v8`)
![ID 13 — Preferência de política × aceitação de uso (`v8`)](../exports/v8.png)
- **Insights e informações extraídas:** O gráfico de barras agrupadas sólidas coloca lado a lado a taxa de aceitação do apoio gramatical (barra azul-marinho) e da redação integral (barra vermelha carmim) para cada modelo de política institucional:
- Em todas as políticas institucionais, a barra de apoio gramatical supera com folga a barra de redação integral, evidenciando que os estudantes enxergam uma fronteira ética categórica entre suporte instrumental e substituição de autoria.
- Entre os defensores do **Banimento completo** ($n = 116$), ambas as barras são residuais: apenas $0,9\%$ aceitam redação integral e $8,6\%$ aceitam apoio gramatical.
- Nas três opções de regulação intermediária (**Política única da universidade**, **Políticas por faculdade** e **Decisão de cada professor**), que reúnem $84,0\%$ da comunidade discente, o apoio gramatical oscila entre $49,9\%$ e $61,4\%$, enquanto a aceitação da redação integral fica contida em patamares reduzidos ($8,0\%\text{–}17,8\%$).
- No grupo que defende **Liberdade de uso** ($n = 246$), a aceitação da redação integral salta para expressivos $47,2\%$ (e o apoio gramatical para $75,2\%$), confirmando que a preferência por ausência de regulação decorre de uma tolerância ética muito maior à geração automatizada de textos.
