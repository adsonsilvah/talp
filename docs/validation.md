# Validação executada

Ambiente: Debian, Python 3.13.5, dependências fixadas, 10/10/2026.

- `python scripts/prepare_data.py`: executado com a planilha real, auditoria e derivado gerados, 2.555 respostas e todos os totais de referência confirmados.
- `python -m pytest -q`: **48 testes passaram**. Inclui round-trip do Excel disponível localmente, parser de vírgulas internas, recortes vazios, métricas, categorias, figuras, callbacks e produção em cópia sem brutos.
- `python -m pip check`: nenhuma incompatibilidade declarada.
- Gunicorn iniciado com dois workers, sem debug, em `127.0.0.1:8050`.
- Cliente HTTP Flask: `/`, `/healthz`, `/_dash-layout`, `/_dash-dependencies`, CSS e callback de filtro responderam 200.
- Navegador: aplicação aberta, filtro de Saúde e Ciências da Vida retornou 759 participantes, navegação para Conhecimento e Finalidades preservou o recorte e renderizou três gráficos. Alturas/área de desenho, presença de todas as categorias e traduções dos controles foram inspecionadas no DOM.
- Detectado e corrigido colapso da altura do Plotly quando `responsive=True`; adicionado teste de regressão para altura explícita do componente.
- Exportação **PNG das seis figuras** e **SVG de V1, V4, V5 e V6** executada com Kaleido 1.5.0 e Chrome local. Arquivos em `exports/`, ignorados pelo Git. V4 e V5 inspecionadas visualmente; fundo branco explícito para relatório.
- Procedência: arquivo oficial baixado e comparado com a fonte local; tabelas idênticas, hashes diferentes. Licença CC BY 4.0 confirmada no catálogo.
- Git: ignorados brutos, PDFs, ambiente virtual e arquivos temporários.

## Limites da validação

Os testes locais não equivalem a CI remoto aprovado. Layout responsivo implementado; validação de usabilidade com usuários, testes em projetor e uma revisão completa de acessibilidade permanecem recomendados.

O teste de round-trip da fonte privada é pulado explicitamente no CI quando o Excel não existe. Os demais testes, inclusive o total e a execução sem brutos, usam o derivado fechado e continuam ativos.

## Revisão: página única e paleta dos slides

Interface reorganizada em oito gráficos na mesma página e quatro categorias. Removidos navegação, KPIs, textos explicativos e modo apresentação. Paleta branca, azul-marinho e vermelha; Outro usa hachura para se distinguir do neutro. Metodologia mantida nos documentos e denominadores nos tooltips.

Após a refatoração, **46 testes passaram** (os testes das seis rotas foram substituídos pelos cenários da página única). O navegador confirmou oito gráficos renderizados, nenhum parágrafo no conteúdo principal e nenhum menu de navegação.
