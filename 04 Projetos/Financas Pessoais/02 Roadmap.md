---
projeto: financas-pessoais
tipo: roadmap
---

# Roadmap

## Fase 1 — Fundamento

- [x] Criar módulo Go com SQLite.
- [x] Criar tabela de lançamentos.
- [x] Implementar `POST /api/lancamentos`.
- [x] Implementar `GET /api/lancamentos?mes=AAAA-MM`.
- [x] Adicionar testes básicos.

## Fase 2 — Entrada rápida

- [x] Criar frontend React.
- [x] Tornar a interface responsiva para celular.
- [x] Configurar PWA e instalação na tela inicial.
- [x] Criar formulário de nova despesa.
- [x] Validar valores em centavos.
- [x] Consultar despesas por mês.

### Melhoria concluída

**FIN-MEL-0002 — Consultar lançamentos do mês**

Usar `GET /api/lancamentos?mes=AAAA-MM` para exibir os lançamentos do mês na aplicação, com totalizadores simples e estados de carregamento, vazio e erro. Esta etapa fecha o primeiro ciclo de uso antes de avançar para PWA, parcelas ou recorrências.

### Melhoria concluída

**FIN-MEL-0003 — Editar e excluir lançamentos**

Permitir corrigir ou remover registros já persistidos, preservando validações, confirmação de exclusão e consistência da lista mensal.

### Ajuste responsivo em análise

**FIN-MEL-0004 — Refinamentos responsivos dos campos**

Validar data, filtro mensal e máscara monetária em iPhone, Android e desktop.

### Melhorias concluídas

**FIN-MEL-0005 — Resumo mensal financeiro**

Exibir receitas, despesas, saldo e quantidade de lançamentos no período consultado, sem alterar o cadastro. Implementação frontend, code review e validação dos 16 CTs concluídos.

**FIN-MEL-0006 — Navegação estilo aplicativo**

Implementação frontend concluída, code review aprovado e todos os 6 CTs aprovados em QA.

**FIN-MEL-0007 — PWA instalável**

Manifest, ícones, service worker e cache do app shell implementados; validação técnica concluída.

## Fase 3 — Cálculos

- [ ] Parcelas.
- [ ] Recorrências.
- [ ] Contas fixas.
- [ ] Faturas.

## Fase 4 — Integração

- [ ] Importar o planejamento existente.
- [ ] Exportar painel e meses para o `financas-vault`.
- [ ] Criar rotina de backup.
- [ ] Publicar homologação com URL HTTPS.
- [ ] Publicar produção com autenticação e banco persistente.
