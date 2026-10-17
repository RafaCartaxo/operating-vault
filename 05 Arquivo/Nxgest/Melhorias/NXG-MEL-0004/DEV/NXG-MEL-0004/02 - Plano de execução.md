# 02 - Plano de execução (NXG-MEL-0004)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0004/QA/NXG-MEL-0004 README e mapa da raiz/01 - Demanda|NXG-MEL-0004 — README e mapa da raiz]]  
> **Plano técnico:** [[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0004/QA/NXG-MEL-0004 README e mapa da raiz/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Atualizar o mapa estrutural do README raiz para refletir a estrutura real do repositório.

---

## Vínculo e sequência

- Plano de governança: [[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]].
- Revisar README, atualizar o mapa, executar auditorias e revisar o diff.

---

## Escopo aprovado

- Pode mudar: README.md do repositório NX Gest, somente a seção de estrutura.
- Deve permanecer intacto: código, `.env`, Docker, agentes, scripts, branches, produção e os 36 arquivos de trabalho aberto.

---

## Decisões

- Fazer um lote documental isolado antes de qualquer movimentação para `infra/`.

---

## Pronto quando

- Critérios da demanda: C1–C4 em [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0004/QA/NXG-MEL-0004 README e mapa da raiz/01 - Demanda|NXG-MEL-0004]].
- CTs do pacote QA cobertos e gates do repositório verdes.

### Testes desta etapa

- **Documentação:** auditoria de estrutura, links e nomenclatura.
- **Regressão:** confirmar que somente a documentação autorizada foi alterada.
- Registrar evidências antes do code review.
