# 02 - Plano de execução — FIN-MEL-0001

> [!info]- Navegação QA/DEV
> **README do card:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda|FIN-MEL-0001 — Cadastro mobile de nova despesa]]  
> **Plano técnico:** a definir após aprovação deste plano  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em `03 - Implementação.md`.

---

## O quê

Entregar a primeira interface React mobile-first para cadastrar uma despesa e enviá-la ao backend Go, preservando o contrato documentado e os CTs da demanda QA.

---

## Vínculo e sequência

- Plano técnico: será vinculado quando o plano de implementação for criado no repositório.
- Criar ou confirmar o frontend Vite + React + TypeScript.
- Criar a camada de serviço HTTP da API.
- Criar a página e o formulário de nova despesa.
- Implementar validação, conversão monetária e estados de envio.
- Executar testes e validar desktop/mobile antes do code review.

---

## Escopo aprovado

- Frontend inicial.
- Página dedicada mobile-first.
- Campos `tipo`, `descricao`, `valor` e `data`.
- Conversão do valor para `valorCentavos`.
- Integração com `POST /api/lancamentos`.
- Estados de carregamento, sucesso e erro.
- Testes básicos e atualização da documentação técnica.

Permanece intacto:

- backend Go e contrato existente;
- persistência SQLite;
- fluxos de GET, dashboard, parcelas, recorrências, autenticação e deploy remoto.

---

## Decisões

- Usar React + TypeScript + Vite, reaproveitando o stack conhecido.
- Manter chamadas HTTP em um service da API.
- Usar página dedicada em vez de modal para facilitar acesso por URL no celular.
- Manter regras definitivas no backend Go.
- Não incluir parcelamento, recorrência ou dashboard nesta entrega.

---

## Pronto quando

- Critérios da demanda [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda#^c1|C1]] a [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda#^c6|C6]] estiverem cobertos.
- [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/03 - Casos de teste|CT-001 a CT-008]] estiverem cobertos pelos testes e pela validação QA.
- `npm run build` passar.
- Testes do frontend passarem.
- Uma despesa puder ser enviada pelo navegador ao backend.
- A tela for utilizável em viewport móvel e desktop.
- `financas-pessoais/docs/fluxos.md` refletir a implementação real.
- Gates aplicáveis e code review estiverem verdes.

### Testes desta etapa

- **Unitários:** conversão monetária e regras de validação isoladas.
- **Formulário/UI:** interação, estados, mensagens e regressões visuais.
- **API/repositório:** contrato e persistência existentes continuam verdes.
- Registrar os caminhos dos testes e os comandos executados antes do code review.
