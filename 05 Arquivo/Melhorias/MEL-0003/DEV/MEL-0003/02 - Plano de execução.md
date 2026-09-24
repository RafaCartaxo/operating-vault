# 02 - Plano de execução (MEL-0003)

> [!info]- Navegação QA/DEV
> **Execução:** [[05 Arquivo/Melhorias/MEL-0003/DEV/MEL-0003/00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/01 - Demanda|MEL-0003 — Expandir e recolher com chevron]]  
> **Plano técnico:** Plano técnico: a definir  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Substituir `Expandir`/`Recolher` por chevrons nos controles de endereço pessoal e endereço do comércio, mantendo a acessibilidade e o comportamento atual.

---

## Vínculo e sequência

- Plano detalhado: Plano técnico a definir (quando aplicável).
- Atualizar os imports de ícones do `ClienteForm`.
- Renderizar `ChevronRight` quando recolhido e `ChevronDown` quando expandido.
- Preservar nome acessível, `aria-expanded` e alternância por clique/teclado.
- Atualizar os testes do formulário para cobrir os dois estados.

---

## Escopo aprovado

- Alterar `frontend/src/modules/cliente/components/ClienteForm.tsx` e seu teste.
- Manter intactos os estados iniciais, campos, conteúdo, API e persistência.

---

## Decisões

- Usar `ChevronRight`/`ChevronDown` de `lucide-react`, sem dependência nova.

---

## Pronto quando

- Critérios da demanda: [[05 Arquivo/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/01 - Demanda#^c1|C1]] a [[05 Arquivo/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/01 - Demanda#^c4|C4]].
- CTs do pacote QA cobertos e gates do repositório verdes.

### Testes desta etapa

- **Unitários:** serviços e regras isoladas da mudança.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato, persistência e retorno dos dados.
- Registrar os caminhos dos testes previstos e executá-los antes do code review.
