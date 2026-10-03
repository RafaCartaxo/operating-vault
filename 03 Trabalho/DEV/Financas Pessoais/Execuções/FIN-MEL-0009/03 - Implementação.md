# 03 - Implementação (FIN-MEL-0009)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/01 - Demanda|FIN-MEL-0009 — Navegação do lançamento por modal]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — ✅ concluída (2026-10-03)

- A tela principal passou a ser o Acompanhamento.
- O formulário existente passou a ser aberto em modal, sem duplicar campos ou regras.
- No desktop, o modal é centralizado; no mobile, funciona como bottom sheet com rolagem interna.
- Adicionados botão de novo lançamento no cabeçalho desktop e ação de novo lançamento na navegação mobile.
- Implementados fechamento, cancelamento, backdrop, tecla Escape e bloqueio de fechamento durante salvamento.
- Edição de lançamentos existentes passou a abrir o mesmo modal.
- Serviços da API e backend permaneceram inalterados.

---

## Evidências

- `npm test`: 20 testes aprovados.
- `npm run build`: TypeScript e build Vite aprovados.

---

## Testes da implementação

- [x] Unitários da regra/serviço alterado — não aplicável, sem alteração de regra/API.
- [ ] Testes de formulário/UI, quando houver interação — validação manual pendente nos CTs QA.
- [x] Testes de API/repositório, quando houver contrato ou persistência — não aplicável, contrato inalterado.
- [x] Testes de regressão relacionados à demanda — build e suíte existente aprovados.
- [x] Registrar os caminhos dos arquivos de teste e o comando executado.

---

## Verificação

- [ ] CTs da demanda relacionados (fonte QA): [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/03 - Casos de teste|ver casos de teste]].
- [x] Gates aplicáveis do repositório verdes.
- [x] Documentação sincronizada quando aplicável.
- [ ] Commit registrado no README.
