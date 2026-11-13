# NXG-036 — Plano

Sob lock, identificar imagem já autenticada, recusar pin divergente, criar/revalidar pin persistente e só então remover tag própria; verificar pin depois. Baseline deve verificar saúde, imagem, tar e marker e arquivar pending próprio antes de retornar sucesso. Testar os três caminhos com modelo stateful e falhas sob isolamento verificado; manter falha fechada e evidências em interrupção. Revisar loader e concorrência e documentar reparo histórico sem execução. QA realiza reteste independente.
