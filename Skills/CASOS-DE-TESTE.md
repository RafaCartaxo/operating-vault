# Skill: Criação de Casos de Teste (NX Gest)

Criar e organizar casos de teste no padrão do vault. Adaptado do `brainwork` (SKILL_CASOS_DE_TESTE). Um único formato em todo o vault — o que muda é a numeração.

Os casos vivem em uma nota própria dentro da pasta da demanda (`03 - Casos de teste.md`). A demanda mantém os critérios de aceite e links para os artefatos.

## Regra de criação

O CT deve nascer a partir de `Templates/QA/03 - Casos de teste.md`: copie o template para a pasta da demanda e substitua apenas os placeholders, títulos, critérios e dados do cenário. Não recrie a estrutura manualmente nem remova campos do padrão sem registrar uma decisão.

Antes de entregar o pacote, conferir:

- [ ] Nota criada no caminho e nome esperados.
- [ ] Frontmatter preservado e links atualizados.
- [ ] Cada CT é um callout recolhível com âncora única.
- [ ] Descrição, pré-condições, Dado/Quando/Então, resultado e critérios preenchidos.
- [ ] Informações técnicas do CT mantidas.
- [ ] Evidências deixadas para a nota de validação.

## Estrutura padrão

Formato único do vault: cada CT é um callout independente na nota `03 - Casos de teste.md`:

```markdown
> [!example]- CT-001 · Nome claro do cenário
>
> ## Cenário
>
> **Descrição:** explique em uma frase o que este caso confirma.
>
> **Pré-condições:**
> - Informe o que precisa estar preparado antes do teste.
>
> **Dado** que ...
> **Quando** ...
> **Então** ...
>
> **Resultado esperado:** descreva o comportamento observado em linguagem direta.
> **Pós-condição:** registre como o sistema deve ficar depois do teste.
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
> **Tipo:** funcional
> **Camada:** API | E2E | manual
> **Automação:** smoke-api | Playwright | manual
> **Execução:** planejado

^ct-001
```

**Cada CT é um callout identificável** (`> [!example]- ... ^ct-001`), não um item de lista — dobra/desdobra e é linkável (`[[nota#^ct-001]]`).

Na validação, a tabela aponta para esse bloco por `^ct-nnn`. O **Page Preview** do Obsidian mostra o callout completo no hover; o Dataview fica reservado para resumos e painéis, não para substituir a leitura/execução do cenário.

| Elemento | Regra |
|---|---|
| Bloco | `> [!example]- CT-NNN Título ^ct-nnn` em nota própria; o callout pode ser recolhido e pré-visualizado por link |
| Palavra-chave | `**Dado**` / `**E**` / `**Quando**` / `**Então**` em negrito, uma por linha, sem bullet |
| Execução | `**Execução:** planejado / em execução / passou / falhou / bloqueado` |
| Evidências | Registradas somente na nota de validação, nunca dentro do CT |
| Separador | `---` entre CTs |

## Numeração

- Nota `03 - Casos de teste.md` da demanda: `CT-001`, `CT-002`... sequencial.
- Nota `02 - Casos de teste.md` de um bug: `CT-B01`, `CT-B02`... (prefixo B).
- CTs da melhoria: `CT-001..` em `03 - Casos de teste.md`, na pasta da demanda.

## Escrita

- Descrever claramente o cenário validado (título acionável).
- 1 cenário por CT; linguagem clara, sem excesso técnico.
- Cobertura: sempre avaliar o caso feliz, bordas/validação e o caminho do erro.
