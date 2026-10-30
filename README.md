# IA no Ensino Superior — Percepções Estudantis e Integridade Acadêmica

Dashboard acadêmico em português brasileiro, desenvolvido para a disciplina de Visualização de Dados. Explora o conhecimento de ferramentas, as finalidades de utilização **ou consideração do uso**, as opiniões sobre integridade acadêmica e as políticas desejadas por estudantes.

A aplicação usa exclusivamente **dados reais de Liverpool 2023**: 2.555 respostas, coleta voluntária em março–abril de 2023, University of Liverpool, Reino Unido. Não mede separadamente uso efetivo e intenção de uso, nem permite inferência causal.

Referência: Johnston, H.; Wells, R. F.; Shanks, E. M.; Boey, T.; Parsons, B. N. (2024). *Student perspectives on the use of generative artificial intelligence technologies in higher education*. International Journal for Educational Integrity, 20, 2. [DOI do artigo](https://doi.org/10.1007/s40979-024-00149-4). [Depósito de dados citado](https://doi.org/10.17638/datacat.liverpool.ac.uk/2297).

## O que está disponível

Uma única página com oito gráficos, organizados em Perfil dos Respondentes, Conhecimento e Finalidades, Integridade Acadêmica e Políticas Institucionais. A interface contém apenas títulos, gráficos e filtros de base, faculdade, nível e confiança, além de unidade, agrupamento e restauração. Numeradores, denominadores e observações de multirresposta ficam nos tooltips. A documentação metodológica permanece neste repositório. Paleta branca, azul-marinho e vermelha inspirada nos slides da disciplina. Gráficos construídos com Plotly Express e Graph Objects:

1. V1: conhecimento de todas as ferramentas/opções (barras horizontais).
2. V2: confiança ordinal 1–5, com comparação por faculdade/nível.
3. V3: todas as finalidades, preservando multirresposta e recusas.
4. V4: duas distribuições de opinião empilhadas a 100%, cinco categorias ordenadas e Outro separado.
5. V5: confiança × seleção da finalidade acadêmica (heatmap por coluna).
6. V6: todas as políticas institucionais, com comparação por faculdade/nível.

Também há distribuições de faculdade e nível. Comparações agrupadas mostram somente grupos com n≥30 e informam omissões nos tooltips. Este limiar não garante precisão ou anonimização. A seleção “por confiança” aplica-se à Integridade Acadêmica; os demais gráficos agrupáveis usam faculdade ou nível.

## Ambiente local — Debian 13

Requisitos: Python 3.13, módulo venv e Git. Se faltarem pacotes do sistema, um administrador pode instalar `python3-venv` e `git` pelo gerenciador do Debian. Nenhum comando abaixo instala pacotes Python globalmente.

Na raiz deste projeto:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python app.py
```

Abra <http://127.0.0.1:8050>. A aplicação local roda sem debug. Para ativar o ambiente opcionalmente: `source .venv/bin/activate`.

As dependências de produção estão em [requirements.txt](requirements.txt); preparação/testes em [requirements-dev.txt](requirements-dev.txt); exportação em [requirements-export.txt](requirements-export.txt). [requirements-lock.txt](requirements-lock.txt) registra todas as versões do ambiente de desenvolvimento validado (Debian/Python 3.13), sem dependências opcionais de exportação. Para reproduzir exatamente esse ambiente, instale esse arquivo em uma venv nova.

## Dados: executar e reproduzir

A aplicação carrega [data/processed/liverpool2023.json](data/processed/liverpool2023.json), suficiente para produção: não lê Excel ou PDFs, nem exige openpyxl no servidor. O arquivo contém somente oito variáveis fechadas. Não há respostas abertas ou identificadores originais.

Para reproduzir a transformação, mantenha sua cópia da planilha em `data/raw/liverpool2023.xlsx`, ignorada pelo Git, e execute:

```bash
.venv/bin/python scripts/prepare_data.py
```

Outro nome/caminho pode ser informado por `--input` e o destino por `--output`. A transformação valida os 16 cabeçalhos e categorias contra um contrato central, verifica os totais de referência, preserva respostas contraditórias e gera a auditoria. Opções multirresposta são reconhecidas por textos completos, nunca por divisão ingênua em vírgulas. A origem é registrada por SHA-256. Brutos não são modificados.

[Auditoria e dicionário completo](docs/data_audit.md), [contrato de dados](docs/data_dictionary.md), [justificativas visuais](docs/visualizations.md).

**Divergência registrada:** 1.366/2.555 = 53,46% de apoio gramatical, contra 54,1% no artigo. O denominador público do dashboard inclui Outro. Os dados não foram ajustados para reproduzir números publicados. Multirresposta pode somar mais de 100%.

**Publicação:** brutos e PDFs ficam fora do Git. O catálogo oficial foi consultado: planilha e README são **CC BY 4.0**. A comparação confirmou valores e cabeçalhos idênticos aos da cópia local (arquivos binários diferentes). Veja [procedência e atribuição](docs/data_provenance.md). A divulgação pública do derivado ainda depende da autorização do proprietário. O derivado ainda contém combinações raras; excluir textos não é anonimização formal.

## Testes

```bash
.venv/bin/python -m pytest -q
```

A suíte verifica parser, estrutura, totais, denominadores, filtros, Likert, figuras, recortes vazios, callbacks HTTP, registro de bases e inicialização de produção em cópia isolada **sem arquivos brutos**. O round-trip Excel é executado apenas se o arquivo privado estiver presente; no CI ele é explicitamente pulado. Veja [validação](docs/validation.md).

## Exportar PNG ou SVG

Kaleido é opcional e separado do servidor:

```bash
.venv/bin/python -m pip install -r requirements-export.txt
.venv/bin/plotly_get_chrome
.venv/bin/python scripts/export_static.py --format png
.venv/bin/python scripts/export_static.py --format svg --charts v1 v4 v6
```

Kaleido 1.x exige Chrome/Chromium e as bibliotecas do sistema desse navegador. `plotly_get_chrome` solicita confirmação para baixar um Chrome compatível; use somente se não existir um compatível. Em ambientes sem essas bibliotecas, instale Chromium pelo Debian. A execução web não depende desses componentes. Para indicar outro executável do navegador, use a variável `BROWSER_PATH`.

As figuras são salvas em `exports/`, ignorado pelo Git, com fonte, tamanho do recorte e nota metodológica incorporados. Um README registra os filtros. Exemplo real de recorte:

```bash
.venv/bin/python scripts/export_static.py --charts v2 v5 --faculty 'Health and Life Sciences' --confidence 3 --confidence 4
```

A barra de ferramentas Plotly também permite baixar PNG no navegador, sem Kaleido. Para figuras de relatório com notas metodológicas incorporadas, prefira o script.

## Estrutura

```text
app.py                       # página única, callbacks e app:server
assets/style.css             # interface responsiva
src/config.py                # caminhos e configuração
src/datasets/                # contrato, adaptador e registro de bases
src/processing/              # validação, transformação, filtros e métricas
src/charts/                  # funções Plotly independentes do Dash
src/components/              # filtros e cartões
pages/                       # página única com quatro categorias
scripts/                     # preparação/auditoria e exportação
tests/                      # validações automatizadas
data/raw/                   # privado, ignorado pelo Git
data/processed/             # derivado fechado para execução
docs/                       # metodologia, arquitetura, colaboração e deploy
.github/workflows/ci.yml     # CI no GitHub
render.yaml                  # Blueprint de publicação
```

## Colaboração via GitHub

A branch `main` recebe versões estáveis. Use `feature/*` para funcionalidades e `fix/*` para correções. Atualize a branch local antes de começar:

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/nova-analise
# Faça as alterações e execute os testes.
.venv/bin/python -m pytest -q
git add src pages tests docs
git commit -m "feat: adiciona nova análise"
git push -u origin feature/nova-analise
```

Abra um Pull Request no GitHub com pergunta analítica, justificativa visual e testes. O outro desenvolvedor revisa, o CI passa e então o responsável faz merge para `main`. Use branches protegidas e ao menos uma aprovação quando disponíveis no plano do repositório. Não faça push direto para `main` no trabalho cotidiano.

O repositório remoto só deve ser criado após definição de nome, proprietário e visibilidade. Não há publicação automática por executar estes scripts. [Fluxo completo, criação do remoto e convite de colaborador](docs/collaboration.md).

## Render e servidor de produção

[render.yaml](render.yaml) instala apenas dependências web e executa Gunicorn, expõe a porta de `$PORT`, desativa o modo de desenvolvimento e verifica `/healthz`. O serviço pode executar sem qualquer computador local ligado. Publicação automática de `main` está configurada para ocorrer após os checks passarem.

Teste local do mesmo servidor, em terminal separado:

```bash
.venv/bin/gunicorn app:server --bind 127.0.0.1:8050 --workers 2 --timeout 120
```

O arquivo de exemplo de ambiente documenta `HOST` e `PORT`; não há carregamento automático de `.env` nem segredos necessários. [Passo a passo de publicação, atualização e limites do plano gratuito](docs/deployment.md).

## Limitações e próximos passos

Somente uma instituição e uma coleta; amostra voluntária; comparação descritiva sem causalidade; valores de 2023 não refletem necessariamente ferramentas atuais. Revisar visualmente em projetor e com usuários da disciplina. Obter autorização do proprietário antes de publicar o derivado, preservando atribuição CC BY 4.0. Novas bases exigem adaptadores, auditoria e verificação de equivalência conceitual antes de qualquer comparação — nenhuma base futura é simulada no seletor. Não há análise automática dos textos livres.
