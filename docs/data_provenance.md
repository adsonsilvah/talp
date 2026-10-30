# Procedência e licença

Verificação realizada em 10 de outubro de 2026.

- Dados: **Parsons, Bryony N.; Johnston, Heather (2023)**. *Student perspectives on the use of Generative Artificial Intelligence Technologies in Higher Education*. University of Liverpool Data Catalogue. DOI: https://doi.org/10.17638/datacat.liverpool.ac.uk/2297.
- [Página oficial](https://datacat.liverpool.ac.uk/2297/): identifica **Creative Commons: Attribution 4.0** para os dois arquivos disponíveis, planilha e README.
- [Planilha oficial](https://datacat.liverpool.ac.uk/2297/1/Raw%20data.xlsx).
- [README oficial](https://datacat.liverpool.ac.uk/2297/2/README%20file%20for%20data.docx): confirma 2.555 respostas, uma pessoa por linha, cabeçalhos na primeira linha, alternativas sem codificação, confiança de 1 a 5 e coleta em março–abril de 2023. Os autores informam ausência de identificadores; aqui isso não é tomado como garantia contra informação contextual identificável nos textos livres.
- [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): preservar autoria, fonte, licença e indicação de alterações.

## Verificação da cópia local

O arquivo oficial foi baixado apenas para `.local/`, ignorado pelo Git. A comparação `pandas.read_excel(...).equals(...)` entre oficial e local retornou **True**, com 2.555 linhas × 16 colunas. Cabeçalhos e valores são iguais. Os arquivos não são binariamente idênticos; diferenças de metadados/empacotamento são possíveis, mas sua causa não foi investigada.

- SHA-256 local: `b201fbdc6e7cff8ab32cc42aed690ecd434ccaf6e2c2168f2a12411c7c1b20ed`.
- SHA-256 oficial: `93ef86d0c083b5d1d73f59d41d89e50dfe6c8bd3e3ce2286b7371d2ed96f7696`.

## Alterações deste derivado

Excluídos consentimento e todas as sete colunas de texto livre. Multirrespostas convertidas em listas por vocabulário completo; prefixos das categorias de opinião substituem seus enunciados longos. Categorias inglesas e todas as linhas preservadas. Traduções são apenas de exibição. Sem deduplicação, imputação, ponderação ou correção silenciosa de respostas contraditórias.

O derivado de dados é atribuído aos autores acima sob CC BY 4.0, com essas modificações documentadas. Isso não atribui licença ao código do projeto nem aos materiais da disciplina. A licença permite reutilização com suas condições; a publicação neste projeto continua condicionada à autorização expressa do proprietário.
