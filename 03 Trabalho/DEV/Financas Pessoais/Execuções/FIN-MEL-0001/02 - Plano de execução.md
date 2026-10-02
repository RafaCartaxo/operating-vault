# 02 - Plano de execução — FIN-MEL-0001

> [!info]- Navegação
> **Execução:** [[00 README|README da execução]]  
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]

## O quê

Entregar a primeira interface React para cadastrar uma despesa e enviá-la ao backend Go.

## Sequência

1. Criar frontend Vite + React + TypeScript.
2. Configurar tema, tokens e layout responsivo.
3. Criar `services/api.ts`.
4. Criar página e formulário `NovaLancamento`.
5. Validar campos: tipo, descrição, valor e data.
6. Integrar `POST /api/lancamentos`.
7. Implementar estados de carregamento, sucesso e erro.
8. Adicionar testes do formulário e service.
9. Validar desktop e viewport móvel.

## Escopo aprovado

Inclui:

- frontend inicial;
- layout mobile-first;
- formulário de despesa;
- integração com endpoint existente;
- testes básicos;
- atualização da documentação de fluxos.

Não inclui:

- dashboard;
- parcelas automáticas;
- recorrências;
- autenticação;
- PWA instalável completo;
- deploy remoto.

## Pronto quando

- `npm run build` passar.
- Testes do frontend passarem.
- Uma despesa puder ser enviada pelo navegador ao backend.
- A tela for utilizável em viewport de celular.
- `financas-pessoais/docs/fluxos.md` refletir a implementação real.
- O board e este README forem atualizados.
