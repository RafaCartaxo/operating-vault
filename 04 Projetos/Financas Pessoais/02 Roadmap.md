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

### Melhoria concluída

**FIN-MEL-0004 — Refinamentos responsivos dos campos**

Validar data, filtro mensal e máscara monetária em iPhone, Android e desktop.

### Melhorias concluídas

**FIN-MEL-0005 — Resumo mensal financeiro**

Exibir receitas, despesas, saldo e quantidade de lançamentos no período consultado, sem alterar o cadastro. Implementação frontend, code review e validação dos 16 CTs concluídos.

**FIN-MEL-0006 — Navegação estilo aplicativo**

Implementação frontend concluída, code review aprovado e todos os 6 CTs aprovados em QA.

**FIN-MEL-0007 — PWA instalável**

Manifest, ícones, service worker e cache do app shell implementados; validação técnica concluída.

### Melhoria concluída

**FIN-MEL-0009 — Navegação do lançamento por modal**

Evoluir a navegação entregue na FIN-MEL-0006: o Acompanhamento será a tela principal e o cadastro de despesa/receita será aberto por uma ação rápida em modal, preservando o formulário, validações, filtros e comportamento responsivo. Implementação, code review e validação concluídos.

## Fase 3 — Cálculos

### Épico em execução

**[[Epicos/FIN-EPIC-0001 Evolução lançamentos mobile/00 README|FIN-EPIC-0001 — Evolução da experiência de lançamentos mobile]]** reúne a sequência `FIN-MEL-0009 → FIN-MEL-0010 → FIN-MEL-0011`. As três demandas estão concluídas.

- [x] Parcelas — FIN-MEL-0008 concluído com 8 CTs aprovados.
- [x] Navegação do lançamento por modal — FIN-MEL-0009 concluído com 10 CTs aprovados.
- [x] Ação de novo lançamento mobile — FIN-MEL-0010 concluído com 5 CTs aprovados.
- [x] Organização da navbar mobile — FIN-MEL-0011 concluído com 5 CTs aprovados.
- [ ] Recorrências — FIN-MEL-0012 em triagem QA.
- [ ] Contas fixas.
- [ ] Faturas.

## Fase 4 — Integração

- [ ] Importar o planejamento existente.
- [ ] Exportar painel e meses para o `financas-vault`.
- [ ] Criar rotina de backup.
- [ ] Publicar homologação com URL HTTPS.
- [ ] Publicar produção com autenticação e banco persistente.
