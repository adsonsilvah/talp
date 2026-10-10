# Publicação no Render

## Estado e pré-condições

Os arquivos de produção estão prontos. Isso **não significa que o serviço foi publicado**. É necessário autorizar a divulgação do derivado, preservar a atribuição CC BY 4.0 confirmada no catálogo, criar/conectar o GitHub e autorizar a hospedagem. Nenhum recurso pago é necessário para preparar o projeto.

## Passos após autorização

1. Publicar código e derivado fechado no repositório autorizado. Verificar que `data/raw/`, `referencias/`, `.env` e `.local/` não foram enviados.
2. Entrar no Render, conectar a conta GitHub e permitir acesso apenas ao repositório escolhido.
3. Criar um **Blueprint** selecionando o repositório e [render.yaml](../render.yaml). Conferir no resumo **Web Service / Python / Free** antes de confirmar; não aceitar upgrade ou cobrança não autorizados.
4. A instalação executa `pip install -r requirements.txt`. A inicialização usa `gunicorn app:server --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile -`.
5. Verificar o build e os logs. O health check `/healthz` deve responder HTTP 200 com `status: ok` e a base Liverpool disponível.
6. Abrir a URL HTTPS fornecida e verificar os oito gráficos da página única, filtros, restauração e recorte vazio. A produção só é validada depois dessas verificações na URL pública.

Não há Excel, PDFs, openpyxl ou Kaleido no caminho de execução do servidor. Python está fixado em 3.13.5. `.env` não é carregado automaticamente; variáveis são definidas pela plataforma. `PORT` é fornecida pelo Render e o modo debug não é usado.

## Atualização

O Blueprint usa `branch: main` e `autoDeployTrigger: checksPass`: após revisão e merge no GitHub, a atualização aguarda checks aprovados. Confirme essa opção também no painel do serviço. O workflow é validado localmente por testes, mas só se sabe se o CI hospedado passa depois de sua primeira execução no GitHub.

Para atualizar dados, reexecute a preparação local com fonte autorizada, revise auditoria/derivado/testes e envie por Pull Request. O disco efêmero do Render não é armazenamento permanente para edições manuais. Para reverter uma falha, use a versão anterior disponível no painel ou um revert revisado no GitHub.

## Plano gratuito e apresentação

O plano gratuito pode suspender serviços após inatividade e apresentar demora na primeira requisição; há limites de horas, CPU, memória e disponibilidade, sujeitos a alterações do provedor. Confirme os termos vigentes em [Render Free](https://render.com/docs/free). Não há garantia de serviço contínuo ou SLA para apresentação.

Antes de apresentar, abra a URL e teste os fluxos com antecedência. Prepare uma execução local e as exportações estáticas como contingência. Para disponibilidade contínua, avalie plano pago somente com autorização explícita; nenhum serviço pago foi contratado. Não dependa de requisições artificiais para contornar limites do plano.

A URL pública funciona independentemente do VS Code e do computador do desenvolvedor quando hospedada. Um servidor apenas em localhost não é deploy.
