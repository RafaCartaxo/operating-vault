---
demanda: FIN-MEL-0011
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — FIN-MEL-0011

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** ainda não criada — aguarda aprovação do pacote QA.

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar a distribuição automática, a centralização e a acessibilidade dos destinos da navbar mobile, garantindo a separação da ação flutuante de Novo lançamento.

---

## Riscos e escopo

- **Escopo:** navbar mobile, ícone de Acompanhamento, distribuição de 1 a 5 itens e regressão da ação flutuante/desktop.
- **Riscos:** item desalinhado, espaçamento desigual, texto ainda ocupando a barra, ícone sem nome acessível e ação flutuante confundida com navegação.

---

## Estratégia de teste

- **Unitário:** regras e serviços isolados.
- **API/repositório:** contrato, validações e persistência.
- **UI/E2E:** comportamento do usuário e integração entre campos/telas.
- **Regressão:** fluxos existentes afetados pela mudança.

Defina apenas as camadas aplicáveis; não crie testes por obrigação quando não houver risco naquela camada.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Regressão | UI/API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Responsividade | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Responsividade | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Acessibilidade | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Regressão | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Exemplo: replique a linha para cada CT do pacote. O link do CT abre a prévia do cenário; o link de Validação leva à tabela onde o resultado e a evidência são registrados.

---

## Entrada e saída

**Entrada:** build com FIN-MEL-0010 disponível, viewport mobile/desktop e dados de navegação.  
**Saída:** 5 CTs executados com evidências e decisão QA registrada.
