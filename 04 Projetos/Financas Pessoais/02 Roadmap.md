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

- [ ] Criar frontend React.
- [ ] Tornar a interface responsiva para celular.
- [ ] Configurar PWA e instalação na tela inicial.
- [ ] Criar formulário de nova despesa.
- [ ] Validar valores em centavos.
- [ ] Consultar despesas por mês.

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
