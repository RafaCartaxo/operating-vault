# NXG-036 — Análise

A remoção da última tag de imagem em uso pode falhar, e a baseline retorna sucesso deixando pending. Os três caminhos atingidos são `scripts/deploy-staging.sh`, `scripts/staging-adoption-execute.sh` e `scripts/initial-baseline.sh`; o loader rejeita tag temporária preexistente. O lock 9 serializa participantes cooperativos, não protege de alterações externas ao contrato. O estado histórico é evidência privada e não será manipulado nesta tarefa.
