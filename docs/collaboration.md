# Git e colaboração

## Primeiro remoto

Confirmar com o proprietário: nome definitivo, conta/organização e visibilidade pública ou privada. A criação e o envio não fazem parte da execução automática da aplicação.

GitHub CLI não foi encontrado no ambiente inicial. Para utilizá-lo, instalar `gh` pelo gerenciador do Debian com um administrador e autenticar interativamente:

```bash
gh auth login
gh auth status
```

Nunca copie tokens para arquivos do projeto. Sem CLI, é possível criar um repositório vazio pela interface GitHub (sem README inicial) e usar SSH ou um gerenciador de credenciais para o Git.

Se a identidade Git estiver ausente, configure **somente neste repositório**, substituindo os exemplos pelos dados reais do autor:

```bash
git config --local user.name 'SEU NOME'
git config --local user.email 'SEU EMAIL OU NOREPLY'
```

Antes do commit, confira que brutos, PDFs e segredos não aparecem no stage. O derivado também precisa de autorização antes de publicação remota.

```bash
git status --short
git add .
git diff --cached --stat
git commit -m "feat: implementa dashboard acadêmico Liverpool 2023"
```

Após autorização, exemplo com CLI (substitua proprietário/nome e escolha explicitamente `--private` ou `--public` conforme autorizado):

```bash
gh repo create PROPRIETARIO/NOME --private --source=. --remote=origin --push
```

Alternativa após criar o repositório vazio no site:

```bash
git remote add origin git@github.com:PROPRIETARIO/NOME.git
git push -u origin main
```

## Dois ou mais desenvolvedores

O proprietário abre **Settings → Collaborators / Manage access → Add people**, informa o usuário GitHub do colega e envia o convite. Em organizações, conceda acesso por equipe quando apropriado. O colega aceita, clona o repositório, cria `.venv` e instala as dependências. Nenhuma senha deve ser compartilhada.

`main` é estável. Antes de iniciar uma tarefa, `git switch main` e `git pull --ff-only origin main`; depois crie `feature/descricao` ou `fix/descricao`. Commits curtos e descritivos; uma alteração coerente por commit. Use `git status` antes de stage e evite `git add .` quando houver arquivos não relacionados.

Abra Pull Request para `main` com problema analítico, solução, evidência visual se pertinente e validação. O colega revisa; os testes de [ci.yml](../.github/workflows/ci.yml) devem passar. Após aprovação, faça merge pelo GitHub (squash é uma opção, mantendo mensagem descritiva). Atualize a cópia local de `main` antes da próxima tarefa.

Configure proteção/ruleset de `main` com CI obrigatório e uma revisão, conforme recursos do plano GitHub. Não contorne falhas nem use force-push para reescrever `main`. Merge aprovado dispara publicação no Render quando o serviço estiver autorizado e conectado.
