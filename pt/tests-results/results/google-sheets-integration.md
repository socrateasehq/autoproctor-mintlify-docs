---
title: "Escrever Resultados no Google Sheets"
description: "Configure a exportação automática de resultados de testes do AutoProctor para o Google Sheets para que os dados fluam em tempo real sem downloads manuais."
---

Em vez de baixar arquivos Excel manualmente após cada teste, você pode configurar o AutoProctor para escrever automaticamente os resultados do teste em uma planilha Google Sheets. Os resultados aparecem na planilha à medida que os candidatos completam seus testes, mantendo seus dados atualizados sem nenhum esforço adicional.

{% hint style="info" %}
Esta é uma **Funcionalidade Premium** e requer uma assinatura Premium ou Elite. Consulte [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalhes dos planos.
{% endhint %}

## Instruções de Configuração

![GIF mostrando como configurar a integração com Google Sheets no AutoProctor](../../images/settings/write-to-gsheet.gif)
*Configurando a integração com Google Sheets*

{% stepper %}
{% step %}
### Abra as configurações do teste
Acesse as **Configurações do Teste** de um teste novo ou existente no seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Localize o campo ID do Google Sheets
Role até a seção **Advanced Settings** e localize o campo **Google Sheets ID**.
{% endstep %}
{% step %}
### Crie uma planilha Google Sheets em branco
Crie uma planilha Google Sheets vazia no seu Google Drive. Você usará esta planilha para receber os resultados do AutoProctor.
{% endstep %}
{% step %}
### Conceda acesso de edição
Compartilhe a planilha Google Sheets com `hello@autoproctor.co` e conceda permissões de **Editor**. Isso permite que o AutoProctor escreva dados na planilha.

{% hint style="warning" %}
Se você não compartilhar a planilha com `hello@autoproctor.co` como Editor, o AutoProctor não conseguirá escrever resultados nela. Certifique-se de conceder acesso de Editor, não apenas de Visualizador.
{% endhint %}
{% endstep %}
{% step %}
### Cole a URL da planilha Google Sheets
Copie a URL da sua planilha Google Sheets e cole-a no campo **Google Sheets ID** nas configurações do teste do AutoProctor.
{% endstep %}
{% step %}
### Salve o teste
Clique em **Create** ou **Update** para salvar a configuração do teste.
{% endstep %}
{% step %}
### Verifique a integração
Complete uma tentativa de teste. Uma nova aba chamada **AutoProctor** aparecerá automaticamente na sua planilha Google Sheets com os dados dos resultados.
{% endstep %}
{% endstepper %}

As tentativas de teste subsequentes preenchem automaticamente a mesma planilha Google Sheets sem necessidade de configuração adicional.

## Integração com Questionários Socratease

Para Questionários Socratease, o sistema escreve tanto as pontuações de supervisão quanto as pontuações do questionário na planilha. No entanto, perguntas e respostas individuais não são incluídas -- apenas dados de pontuação agregados aparecem.

{% hint style="info" %}
Se você precisa de dados detalhados por pergunta para Questionários Socratease, use a visualização de [submissões individuais](tests-results/results/individual-submissions.md) no [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endhint %}

## Recursos Relacionados

- [Exportar para Excel](tests-results/results/export-to-excel.md) -- Baixe resultados manualmente como planilha
- [Acessar Respostas e Entregas do Candidato](tests-results/results/individual-submissions.md) -- Veja respostas detalhadas por candidato
- [Onde Posso Ver os Resultados do Meu Teste?](tests-results/results/how-to-see-results.md) -- Visão geral dos resultados do teste vs. resultados de supervisão
- [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) -- Detalhes dos planos e disponibilidade de funcionalidades
- [Compartilhar Resultados do Teste](tests-results/results/sharing-test-results.md) -- Conceda acesso aos resultados do teste para outros usuários
