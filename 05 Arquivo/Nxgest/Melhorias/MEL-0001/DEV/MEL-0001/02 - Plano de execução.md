# 02 - Plano de execução (MEL-0001)

> [!info]- Navegação QA/DEV
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001 — demanda]]  
> **Plano técnico:** `docs/plans/PLAN-089-cliente-cep-localizacao-aproximada.md`  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Adicionar consulta de CEP aos endereços pessoal e comercial, preencher os dados retornados e oferecer localização aproximada, mantendo o GPS manual como origem exata e prioritária.

---

## Vínculo e sequência

- Plano detalhado: `docs/plans/PLAN-089-cliente-cep-localizacao-aproximada.md`.
- Sequência: contrato/banco/API → adapter de CEP e geocoding → formulário e indicadores → navegação → testes e documentação.
- A validação QA só começa depois de implementação, review e gates verdes.

---

## Escopo aprovado

- Adicionar e persistir CEP nos dois blocos de endereço.
- Consultar CEP válido com debounce/timeout e proteger contra respostas fora de ordem.
- Preencher logradouro, bairro, cidade e UF sem alterar número/complemento.
- Diferenciar GPS manual de localização aproximada pelo CEP, inclusive na edição.
- Invalidar somente a localização aproximada quando CEP/texto relevante mudar.
- Manter salvamento sem CEP, prioridade de navegação e captura manual existentes.

Fora de escopo: CEP obrigatório, validação do número do imóvel, localização exata, histórico de consultas e mudança da regra comércio → endereço pessoal.

---

## Decisões

- O provedor de CEP será encapsulado em adapter substituível; a escolha final deve respeitar timeout, limites e política de acesso.
- Geocoding é etapa separada: se falhar, o endereço continua utilizável e o GPS manual permanece disponível.
- A origem (`gps` ou `cep_aproximado`) deve acompanhar as coordenadas para renderização e navegação coerentes.
- Falha de consulta oferece “Corrigir” ou “Salvar sem CEP”, sem apagar texto manual.

---

## Pronto quando

- Critérios da demanda [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda#^c1|C1]] a [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda#^c10|C10]] cobertos.
- CTs do pacote QA executáveis, documentação sincronizada e gates do repositório verdes.
- `03 - Implementação.md` e `04 - Code review.md` registrados antes da entrega para validação QA.

### Testes desta etapa

- **Unitário do serviço:** `frontend/src/shared/utils/cep.test.ts` — normalização, CEP inválido, não encontrado, indisponibilidade e timeout.
- **Unitário de geocoding:** `frontend/src/shared/utils/geocoding.test.ts` — resultado válido, ausência de resultado e falha do provedor.
- **Formulário:** `frontend/src/modules/cliente/components/ClienteForm.test.tsx` — preenchimento sem sobrescrever número/complemento, resposta obsoleta, erro e origem `CEP aprox.`.
- **API/repositório:** cenários de create/update em `src/modules/cliente` — persistência e retorno de `cep` nos dois endereços.
