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
- [ ] Configurar PWA e instalação na tela inicial.
- [x] Criar formulário de nova despesa.
- [x] Validar valores em centavos.
- [x] Consultar despesas por mês.

### Melhoria concluída

**FIN-MEL-0002 — Consultar lançamentos do mês**

Usar `GET /api/lancamentos?mes=AAAA-MM` para exibir os lançamentos do mês na aplicação, com totalizadores simples e estados de carregamento, vazio e erro. Esta etapa fecha o primeiro ciclo de uso antes de avançar para PWA, parcelas ou recorrências.

### Próxima melhoria recomendada

**FIN-MEL-0003 — Editar e excluir lançamentos**

Permitir corrigir ou remover registros já persistidos, preservando validações, confirmação de exclusão e consistência da lista mensal.

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
