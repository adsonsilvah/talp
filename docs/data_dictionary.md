# Contrato de dados

O [relatório de auditoria](data_audit.md) contém os **16 cabeçalhos originais, A–P, tipos, ausências, categorias e frequências**. O mapeamento único está em [liverpool_schema.json](../src/datasets/liverpool_schema.json); nenhum módulo analítico usa índices posicionais da planilha.

O artefato [liverpool2023.json](../data/processed/liverpool2023.json) contém `schema_version`, `dataset_id`, `source_sha256`, `respondents` e `records`. Cada registro contém:

| Campo | Representação | Significado |
|---|---|---|
| faculty | string nominal original | Faculdade; Not sure é preservado |
| study_level | string nominal original | Nível/modalidade; sem escala numérica |
| confidence | inteiro ordinal 1–5 | 1 nada confiante; 5 muito confiante |
| awareness | lista de alternativas completas | Ferramentas conhecidas antes da pesquisa |
| purposes | lista de alternativas completas | Finalidades de utilização **ou consideração** |
| grammar_attitude | categoria ordinal inglesa abreviada | Opinião sobre outro estudante usar apoio gramatical |
| essay_attitude | categoria ordinal inglesa abreviada | Opinião sobre outro estudante gerar todo o trabalho |
| policy | string nominal original | Preferência institucional, escolha única |

Textos longos de opinião são mapeados para Supportive, Somewhat supportive, Neutral, Somewhat unsupportive, Unsupportive; Other é categoria independente. O texto integral de cada alternativa original permanece no contrato/auditoria. Não há dados ausentes nesses campos nesta versão; ausências ou categorias desconhecidas futuras causam erro, em vez de imputação silenciosa.

Traduções são centralizadas em [schema.py](../src/datasets/schema.py). Novas bases precisam do próprio contrato, decisões de ausências e adaptador. Não adicione valores desconhecidos automaticamente ao contrato existente.
