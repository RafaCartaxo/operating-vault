# 02 - Plano de execução (FIN-MEL-0006)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0006 Navegação estilo aplicativo/01 - Demanda|FIN-MEL-0006 — Navegação estilo aplicativo]]  
> **Plano técnico:** não aplicável; escopo restrito ao frontend.  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0006 Navegação estilo aplicativo/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Navegação inferior responsiva com áreas distintas para Lançamentos e Histórico/Acompanhamento.

---

## Vínculo e sequência

- Revisar a estrutura atual do App.
- Separar navegação e visões sem alterar serviços ou contratos da API.
- Aplicar layout responsivo e estados ativo/acessível.
- Executar testes e build antes do code review.

---

## Escopo aprovado

- Alterar frontend e estilos relacionados à navegação.
- Manter backend, banco, serviços de lançamentos e regras intactos.

---

## Decisões

- Usar estado de área ativa no frontend; não criar rotas ou dependências novas.
- Usar componente de navegação configurável para permitir futuras áreas.

---

## Pronto quando

- Critérios da demanda: FIN-MEL-0006, C1 a C7.
- CTs do pacote QA cobertos e gates do repositório verdes.

### Testes desta etapa

- **Unitários:** serviços e regras isoladas da mudança.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato, persistência e retorno dos dados.
- Registrar os caminhos dos testes previstos e executá-los antes do code review.
