# 04 Trabalho DEV

Área de implementação do produto. O QA prepara e valida a demanda; o DEV confirma a solução, planeja, implementa, revisa e entrega as evidências para validação.

## Fluxo DEV

```text
DEV · 01 Análise técnica → DEV · 02 Plano → DEV · 03 Implementação → DEV · 04 Code review → QA · Validação
```

O `status` do card continua representando o ciclo macro no Board. A propriedade `etapa_atual` identifica a etapa detalhada e a camada responsável.

## Organização

| Pasta | Finalidade |
|---|---|
| `Fixes/` | Correções de bugs e defeitos `NXG-NNN` |
| `Execuções/` | Implementação de melhorias `MEL-NNNN` |
| `Planos/` | Índices e vínculos para planos técnicos `PLAN-NNN` |

## Pacote de um fix

```text
Fixes/NXG-NNN/
├── 00 README.md
├── 01 - Análise.md
├── 02 - Plano de correção.md
├── 03 - Implementação.md
└── 04 - Code review.md
```

## Pacote de uma execução

```text
Execuções/MEL-NNNN/
├── 00 README.md
├── 01 - Análise.md
├── 02 - Plano de execução.md
├── 03 - Implementação.md
└── 04 - Code review.md
```

O plano técnico do repositório (`PLAN-NNN`) é referenciado, não duplicado. Os casos de teste e a decisão de validação permanecem no pacote QA.

## Regras de transição

- Bug só entra em `Fixes/` após a causa ser confirmada no código.
- Melhoria só entra em `Execuções/` com escopo, critérios, CTs e plano técnico suficientes.
- `02` congela o plano aprovado; desvios são registrados em `03 - Implementação.md`.
- `04 - Code review.md` registra a decisão e os achados.
- Ao fechar, o card e a pasta de trabalho movem juntos para `05 Arquivo/<ID>/`.

Modelos: [[Templates/Fix/00 README|Fix]] · [[Templates/Execução/00 README|Execução]] · [[Templates/QA/00 README|QA]]
