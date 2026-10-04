# 02 - Plano de execução — FIN-MEL-0012

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/01 - Demanda|FIN-MEL-0012 — Recorrências mensais sem duplicidade]]  
> **Plano técnico:** ainda não criado — decisão de produto pendente.  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Resultado: regras recorrentes mensais persistidas e geradas de forma idempotente, com gestão no frontend, integração ao acompanhamento mensal e exclusão explícita das ocorrências marcadas como incluídas em fatura no cálculo do saldo.

---

## Vínculo e sequência

- Dependência: decisão de produto sobre C5 e atualização do CT-008 para a marcação explícita de inclusão em fatura.

---

## Escopo aprovado

- Backend: novo domínio/endpoints de recorrências, migration própria e extensão do retorno mensal.
- Frontend: tipos, services, validação, tela/formulário de recorrências e resumo/lista mensal.
- Documentação: API, modelo de dados e fluxos Mermaid.

---

## Decisões

- Recorrências ficam em entidade própria; ocorrências entram no fluxo mensal de `lancamentos`.
- A unicidade será garantida por regra + competência no banco, não por deduplicação no frontend.
- A regra de inclusão em fatura será explícita; não haverá heurística por valor, data ou descrição.

---

## Pronto quando

- C5 e CT-008 revisados e aprovados pelo QA.
- Migration aplicada em banco novo e banco existente.
- APIs e UI cobrem cadastro, geração, edição, encerramento, controle de fatura e validações.
- Testes técnicos verdes e 10 CTs disponíveis para execução funcional.

### Testes desta etapa

- **Unitários:** serviços e regras isoladas da mudança.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato, persistência e retorno dos dados.
- Registrar os caminhos dos testes previstos e executá-los antes do code review.
