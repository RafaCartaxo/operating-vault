---
tipo: processo
status: ativo
escopo: operating-vault
---

# Fluxo QA → DEV

Esta página é a referência operacional para qualquer projeto dentro do Operating Vault. O fluxograma Mermaid desta nota é a representação visual e textual oficial; esta nota define o contrato que deve ser seguido.

## Entrada em um chat novo

Quando uma pessoa apresenta uma nova melhoria, bug ou necessidade, a skill `qa-first-delivery` é o ponto de entrada automático. Não é necessário explicar novamente o processo nem chamar a skill manualmente.

Depois do gate QA, o próximo responsável é `$dev-execution`. A troca é determinada pelos artefatos e pelo status da demanda, não por uma palavra-chave específica. Se o gate não estiver pronto, o fluxo permanece em QA.

## Visão geral

```mermaid
flowchart TD
    A[Entrada em chat novo] --> B[qa-first-delivery]
    B --> C[QA · Triagem]
    C --> D[Copiar template oficial]
    D --> E[Critérios de aceite]
    E --> F[CTs + matriz de cobertura]
    F --> G[Executar validador do pacote QA]
    G --> H{Pacote QA íntegro?}
    H -- Não --> C
    H -- Sim --> I[QA_READY_FOR_DEV]
    I --> J[dev-execution]
    J --> K[DEV · Análise]
    K --> L[DEV · Plano congelado]
    L --> M[DEV · Implementação]
    M --> N[Testes técnicos + auditorias]
    N --> O[DEV · Code review]
    O --> P{Escopo preservado?}
    P -- Não --> Q[QA · Reavaliar escopo]
    Q --> C
    P -- Sim --> R[Sincronizar artefatos DEV]
    R --> S{Transição DEV sincronizada?}
    S -- Não --> R
    S -- Sim --> T[DEV_READY_FOR_QA]
    T --> U[qa-first-delivery]
    U --> V[QA · Execução dos CTs]
    V --> W{CTs aprovados?}
    W -- Não --> X[QA_REJECTED · Defeito/ajuste]
    X --> J
    W -- Sim --> Y[Sincronizar artefatos QA]
    Y --> Z{Fechamento sincronizado?}
    Z -- Não --> Y
    Z -- Sim --> AA[QA_APPROVED]
    AA --> AB[Concluído + arquivo]
```

## Responsabilidades

| Etapa | Dono | Entrada | Saída |
|---|---|---|---|
| Triagem e definição | QA | ideia, relato ou necessidade | demanda classificada |
| Critérios e cobertura | QA | demanda | critérios, CTs, matriz e validação preparada |
| Handoff | QA | pacote íntegro e aprovado | demanda pronta para DEV |
| Análise e plano | DEV | pacote QA aprovado | decisão técnica e plano congelado |
| Implementação | DEV | plano | código, testes e documentação |
| Code review | DEV | implementação verificada | execução pronta para sincronização |
| Sincronização DEV | DEV | code review aprovado | README, board, status, links, evidências e handoff coerentes |
| Validação funcional | QA | aplicação + CTs | aprovado, reprovado ou bloqueado |
| Sincronização QA/fechamento | QA + DEV | validação aprovada | boards, roadmap, arquivo, histórico e links sincronizados |

## Regras de passagem

1. A pasta da demanda nasce copiando o template oficial; o template nunca é reconstruído manualmente.
2. Cada critério `C1..Cn` tem pelo menos um CT e cada CT aponta para um critério.
3. Antes do handoff, o QA/`qa-first-delivery` deve executar `python3 scripts/validar_pacote_qa.py <pasta-da-demanda>`; saída diferente de sucesso bloqueia o gate. Registrar o resultado resumido no `00 README.md` da demanda e manter a saída detalhada como evidência da execução.
4. A execução DEV só nasce depois do gate QA; a pasta é criada copiando `Templates/Execução/`.
5. O DEV não altera o contrato funcional para acomodar a implementação. Mudança de comportamento retorna para QA.
6. Build verde e testes técnicos verdes não equivalem à aprovação funcional dos CTs.
7. Toda transição atualiza frontmatter, README, board, roadmap e links relacionados.
8. A sincronização documental é um gate: sem checklist concluído e coerência verificada, não se emite `DEV_READY_FOR_QA` nem `QA_APPROVED`.
9. Falha de CT em DEV gera defeito/ajuste vinculado; não se apaga nem se reescreve o histórico da demanda pai.

## Verificação de sincronização documental

Antes de cada handoff ou fechamento, o responsável deve conferir:

- frontmatter e etapa atual da demanda e da execução;
- README e status atual;
- board da camada correspondente;
- links QA ↔ DEV, CTs, validação, evidências e épico/roadmap;
- histórico, pendências, datas e resultado dos gates;
- ausência de instruções ou placeholders obsoletos;
- checklist de transição marcado somente após a conferência.

Se qualquer item estiver divergente, registrar a pendência e manter a demanda na etapa atual. A implementação pode estar tecnicamente pronta, mas a transição não está concluída.

## Artefatos por etapa

### QA

- `03 Trabalho/QA/<projeto>/Demandas/<tipo>/<ID>/00 README.md`
- `01 - Demanda.md`
- `02 - Plano de teste.md`
- `03 - Casos de teste.md`
- `04 - Validação dev.md`
- `05 - Preparação Qase.md`, quando aplicável

### DEV

- `03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README.md`
- `01 - Análise.md`
- `02 - Plano de execução.md`
- `03 - Implementação.md`
- `04 - Code review.md`

## Fluxo entre pessoas e sistema

```mermaid
flowchart TD
    A[Pessoa / Produto] --> B[qa-first-delivery]
    B --> C[Operating Vault · demanda + critérios + CTs]
    C --> D{QA_READY_FOR_DEV?}
    D -- Não --> B
    D -- Sim --> E[dev-execution]
    E --> F[Repositório / Aplicação · análise + implementação]
    F --> G[Testes técnicos + code review]
    G --> H[Sincronização documental DEV]
    H --> I{DEV_READY_FOR_QA?}
    I -- Não --> E
    I -- Sim --> J[qa-first-delivery · validação]
    J --> K[Aplicação · execução dos CTs]
    K --> L{CTs aprovados?}
    L -- Não --> M[QA_REJECTED · defeito/ajuste]
    M --> E
    L -- Sim --> N[Sincronização documental QA]
    N --> O{QA_APPROVED?}
    O -- Não --> J
    O -- Sim --> P[boards + roadmap + fechamento]
```

## Skills associadas

- `$qa-first-delivery`: organiza a entrada, instancia templates, define critérios e CTs e conduz o gate QA.
- `$dev-execution`: executa o pacote aprovado, registra evidências e devolve a demanda para QA.

As skills são reutilizáveis em outros projetos; os caminhos concretos de templates, boards e IDs continuam sendo definidos pelo vault do projeto.

O usuário não precisa escolher a skill seguinte: a etapa atual define o próximo responsável. A chamada explícita das skills continua disponível, mas é opcional.
