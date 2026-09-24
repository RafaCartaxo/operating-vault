# Demandas de QA

Cada demanda possui sua própria pasta. O `00 README.md` é o índice operacional; o `01` é o card principal e os demais arquivos registram o planejamento, os cenários e a validação, quando aplicáveis.

## Melhorias

```text
Melhorias/MEL-NNNN/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
└── 04 - Validação dev.md
```

## Bugs

```text
Bugs/NXG-NNN/
├── 00 README.md
├── 01 - Bug.md
└── 02 - Casos de teste.md
```

Quando o bug for corrigido, a validação pode ser acrescentada como `03 - Validação <ambiente>.md`, e o fix correspondente fica em `04 Trabalho DEV/Fixes/`.

Planos transversais ficam em `Demandas/Planos/`; não há uma pasta global de planos de teste.

Modelos: [[Templates/Bug/00 README|Bug]] · [[Templates/Melhoria/00 README|Melhoria]] · [[Templates/QA/00 README|QA]].
