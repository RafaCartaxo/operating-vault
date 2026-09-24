---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "QA · Encerramento"
modulo: cliente
plano: PLAN-088
execucao: "[[05 Arquivo/Nxgest/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]"
ambiente: dev
origem: observado
projeto: nxgest
pai: ""
data_inicio: "2026-08-29"
data_fim: "2026-09-11"
responsavel: ""
pontos_alocados: 70
---
# MEL-0002 — Cliente: documento alternativo abaixo do CPF

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** executar os casos em [[03 - Casos de teste]] e registrar as evidências em [[04 - Validação dev]].

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** `pontos_alocados` (atualmente 70 pontos).
>
> ```dataviewjs
> const id = (dv.current().file.path.match(/MEL-\d+/) || [""])[0];
> const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
> const lista = paginas.sort(p => p.file.name);
> const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> const alocado = Number(dv.current().pontos_alocados || 0);
> const diferenca = alocado - necessario;
> dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço necessário:** ${necessario} pontos · **Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> ```

> **Entrega desta capacidade:** a demanda completa da MEL-0002, conforme o escopo e os critérios de aceite registrados abaixo.

## Problema / contexto

Em atendimentos de campo, nem sempre o CPF do cliente está disponível ou é confiável. Hoje, o operador não tem onde registrar RG ou outro identificador, perdendo uma informação útil para reconhecer o cliente depois.

## Objetivo

Permitir registrar um documento alternativo do cliente (RG ou outro) no cadastro, sem mudar a validação nem a deduplicação atuais do CPF.

## Decisões de produto

- CPF e Documento são opcionais, inclusive ao mesmo tempo.
- CPF informado continua válido, validado e único.
- Documento é texto livre, sem máscara, validação de RG ou unicidade.

## Escopo

- Campo Documento abaixo do CPF na criação e edição.
- Persistência, retorno pela API, pré-preenchimento, alteração e remoção.
- Textos nos três idiomas da aplicação.

## Fora de escopo

- Validar formato de RG.
- Buscar, filtrar ou deduplicar por Documento.
- Exibir Documento em cards ou listas.
- Alterar regras de CPF, CEP ou endereço.

## Regras do negócio

| Propriedade | Definição |
|---|---|
| Nome técnico | `documento` |
| Tipo | texto livre |
| Obrigatório | não |
| Limite | 20 caracteres |
| Valor vazio | `null` após remover espaços externos |
| Unicidade | não |

## Critérios de aceite

- C1. Campo Documento aparece abaixo do CPF na criação e edição. ^c1
- C2. CPF válido salva com ou sem Documento. ^c2
- C3. Cliente sem CPF e com Documento salva. ^c3
- C4. Cliente sem CPF e sem Documento salva. ^c4
- C5. CPF inválido bloqueia o salvamento mesmo com Documento. ^c5
- C6. Documento é persistido, retornado e pré-preenchido. ^c6
- C7. Documento pode ser alterado e removido. ^c7
- C8. Mais de 20 caracteres é rejeitado. ^c8
- C9. Deduplicação do CPF permanece inalterada. ^c9
- C10. Clientes existentes sem Documento permanecem compatíveis. ^c10

## Pendências de decisão

- Nenhuma.
