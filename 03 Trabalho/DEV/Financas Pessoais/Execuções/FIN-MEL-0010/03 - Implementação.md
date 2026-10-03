# 03 - Implementação (FIN-MEL-0010)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0010 Ação novo lançamento mobile/01 - Demanda|FIN-MEL-0010 — Ação de novo lançamento mobile]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0010 Ação novo lançamento mobile/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — ✅ concluída (2026-10-03)

- Removido “Novo lançamento” como item da barra inferior mobile.
- Adicionado botão flutuante mobile separado da navegação.
- O botão reutiliza `openNewLancamento` e abre o modal existente.
- O botão respeita safe area, possui área de toque de 56px e fica acima da barra inferior.
- Navegação desktop e ação do cabeçalho permanecem preservadas.

---

## Evidências

- `npm test`: 20 testes aprovados.
- `npm run build`: TypeScript e build Vite aprovados.

---

## Testes da implementação

- [ ] Unitários da regra/serviço alterado.
- [ ] Testes de formulário/UI, quando houver interação — validação manual pendente nos CTs QA.
- [ ] Testes de API/repositório, quando houver contrato ou persistência.
- [ ] Testes de regressão relacionados à demanda.
- [ ] Registrar os caminhos dos arquivos de teste e o comando executado.

---

## Verificação

- [ ] CTs da demanda relacionados (fonte QA): [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0010 Ação novo lançamento mobile/03 - Casos de teste|ver casos de teste]].
- [x] Gates aplicáveis do repositório verdes.
- [x] Documentação sincronizada quando aplicável.
- [ ] Commit registrado no README.
