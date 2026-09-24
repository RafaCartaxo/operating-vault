# 01 - Análise (MEL-0002)

> [!info]- Navegação QA/DEV
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/01 - Demanda|Demanda]]  
> **Plano:** [[02 - Plano de execução|Plano de execução]]

## Veredito

A melhoria é viável; exige migração não destrutiva e propagação do campo Documento por backend, API, frontend, traduções e testes.

## O que foi confirmado

- CPF e Documento podem ficar vazios.
- CPF informado mantém validação e deduplicação atuais.
- Documento é texto livre, sem máscara, sem unicidade e limitado a 20 caracteres.

## Abordagem e riscos

- Alteração de schema deve preservar clientes existentes.
- Contrato backend/frontend precisa permanecer compatível para clientes sem Documento.
- CTs do pacote QA cobrem os casos de sucesso, erro, persistência e regressão.

## Alternativas descartadas

- Reutilizar o campo CPF para RG: descartado por misturar identificadores e quebrar a regra de CPF.

## Perguntas abertas

- Nenhuma.
