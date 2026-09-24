# 03 - Implementação (MEL-0001)

> [!info]- Navegação QA/DEV
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001 — demanda]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; qualquer desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — 🔵 Contrato e persistência inicial

- Adicionados `cep` e `comercio_cep` ao schema PostgreSQL, com migração não destrutiva.
- Propagado `cep` nos tipos de domínio, schemas de create/update, repositório e resposta do cliente.
- Incluído o campo CEP mascarado nos dois blocos do `ClienteForm` e normalização para oito dígitos no payload.
- **Ainda pendente:** consulta automática, preenchimento do endereço, geocoding aproximado, origem GPS/CEP e confirmação para CEP inválido.
- Nenhum desvio do plano registrado.

### Rodada 2 — 🔵 Consulta básica de CEP

- Criado o adapter `frontend/src/shared/utils/cep.ts` para ViaCEP, com normalização, timeout e classificação de erro.
- Conectada a consulta ao campo CEP dos dois blocos do formulário.
- Consulta válida preenche apenas logradouro, bairro, cidade e UF; número e complemento permanecem intactos.
- Falhas de consulta agora exibem confirmação para corrigir ou salvar sem CEP.
- Respostas fora de ordem são ignoradas por controle de sequência por campo.
- O contrato já registra a origem da localização (`gps`/`cep_aproximado`) e a UI distingue a origem quando informada.
- Consulta de CEP agora tenta geocoding aproximado e marca o bloco como `CEP aprox.` quando encontra coordenadas.
- Se o geocoding falhar, o endereço continua utilizável e o GPS manual permanece disponível.
- Criados testes unitários para consulta CEP e geocoding (`cep.test.ts` e `geocoding.test.ts`): 5 testes aprovados.
- Teste do `ClienteForm` cobre preenchimento por CEP sem alterar número/complemento; 14 testes da fatia passaram.
- Testes de create/update do cliente cobrem persistência dos dois CEPs e origem da localização; 2 testes aprovados.
- Revisão documental, TypeScript, testes direcionados e build completo concluídos.
- Code review aprovado; implementação entregue para validação QA.
- TypeScript backend/frontend permanece sem erros.

---

## Evidências

- A registrar durante a implementação: testes, gates, CI e evidências do ambiente.

---

## Verificação

- [ ] CTs da demanda relacionados (fonte QA): [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/03 - Casos de teste|ver casos de teste]].
- [x] TypeScript do backend e frontend sem erros (`npx tsc --noEmit`).
- [ ] Gates aplicáveis do repositório verdes.
- [ ] Documentação sincronizada quando aplicável.
- [ ] Commit registrado no README.
