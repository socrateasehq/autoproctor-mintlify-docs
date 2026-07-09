---
title: "Concorrência - Máximo de Candidatos Simultâneos"
description: "Entenda os limites de concorrência do AutoProctor que controlam quantos candidatos podem iniciar testes simultaneamente em uma janela de 60 segundos."
---

A concorrência controla quantos candidatos podem iniciar qualquer teste na sua conta dentro da mesma janela de 60 segundos. Entender esses limites ajuda você a planejar sessões de teste em grande escala e evitar atrasos inesperados para os candidatos.

## O Que é Concorrência Máxima?

A concorrência máxima é o número máximo de candidatos que podem começar um teste dentro de qualquer período contínuo de 60 segundos. Esse limite se aplica a **todos os testes da sua conta**, não a cada teste individual.

{% hint style="info" %}
Se você tem três testes ativos e um limite de concorrência de 1.000, o limite de 1.000 é compartilhado entre os três testes combinados — não 1.000 por teste.
{% endhint %}

## Limites de Concorrência por Plano

### Testes com Supervisão Ativada

| Plano | Concorrência Máxima |
|---|---|
| Standard | 1.000 candidatos/minuto |
| Premium | 2.000 candidatos/minuto |
| Elite | 5.000 candidatos/minuto |

### Testes Sem Supervisão

| Plano | Concorrência Máxima |
|---|---|
| Standard | 50 candidatos/minuto |
| Premium | 100 candidatos/minuto |
| Elite | 150 candidatos/minuto |

## Escalonamento Automático

Quando a demanda excede a capacidade do seu plano, o AutoProctor escalona automaticamente a entrada dos candidatos. Os candidatos que excedem o limite veem um botão com uma contagem regressiva de até 60 segundos antes de poderem acessar o teste.


{% hint style="info" %}
Se o seu teste tem uma duração configurada, o AutoProctor ajusta automaticamente o temporizador de cada candidato para compensar os atrasos de escalonamento. Nenhum candidato perde tempo de teste devido aos limites de concorrência.
{% endhint %}

## Usuários do SDK

Se você usa o SDK de JavaScript do AutoProctor no seu próprio site, recebe um limite padrão de 5.000 candidatos por minuto. Quando esse limite é excedido, o SDK retorna uma resposta 429 (Muitas Solicitações). Você deve gerenciar a limitação de taxa de forma independente na sua implementação.

{% hint style="warning" %}
Os usuários do SDK não se beneficiam do escalonamento automático. Você deve construir sua própria lógica de retentativa para lidar com respostas 429 quando o limite de concorrência for excedido.
{% endhint %}

## Como Aumentar Seus Limites

Se você precisa de limites de concorrência mais altos, [entre em contato com a equipe do AutoProctor](pricing-account/support/contact-us.md):

| Tipo de Aumento | Custo Aproximado | Detalhes |
|---|---|---|
| Temporário (evento único) | $500 por incremento de 500 candidatos/minuto | Taxa única |
| Permanente | $2.500/mês por incremento de 500 candidatos/minuto | Compromisso anual obrigatório |

{% hint style="info" %}
A plataforma suporta até um máximo de 25.000 candidatos por minuto.
{% endhint %}

## Recursos Relacionados

- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure a duração do teste e janelas de tempo
- [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) — Detalhes do plano e informações de preços
- [Boas Práticas para Criadores de Testes](understanding/getting-started/best-practices-for-teachers.md) — Dicas para uma administração de testes tranquila
- [Coisas que Você Precisa Saber](understanding/getting-started/things-you-need-to-know.md) — Requisitos essenciais para usar o AutoProctor
- [Fale Conosco](pricing-account/support/contact-us.md) — Entre em contato com a equipe do AutoProctor para aumentos de limite
