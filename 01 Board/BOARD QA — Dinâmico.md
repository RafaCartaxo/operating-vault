# Board QA — Visão dinâmica

> Esta visão é alimentada pelo `status` do `00 README.md` de cada demanda ativa em todos os projetos. Cards concluídos ficam em [[05 Arquivo/00 README|05 Arquivo]] e permanecem acessíveis pelo histórico.

```dataviewjs
const colunas = [
  ["backlog", "📥 Backlog"],
  ["analise", "🔍 Em análise"],
  ["execucao", "⚙️ Em execução"],
  ["validacao", "🧪 Em validação"],
  ["concluido", "✅ Concluído"],
];
const cards = dv.pages()
  .where((pagina) => pagina.file.name === "00 README" && String(pagina.file.folder).includes("/03 Trabalho/QA/") && String(pagina.file.folder).includes("/Demandas/"));
const board = dv.el("div", "", { attr: { style: "display:flex;flex-direction:row;gap:12px;align-items:flex-start;width:100%;overflow-x:auto;padding-bottom:12px;" } });

for (const [status, titulo] of colunas) {
  const coluna = board.createEl("section", { attr: { style: "flex:0 0 210px;min-height:130px;padding:10px;border:1px solid var(--background-modifier-border);border-radius:8px;background:var(--background-secondary);" } });
  coluna.createEl("h3", { text: titulo, attr: { style: "margin:0 0 10px;font-size:0.95em;white-space:normal;" } });
  const itens = cards.where((pagina) => String(pagina.status ?? "") === status).sort((pagina) => pagina.file.name).array();
  if (!itens.length) {
    coluna.createEl("p", { text: "Nenhum card", attr: { style: "margin:0;color:var(--text-muted);font-size:0.85em;" } });
    continue;
  }
  for (const pagina of itens) {
    const card = coluna.createEl("div", { attr: { style: "margin:0 0 8px;padding:9px;background:var(--background-primary);border:1px solid var(--background-modifier-border);border-radius:6px;" } });
    const nomeCard = String(pagina.file.folder).split("/").pop() || pagina.file.name;
    const caminhoCard = pagina.file.path;
    const link = card.createEl("a", { text: nomeCard, cls: "internal-link", attr: { href: caminhoCard, "data-href": caminhoCard } });
    link.addEventListener("click", (evento) => {
      evento.preventDefault();
      app.workspace.openLinkText(caminhoCard, "", false);
    });
    if (pagina.etapa_atual) card.createEl("div", { text: String(pagina.etapa_atual), attr: { style: "margin-top:5px;color:var(--text-muted);font-size:0.78em;" } });
  }
}
```
