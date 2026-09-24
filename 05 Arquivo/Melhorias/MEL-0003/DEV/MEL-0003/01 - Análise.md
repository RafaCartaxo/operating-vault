# 01 - Análise (MEL-0003)

> [!info]- Navegação QA/DEV
> **Execução:** [[05 Arquivo/Melhorias/MEL-0003/DEV/MEL-0003/00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/01 - Demanda|MEL-0003 — Expandir e recolher com chevron]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/04 - Validação dev|Validação QA]]

---

## Veredito

Melhoria viável e localizada: `ClienteForm` já controla os dois estados; basta trocar o texto visual por ícones Lucide, preservando `aria-expanded` e o clique.

---

## O que foi confirmado

- `frontend/src/modules/cliente/components/ClienteForm.tsx` mantém `enderecoComercioAberto` e `enderecoPrincipalAberto`.
- Os dois botões usam `aria-expanded` e alternam o estado com `setEndereco*Aberto`.
- O texto atual (`Expandir`/`Recolher`) aparece nos dois controles e é o único ponto visual a ser refinado.
- `ClienteForm.test.tsx` já valida os estados iniciais; deve passar a validar também a presença/estado do chevron.

---

## Abordagem e riscos

- Usar `ChevronRight` recolhido e `ChevronDown` expandido, seguindo os ícones já adotados no projeto.
- Manter um nome acessível no botão (texto visual oculto ou `aria-label`) e `aria-expanded`.
- Não alterar estado inicial, conteúdo das seções, API ou persistência.

---

## Alternativas descartadas

- Manter texto por extenso: descartado porque é o problema visual da melhoria.
- Criar componente novo: desnecessário para dois controles locais e aumentaria o escopo.

---

## Perguntas abertas

- Nenhuma. Se houver decisão que altere escopo, regra ou aceite, voltar o card para análise.
