# Plano — nova baseline CT-011

1. Preservar delta rastreado e não rastreado; não acessar envs reais.
2. Suprimir URL do schema; implementar verificação sintética de contrato assinado com política e testes negativos, sem apresentá-la como fonte real.
3. Preparar extração segura e harness opt-in para dados sintéticos sem execução real; preservar bloqueios operacionais se não houver fonte autenticada efetiva.
4. Executar testes somente em sandbox com guardas verificadas por PATH, absoluto e subprocessos; revisar e registrar cobertura/limitações por CT.
5. Entregar a QA; ensaio real depende de autorização própria e GitHub real não é presumido.
