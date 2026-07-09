---
title: "Exportar Resultados para Excel"
description: "Baixe os resultados dos seus testes do AutoProctor como uma planilha Excel para registro, compartilhamento com colegas e fins de auditoria."
---

O AutoProctor permite exportar os resultados dos seus testes para uma planilha Excel. Isso é útil para compartilhar resultados com colegas, manter registros de auditoria ou armazenar documentação para sua instituição.

## O Que a Exportação Inclui

A planilha exportada contém um resumo de todos os resultados dos candidatos:

| Coluna | Descrição |
|---|---|
| **Nome do candidato** | Nome do participante do teste |
| **Endereço de e-mail** | E-mail usado para realizar o teste |
| **Hora de início do teste** | Quando o candidato iniciou o teste |
| **Hora de envio** | Quando o candidato enviou o teste |
| **Trust Score** | Pontuação de integridade da supervisão (se a supervisão estiver ativada) |
| **Pontuação do questionário** | Pontuação do candidato (apenas para Questionários Socratease) |

![Tabela de resultados no painel do AutoProctor com opção de exportação](../../images/results/export-results-table.png)
*Tabela de resultados com botão Export to Excel*

Você pode consultar uma [planilha de exemplo exportada](https://docs.google.com/spreadsheets/d/1lvkt7n7ZkOushCFYd0ZrTv5YgBAex4CJV78LG88mLx4/edit#gid=0) para ver o formato exato.

## Como Exportar

![GIF mostrando como exportar resultados para Excel no painel do AutoProctor](../../images/results/export-results-to-excel.gif)
*Exportando resultados para Excel*

{% stepper %}
{% step %}
### Abra a página de resultados
Navegue até o seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/) e clique em **Results** do teste que deseja exportar.
{% endstep %}
{% step %}
### Clique no botão Exportar
Clique no botão **Export to Excel** no topo da tabela de resultados. O arquivo é baixado automaticamente para o seu dispositivo.
{% endstep %}
{% step %}
### Abra o arquivo
Abra o arquivo `.xlsx` baixado no Microsoft Excel, Google Sheets ou qualquer aplicativo de planilhas compatível.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Para exportações automáticas e contínuas sem downloads manuais, considere configurar a [integração com Google Sheets](tests-results/results/google-sheets-integration.md).
{% endhint %}

## Recursos Relacionados

- [Integração com Google Sheets](tests-results/results/google-sheets-integration.md) -- Escreva resultados automaticamente em uma planilha Google
- [Onde Posso Ver os Resultados do Meu Teste?](tests-results/results/how-to-see-results.md) -- Visão geral dos resultados do teste vs. resultados de supervisão
- [Compartilhar Resultados do Teste](tests-results/results/sharing-test-results.md) -- Conceda acesso aos resultados do teste para outros usuários
- [Onde Posso Ver os Resultados de Supervisão?](tests-results/results/proctoring-results.md) -- Veja relatórios detalhados de supervisão
