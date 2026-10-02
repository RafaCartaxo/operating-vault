# 04 - Code review — FIN-MEL-0001

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README da execução]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda|FIN-MEL-0001 — Demanda QA]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/04 - Validação dev|Validação QA]]

**Estado:** ✅ aprovado após ajustes finais

---

## Checklist

- [x] O código respeita as convenções reais do repositório.
- [x] O diff está limitado ao escopo aprovado.
- [x] O plano foi seguido; ajustes de parsing e mensagens foram registrados nesta revisão.
- [x] Testes de regressão e gates aplicáveis estão verdes.
- [x] Critérios de aceite e CTs do pacote QA estão cobertos.
- [x] Documentação foi sincronizada quando aplicável.
- [x] Não foram introduzidos segredos, dados sensíveis ou dependências desnecessárias.

---

## Achados

- **Ajustado:** parsing inicial removia todos os pontos e poderia transformar `12.34` em `1234`. A conversão foi isolada em `src/utils/money.ts` e coberta por testes.
- **Ajustado:** a interface permitia `receita`, mas usava textos fixos de despesa. Os títulos e mensagens agora são neutros/dinâmicos.
- **Ajustado após observação de uso:** o campo monetário agora filtra caracteres inválidos e limita a entrada a duas casas decimais; cobertura adicionada em `src/utils/money.test.ts`.
- O refinamento está formalizado no pacote QA como [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/03 - Casos de teste#^ct-005|CT-005]].
- A máscara monetária está formalizada no pacote QA como [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/03 - Casos de teste#^ct-006|CT-006]].
- A preservação do cursor está formalizada no pacote QA como [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/03 - Casos de teste#^ct-007|CT-007]].
- A validação simultânea está formalizada no pacote QA como [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/03 - Casos de teste#^ct-008|CT-008]].

## Evidências

- `npm test`: 12 testes aprovados.
- `npm run build`: aprovado.
- `go test ./...`: backend aprovado.
- Smoke test manual: criação de lançamento via formulário retornou sucesso.

---

## Decisão

- [x] Aprovar
- [ ] Solicitar ajustes

Próximo estágio: QA executar CT-001 a CT-008 no pacote de validação.
