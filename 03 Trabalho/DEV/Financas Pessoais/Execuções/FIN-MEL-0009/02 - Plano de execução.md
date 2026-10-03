# 02 - Plano de execução (FIN-MEL-0009)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/01 - Demanda|FIN-MEL-0009 — Navegação do lançamento por modal]]  
> **Plano técnico:** não aplicável  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Transformar o Acompanhamento na tela principal e abrir o formulário de lançamento em um modal reutilizando o fluxo atual.

---

## Vínculo e sequência

- Não há plano técnico separado; o escopo está documentado na demanda QA.
- Criar estado de abertura/fechamento do modal.
- Reutilizar o formulário existente sem duplicar regras.
- Implementar apresentação mobile e desktop conforme decisão aprovada.
- Atualizar lista após sucesso e preservar filtros/edição.

Sequência: reorganizar o formulário dentro do `App.tsx` → adicionar modal e backdrop → aplicar layout mobile/desktop → conectar estados de sucesso/erro/submissão → adicionar cobertura de UI/regressão → executar build e testes.

---

## Escopo aprovado

- Frontend: composição da tela principal, botão de adicionar, modal/container e estilos responsivos.
- Permanece intacto: serviços da API, modelo de dados, validações financeiras e comportamento do backend.

---

## Decisões

- Usar um único formulário reutilizado dentro do modal para evitar divergência.
- Usar modal centralizado no desktop e bottom sheet no mobile para adequar o espaço disponível.
- Fechar automaticamente somente após sucesso; em erro, manter o contexto e permitir nova tentativa.

---

## Pronto quando

- Critérios da demanda C1–C10 atendidos.
- CTs do pacote QA cobertos e gates do repositório verdes.

### Testes desta etapa

- **Unitários:** serviços e regras isoladas da mudança.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato, persistência e retorno dos dados.
- Registrar os caminhos dos testes previstos e executá-los antes do code review.

### Arquivos e responsabilidades

| Área | Responsabilidade |
|---|---|
| `src/App.tsx` | Orquestração do estado, abertura/fechamento, foco, submissão e atualização dos registros |
| `src/styles.css` | Apresentação do modal, bottom sheet, backdrop, responsividade e safe area |
| `src/services/lancamentos.ts` | Permanece inalterado; mantém o contrato atual da API |
| `src/components/*` | Reutilização dos campos existentes, sem duplicar validações |
