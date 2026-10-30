# Auditoria — Liverpool 2023

Relatório gerado por `python scripts/prepare_data.py`; nenhuma resposta aberta individual é reproduzida.

Uma aba (`Sheet 1`), 2,555 respostas, 16 colunas. SHA-256 da fonte: `b201fbdc6e7cff8ab32cc42aed690ecd434ccaf6e2c2168f2a12411c7c1b20ed`.

## Dicionário de dados

| Coluna | Nome interno | Tipo analítico | Ausências | Valores distintos | Cabeçalho original |
|---|---|---|---:|---:|---|
| A | consent | Nominal | 0 | 1 | 1. Please provide your consent to continue. |
| B | faculty | Nominal | 0 | 4 | 2. Which faculty do you belong to? (if you are unsure, you can view this word file to help). |
| C | study_level | Nominal | 0 | 5 | 3. What level of study are you? |
| D | confidence | Ordinal 1–5 | 0 | 5 | 4. How confident are you in writing in an academic manner? (1= not confident, 5=very confident) |
| E | awareness | Nominal multirresposta | 0 | 47 | 5. Prior to this survey, have you heard of any of the following assistive technologies? Select all that apply. |
| F | other_tools | Texto livre (excluído) | 2530 | 25 | 5.a. If you selected Other, please specify: |
| G | purposes | Nominal multirresposta | 0 | 21 | 6. If you have used, or considered using them before, what purpose was this for? Select as many as apply. |
| H | other_purposes | Texto livre (excluído) | 2512 | 43 | 6.a. If you selected Other, please specify: |
| I | grammar_attitude | Ordinal + Outro | 0 | 6 | 7. How would you feel if another student had used an assistive technology as an academic aid (e.g. for grammar help) to complete a piece of coursework? Select the statement which best matches your point of view. |
| J | grammar_reason | Texto livre (excluído) | 2522 | 33 | 7.a. If you selected Other, please specify: |
| K | essay_attitude | Ordinal + Outro | 0 | 6 | 8. How would you feel if another student had used an assistive technology such as Chat GPT to write their entire essay for them? Select the statement which best matches your point of view. |
| L | essay_reason | Texto livre (excluído) | 2515 | 40 | 8.a. If you selected Other, please specify: |
| M | policy | Nominal | 0 | 6 | 9. How do you think the university should respond to these technologies? |
| N | policy_reason | Texto livre (excluído) | 2509 | 46 | 9.a. If you selected Other, please specify: |
| O | other_study_uses | Texto livre (excluído) | 1445 | 1032 | 10. Can you think of any other ways these technologies would be useful to you in your studies? |
| P | comments | Texto livre (excluído) | 1952 | 413 | 11. Do you have any other comments? |

Nível de estudo é apresentado como nominal: Foundation/graduação/pós-graduação têm relações institucionais, mas modalidades de pós-graduação não constituem uma escala numérica. Confiança e opiniões são ordinais, nunca médias numéricas. Consentimento é verificado e excluído do produto processado.

## Categorias e frequências observadas

### consent

| Categoria original | n |
|---|---:|
| I understand that I am under no obligation to complete this survey and I consent to my answers being anonymously recorded and used for research purposes. | 2555 |

### faculty

| Categoria original | n |
|---|---:|
| Humanities and Social Sciences | 1033 |
| Health and Life Sciences | 759 |
| Science and Engineering | 680 |
| Not sure | 83 |

### study_level

| Categoria original | n |
|---|---:|
| Undergraduate | 1782 |
| Postgraduate - Taught | 579 |
| Postgraduate - Research | 167 |
| Foundation | 17 |
| Not sure | 10 |

### confidence

| Categoria original | n |
|---|---:|
| 4 | 1059 |
| 3 | 952 |
| 5 | 273 |
| 2 | 228 |
| 1 | 43 |

### awareness

| Categoria original | n |
|---|---:|
| Grammarly | 2260 |
| Chat GPT | 1761 |
| ChatSonic | 65 |
| Jasper Chat | 52 |
| QuillBot | 693 |
| DALI-E | 301 |
| None of the above | 178 |
| Other | 25 |

47 combinações distintas. Frequências de seleções; denominador = 2.555 respondentes, não o total de seleções. A soma pode ultrapassar 100%.

### purposes

| Categoria original | n |
|---|---:|
| Personal e.g. translations, recipes | 763 |
| Academic e.g. checking grammar, formatting references | 1302 |
| Professional e.g. creating to-do lists, rotas, e-mails | 444 |
| I have not used or considered using them | 898 |
| Prefer not to say | 38 |
| Other | 43 |

21 combinações distintas. Frequências de seleções; denominador = 2.555 respondentes, não o total de seleções. A soma pode ultrapassar 100%.

### grammar_attitude

| Categoria original | n |
|---|---:|
| Supportive – I think in 2023 we should all be using artificial intelligence technologies to make our life easier. | 695 |
| Somewhat supportive – I am fine with other students using software if they give credit to the technology in their work. | 671 |
| Neutral – I don’t really have an opinion on this. I think it’s up to the individual student to decide to use it/not the use it. | 670 |
| Somewhat unsupportive – I think these technologies still have a lot of limitations and I would encourage other students to check the information they find. | 296 |
| Unsupportive – I think it is really unfair for other students to use these technologies. People who use these technologies are effectively copying the work of others without giving full credit. | 190 |
| Other | 33 |

### essay_attitude

