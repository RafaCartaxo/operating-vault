# 03 Trabalho QA

Área de qualidade do produto: transformar uma demanda em critérios verificáveis, preparar a cobertura, executar os cenários e registrar a decisão de validação. A nota da demanda é a fonte; o board (`01 Board/BOARD.md`) é apenas a visão de acompanhamento.

## Fluxo QA

```text
entrada → QA · 01 Demanda → QA · 02 Plano de teste → QA · 03 Casos de teste
                                      ↓ entrega ao DEV
                         DEV implementa e revisa
                                      ↓ retorno ao QA
                         QA · 04 Validação
```

### Entrega entre as camadas

- **QA entrega ao DEV:** demanda compreensível, decisões fechadas, escopo, critérios de aceite, plano de teste e casos de teste relacionados.
- **DEV entrega ao QA:** implementação revisada, evidências dos gates e execução DEV vinculada ao card.
- **QA encerra:** executa os CTs, registra resultado/evidência e decide `aprovado`, `reprovado` ou `aprovado com ressalvas`.
- **CT com falha:** cria `NXG-NNN` em `Demandas/Bugs/`, informa `pai: <ID da demanda>` e vincula o bug na coluna **Defeito/Bug** da validação.
- **Validação aprovada:** atualiza os artefatos para concluído e move o pacote completo para `05 Arquivo/<ID>/`.

Cada demanda possui uma pasta própria e um `00 README.md` que resume o status e concentra os links daquela entrega. Os arquivos `01–03` preparam o trabalho; `04 - Validação dev` só é executado após o retorno do DEV. O trabalho técnico de implementação fica em `04 Trabalho DEV`.

## Organização

| Pasta | Finalidade |
|---|---|
| `Demandas/Bugs/` | Bugs e defeitos, com seus casos de teste |
| `Demandas/Melhorias/` | Melhorias e funcionalidades, com o pacote QA completo |
| `Demandas/Planos/` | Planos transversais, backlog, infraestrutura, segurança e decisões |

**Regra de entrada:** bug → `Demandas/Bugs/` · melhoria → `Demandas/Melhorias/` · plano ou decisão → `Demandas/Planos/`.

## Pacote de uma demanda

```text
MEL-NNNN ou NXG-NNN/
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
└── 04 - Validação dev.md
```

Os quatro arquivos não são obrigatórios desde o primeiro dia; eles são criados conforme a demanda avança no fluxo. A pasta e o ID permanecem os mesmos durante todo o ciclo.

**Regra de templates:** cada artefato deve ser copiado do template correspondente e apenas preenchido. Não reconstruir a estrutura manualmente; isso evita divergências e retrabalho.

Modelos: [[Templates/Bug/00 README|Bug]] · [[Templates/Melhoria/00 README|Melhoria]] · [[Templates/QA/00 README|QA]]
