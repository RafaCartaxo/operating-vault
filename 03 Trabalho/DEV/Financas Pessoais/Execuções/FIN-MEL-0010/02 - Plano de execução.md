# 02 - Plano de execução (FIN-MEL-0010)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0010 Ação novo lançamento mobile/01 - Demanda|FIN-MEL-0010 — Ação de novo lançamento mobile]]  
> **Plano técnico:** não aplicável  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0010 Ação novo lançamento mobile/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Remover Novo lançamento da barra inferior mobile e apresentar a ação como botão destacado, reutilizando o modal existente.

---

## Vínculo e sequência

- Não há plano técnico separado.
- Remover o item de ação da barra inferior sem remover as áreas de navegação.
- Adicionar/reposicionar botão destacado com safe area e área de toque adequada.
- Reutilizar a mesma função de abertura do modal.
- Validar mobile em diferentes larguras e regressão desktop.

---

## Escopo aprovado

- `src/App.tsx`: composição da navegação e botão de ação.
- `src/styles.css`: posicionamento, safe area, tamanho e sobreposição.
- Permanece intacto: modal, formulário, serviços, API e regras financeiras.

---

## Decisões

- O mobile terá botão de ação separado da barra inferior.
- A barra inferior continuará dedicada a áreas/telas.
- O desktop manterá a ação de cabeçalho já existente.

---

## Pronto quando

- Critério da demanda: [[<DEMANDA>#C1|C1]].
- CTs do pacote QA cobertos e gates do repositório verdes.

### Testes desta etapa

- **Unitários:** serviços e regras isoladas da mudança.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato, persistência e retorno dos dados.
- Registrar os caminhos dos testes previstos e executá-los antes do code review.
