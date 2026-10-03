# 02 - Plano de execução (FIN-MEL-0008)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|README da execução]]  
> **Demanda QA:** [[<DEMANDA>|<ID> — <título da demanda>]]  
> **Plano técnico:** [[03 Trabalho/DEV/<projeto>/Planos/PLAN-NNN|PLAN-NNN]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[<VALIDACAO>|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Fluxo completo para criar, consultar, editar e excluir séries parceladas.

---

## Vínculo e sequência

- Adicionar identificador de série e migração compatível.
- Implementar criação transacional e cálculo de datas/centavos.
- Expor edição/exclusão da série.
- Adicionar campos e apresentação no React.
- Cobrir backend e frontend com testes.

---

## Escopo aprovado

- Backend Go: modelo, repositório, handler e migration.
- Frontend React: tipos, serviço, formulário e histórico.
- Preservar lançamentos simples e API existente.

---

## Decisões

- Persistir cada parcela como lançamento individual para manter a consulta mensal existente.
- Usar um identificador de série para operações em lote.
- Usar transação no backend para evitar séries parciais.

---

## Pronto quando

- Critério da demanda: [[<DEMANDA>#C1|C1]].
- CTs do pacote QA cobertos e gates do repositório verdes.

### Testes desta etapa

- **Unitários:** serviços e regras isoladas da mudança.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato, persistência e retorno dos dados.
- Registrar os caminhos dos testes previstos e executá-los antes do code review.
