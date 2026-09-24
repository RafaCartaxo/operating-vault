# Escala de esforço (pontos)

O campo `pontos` registra o esforço estimado da passagem pelo card. Não é tempo cronometrado. O card pode nascer sem pontuação, mas deve receber um valor antes de sair da triagem; o valor pode ser ajustado ao fechar a etapa.

A escala usa a progressão Fibonacci calibrada em unidades de 10: `0, 10, 20, 30, 50, 80...`.

| Pontos | Faixa de referência |
|---:|---|
| 0 | < 0,5h |
| 10 | < 2h |
| 20 | < 4h |
| 30 | < 8h |
| 50 | < 2 dias |
| 80 | < 3 dias |
| 130 | < 4 dias |
| 210 | < 5 dias |
| 340 | < 7 dias |
| 550 | < 10 dias |
| 890 | < 15 dias |
| 1440 | < 30 dias |

A faixa é apenas uma referência para calibrar a estimativa. A fonte de verdade é o valor em `pontos`.

## Total automático

Cada artefato de uma etapa pode ter seu próprio `pontos`. Os READMEs de QA, Execução e Fix exibem automaticamente a soma dos valores numéricos encontrados na própria pasta usando Dataview. Não preencher um campo de total manualmente: o total exibido é derivado dos pontos das etapas.

No card, preencher apenas `pontos_alocados` para registrar a capacidade reservada ao ciclo. O esforço necessário é sempre a soma automática dos `pontos` das etapas; não existe um segundo campo manual para esse total.

Na validação, o andamento é derivado de `ct_resultados`; a etapa só é considerada entregue quando `resultado` estiver aprovado. O resultado de cada CT continua sendo a fonte para aprovação, falha ou bloqueio individual.

Enquanto a validação estiver parcial, os pontos entregues são proporcionais aos CTs aprovados: `pontos da etapa × CTs aprovados ÷ CTs totais`. O valor é exibido como progresso, sem alterar a estimativa original da etapa.
