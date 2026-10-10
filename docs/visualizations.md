# Abstração de dados e tarefas

Fundamentação: material local `DataVis_Aula_1_merged.pdf`, seções “Tipos de atributos”, “Marcas, canais e regras gerais”, “Abstração de tarefas” e “Visualizando dados tabulares”; Munzner (2014), *Visualization Analysis and Design*, capítulos 4–7; Brehmer e Munzner (2013), tipologia multinível de tarefas. O PDF da disciplina permanece local, fora do repositório.

Partimos de perguntas de domínio, abstraímos atributos e tarefas, escolhemos codificações e validamos denominadores e interpretação. A interação permite exploração; a ordem das categorias na mesma página organiza: amostra → conhecimento/finalidades → limites acadêmicos → políticas.

| Visual | Pergunta/tarefa | Dados e codificação | Decisão e limite |
|---|---|---|---|
| V1 | O que conheciam? Identificar/comparar | Nominal multirresposta → comprimento de barras horizontais, ordenadas por frequência | Comprimento em base comum; todas as opções, inclusive nenhuma e Outro |
| V2 | Como varia a confiança? Resumir/comparar | Ordinal 1–5 → posição discreta fixa e altura quantitativa | Sem média nem curva que sugira continuidade; agrupamento por faculdade/nível |
| V3 | Para que utilizaram ou consideraram? Comparar | Nominal multirresposta → barras, possíveis grupos por cor | Não representa uso efetivo; soma pode exceder 100%; não esconder recusas |
| V4 | Apoio ou autoria integral? Comparar distribuições | Cinco opiniões ordinais → segmentos em ordem, cada cenário a 100% | Azul para apoio, branco central para neutro, vermelho para oposição; Outro branco hachurado no fim, nunca incorporado ao neutro |
| V5 | Confiança associa-se à finalidade? Explorar | Ordinal × binário → matriz, luminância azul sequencial para magnitude | Denominador por coluna; sem observações = célula sem cor; hover resolve leitura exata |
| V6 | Quem deveria definir regras? Identificar/comparar | Política nominal → barras ordenadas ou agrupadas | Todas as seis alternativas; denominador do grupo, nunca total de seleções |

Distribuições adicionais de faculdade/nível contextualizam a amostra. A interface contém apenas gráficos, títulos e filtros; detalhes metodológicos permanecem na documentação e nos tooltips.

## Regras perceptuais e de interação

- Escalas quantitativas de barras partem do zero. Categoria e cor não substituem numeradores/denominadores.
- Cor de grupos é categórica; heatmap usa luminância sequencial; opiniões mantêm ordem e significado em todos os gráficos.
- Multirrespostas não são partes exclusivas de um todo, portanto não recebem pizza nem empilhamento a 100%.
- Barras empilhadas facilitam a comparação da distribuição geral, mas os segmentos internos têm bases diferentes. O hover fornece leitura exata; uma futura versão pode acrescentar pontos por categoria.
- Legendas identificam grupos; títulos, eixos e tooltips explicam as medidas. Títulos da interface quebram linha fora do SVG para melhorar legibilidade em telas estreitas.
- Filtros atualizam todos os gráficos na mesma página; “Restaurar filtros” também redefine agrupamento e unidade. Ausência de dados mostra mensagem, não estimativa de 0%.
- Grupos n<30 são omitidos apenas das comparações agrupadas e os tooltips informam grupos/pessoas omitidos; a regra é descritiva, não teste de significância nem mecanismo completo de privacidade.
- Paleta baseada nos slides da disciplina: branco, azul-marinho e vermelho. Tons claros codificam intensidades; hachura distingue Outro do neutro na distribuição de opiniões.
- Sem séries temporais, mapas, 3D, radar ou inferência de sentimento, pois os atributos e tarefas não justificam essas representações.

## Denominadores

Indicadores: todos do recorte. Barras: todos do recorte ou do grupo. Likert: todos, incluindo Outro. Heatmap: todos em cada nível de confiança do recorte. Recusas e respostas contraditórias permanecem; o audit trail está no [relatório](data_audit.md).
