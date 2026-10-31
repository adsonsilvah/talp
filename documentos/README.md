# Documentos do Projeto TALP

Esta pasta reúne a documentação acadêmica e relatórios formais gerados para o projeto **"IA no Ensino Superior — Percepções Estudantis e Integridade Acadêmica"**, seguindo rigorosamente os critérios metodológicos de visualização de dados (Munzner, 2014; Cleveland & McGill, 1984).

---

## Arquivos Disponíveis

1. **[relatorio_visualizacao_dados.docx](relatorio_visualizacao_dados.docx)**:
   - Relatório acadêmico completo formatado no padrão ABNT / Word com todas as tabelas (Abstração de Dados, Abstração de Tarefas, Codificações Visuais) e os 13 gráficos em alta resolução incorporados com seus respectivos insights.
   - *Como abrir:* Abra com o LibreOffice Writer (`libreoffice documentos/relatorio_visualizacao_dados.docx`), Microsoft Word ou importe para o Google Docs.

2. **[relatorio_visualizacao_dados.md](relatorio_visualizacao_dados.md)**:
   - Versão em texto Markdown do relatório acadêmico completo.
   - *Como abrir:* Pode ser lido diretamente no editor do Antigravity, no VS Code ou no visualizador do GitHub.

3. **[escolha_dos_graficos.md](escolha_dos_graficos.md)**:
   - Documento detalhado de fundamentação teórica que explica a escolha de cada uma das 13 visualizações com base na hierarquia perceptual de canais visuais de Munzner e Cleveland & McGill, incluindo a justificativa de descarte de representações problemáticas (como Treemap e Dumbbell plot).

---

## Como Reconstruir os Relatórios

Para atualizar ou regenerar os documentos após alterações nos gráficos ou análises, execute a partir da raiz do projeto:

```bash
# 1. (Opcional) Reexporta as imagens dos gráficos se houve mudanças de código
BROWSER_PATH=/home/adson/Documentos/projeto-TALP/.local/chrome/chrome-linux64/chrome .venv/bin/python scripts/export_static.py

# 2. Reconstrói os relatórios em DOCX e Markdown
.venv/bin/python scripts/build_report.py
```
