# 02 - Plano de execução (NXG-MEL-0008)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/01 - Demanda|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/03 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/04 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/02 - Plano de execução|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/04 - Code review|Code review]]  

## O quê

Consolidar a configuração e documentação de ambientes e entregar uma revisão reproduzível, preservando trabalhos separados.

## Vínculo e sequência

Gate QA aprovado; preservar e testar recuperação; consolidar infraestrutura e ambiente; executar correções NXG-029/030; validar tecnicamente e entregar a QA independente.

## Escopo aprovado

`.env.example`, referências/ignores, scripts, README, guias, `agents/`, `infra/`, planos e evidências. Componente de cliente integrado apenas pelos commits locais identificados; ícones e Qase ficam na branch WIP.

## Decisões

Manter documento, CEP e expandir/recolher juntos em `7099a97` por compartilharem trechos; alterações anteriores são recuperáveis. Corrigir CEP opcional no formulário após falha inicial de build.

## Pronto quando

Critérios e CTs em [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/01 - Demanda|demanda]] e [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/03 - Casos de teste|casos de teste]]; QA decide aceite e fechamento. QA deve decidir os CTs, consolidar governança e avaliar a revisão final. Checkout QA ativo e rename local seguem coordenação; não renomear agora. Não foi feito teste em macOS.

### Testes desta etapa

- Unitários/UI: `npm test`; segurança: `npm run test:safety`.
- Integração: Compose `config` com valores sintéticos e smoke em banco isolado; QA valida checkout e persistência.
- Gates: build, `node scripts/check-dist.mjs`, auditorias documentais, UI, estilos, módulos e links.