| Categoria original | n |
|---|---:|
| Unsupportive – I think it is really unfair for other students to use these technologies. People who use these technologies are effectively copying the work of others without giving full credit. | 1240 |
| Somewhat unsupportive – I think these technologies still have a lot of limitations and I would encourage other students to check the information they find. | 560 |
| Neutral – I don’t really have an opinion on this. I think it’s up to the individual student to decide to use it/not the use it. | 363 |
| Somewhat supportive – I am fine with other students using software if they give credit to the technology in their work. | 209 |
| Supportive – I think in 2023 we should all be using artificial intelligence technologies to make our life easier. | 143 |
| Other | 40 |

### policy

| Categoria original | n |
|---|---:|
| Have a university wide policy on when they are and or not appropriate to use | 1049 |
| Let departments/faculties decide the policy when they are or are not appropriate to use | 665 |
| Let lecturers decide individual policies for individual assignments on when they are or are not appropriate to use | 433 |
| Allow them to be used however the students wish | 246 |
| Ban them entirely | 116 |
| Other | 46 |

## Inconsistências e decisões

- 4 respostas selecionam 'None of the above' junto a outra alternativa.
- 17 respostas selecionam 'I have not used or considered using them' junto a outra alternativa; 2 selecionam 'Prefer not to say' junto a outra alternativa. Há sobreposição entre esses indicadores.
- 131 linhas completamente iguais. Foram preservadas: sem identificadores não há evidência de submissões duplicadas; respostas fechadas iguais podem ser legítimas.
- Nenhuma ausência nas nove colunas fechadas, incluindo consentimento. Ausências nos textos opcionais não são imputadas.
- Nenhuma alternativa desconhecida foi aceita. A grafia original DALI-E foi preservada; Chat GPT é exibido como ChatGPT.
- O parser consome alternativas completas de um vocabulário validado; vírgulas internas de G não delimitam alternativas.
- Todas as seleções contraditórias são mantidas. 'Não selecionou finalidade acadêmica' não significa que nunca utilizou IA; inclui recusas e outras finalidades.

## Comparação com o artigo

| Indicador | Planilha: n / 2.555 | Calculado | Artigo |
|---|---:|---:|---:|
| Conhecia o ChatGPT | 1761 / 2.555 | 68.9237% | 68.9% |
| Finalidade acadêmica | 1302 / 2.555 | 50.9589% | 50.9% |
| Apoio gramatical · favoráveis | 1366 / 2.555 | 53.4638% | 54.1% |
| Redação integral · contrários | 1800 / 2.555 | 70.4501% | 70.4% |
| Política institucional única | 1049 / 2.555 | 41.0568% | 41.1% |

Grammarly: 2260/2.555 (artigo: 88,5%). Os totais por faculdade e os cinco totais de referência foram verificados pelo script.

Apoio gramatical: 1.366/2.555 = 53,4638%, contra 54,1% no artigo (diferença −0,6362 ponto percentual). Excluindo os 33 'Outro', 1.366/2.522 = 54,1634% (54,2% por arredondamento convencional). Isso sugere diferença de denominador e/ou arredondamento, mas não comprova a metodologia publicada. Não se alteraram registros para reproduzir 54,1%. O artigo informa exclusão de 'Other' nas análises ordinais; isso não esclarece integralmente o percentual do resumo.

## Privacidade, origem e reutilização

Fonte local: planilha fornecida no projeto. Artigo: Johnston, Wells, Shanks, Boey e Parsons (2024), DOI https://doi.org/10.1007/s40979-024-00149-4. Repositório de dados citado: https://doi.org/10.17638/datacat.liverpool.ac.uk/2297.

O artigo declara CC BY 4.0 para seu conteúdo e CC0 para dados disponibilizados no artigo salvo indicação contrária. O catálogo externo foi consultado em 10/10/2026: Raw data.xlsx e seu README estão explicitamente sob CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). A comparação pandas entre a fonte local e o arquivo oficial confirmou igualdade dos 2.555 × 16 valores e cabeçalhos, embora os hashes dos arquivos Excel difiram. Veja data_provenance.md para evidências e atribuição.

Respostas livres podem mencionar pessoas, circunstâncias ou detalhes identificáveis. Foi examinada sua estrutura e presença, sem reproduzir seus conteúdos: a decisão conservadora é excluir integralmente F, H, J, L, N, O e P. Não há classificação automática nem declaração de anonimização desses textos. Brutos e PDFs permanecem ignorados pelo Git.

O derivado contém oito variáveis fechadas, sem consentimento, índices originais ou textos livres; mantém categorias inglesas. Combinações raras podem permitir inferências. A divulgação do derivado também requer autorização do proprietário, atribuição CC BY 4.0 e indicação das transformações; remoção de textos não equivale a anonimização formal. Não há download de microdados na interface. Comparações agrupadas omitem grupos com n<30, regra descritiva que não garante sigilo ou precisão estatística.

## Limitações e denominadores

Amostra voluntária, uma instituição do Reino Unido, março–abril de 2023; 8,86% da população universitária segundo o artigo. Sem ponderação, inferência causal ou extrapolação para todos os estudantes. As ferramentas do questionário incluem assistentes que não são estritamente IA generativa. Não há medida de uso efetivo separada de intenção/consideração.

KPIs e barras: denominador = todos os respondentes do filtro; agrupadas = total do grupo dentro do filtro. Likert: cinco categorias em ordem, com Outro como sexta categoria separada semanticamente, denominador inclui Outro. Heatmap: denominador = total em cada nível de confiança dentro do filtro; colunas sem respondentes ficam sem estimativa. Arredondamento visual a uma casa, cálculos em precisão completa.
