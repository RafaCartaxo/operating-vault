# 02 - Plano de execução (MEL-0002)

> [!info]- Navegação QA/DEV
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/01 - Demanda|Demanda]]  
> **Plano técnico:** [[05 Arquivo/Melhorias/MEL-0002/DEV/PLAN-088-cliente-documento-alternativo|PLAN-088]]

## O quê

Adicionar Documento opcional abaixo de CPF no cadastro de cliente, com persistência, edição e limite de 20 caracteres.

## Vínculo e sequência

1. Migração e schema.
2. Entidade, casos de uso, repositório e controller.
3. Contrato/documentação da API.
4. Formulários de criação e edição.
5. Traduções e testes automatizados.
6. Gates do repositório.

## Escopo aprovado

- Implementar somente o escopo do PLAN-088.
- Manter CPF, CEP, endereço, listas e deduplicação inalterados.

## Decisões

- Valor vazio será normalizado para null.
- Documento não terá validação específica de RG.

## Pronto quando

- Critérios C1–C10 e CT-001–CT-008 do pacote QA estiverem cobertos.
- Gates aplicáveis do repositório estiverem verdes.
