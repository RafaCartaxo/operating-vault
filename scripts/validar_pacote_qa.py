#!/usr/bin/env python3
"""Valida a integridade estrutural de um pacote QA de melhoria.

O script verifica o contrato mínimo do vault sem depender do Obsidian:
demanda -> critérios -> casos -> validação.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "00 README.md",
    "01 - Demanda.md",
    "02 - Plano de teste.md",
    "03 - Casos de teste.md",
    "04 - Validação dev.md",
    "05 - Preparação Qase.md",
)


def unique_matches(pattern: str, text: str) -> list[str]:
    return list(dict.fromkeys(re.findall(pattern, text, flags=re.MULTILINE)))


def add_error(errors: list[str], message: str) -> None:
    errors.append(f"❌ {message}")


def validate(package: Path) -> list[str]:
    errors: list[str] = []
    files: dict[str, str] = {}

    for filename in REQUIRED_FILES:
        path = package / filename
        if not path.is_file():
            add_error(errors, f"arquivo obrigatório ausente: {filename}")
        else:
            files[filename] = path.read_text(encoding="utf-8")

    if len(files) != len(REQUIRED_FILES):
        return errors

    demand = files["01 - Demanda.md"]
    plan = files["02 - Plano de teste.md"]
    cases = files["03 - Casos de teste.md"]
    validation = files["04 - Validação dev.md"]

    criteria = unique_matches(r"^[-*] C(\d+)\..*\^c\d+\s*$", demand)
    criteria_ids = {f"C{number}" for number in criteria}
    criteria_anchors = unique_matches(r"^[-*] C\d+\..*\^(c\d+)\s*$", demand)
    if not criteria_ids:
        add_error(errors, "nenhum critério C1..Cn foi encontrado na demanda")
    if len(criteria) != len(criteria_anchors):
        add_error(errors, "há critérios com âncoras duplicadas ou ausentes")

    case_ids = unique_matches(r"^> \[!example\]- (CT-\d{3})\b", cases)
    case_anchors = unique_matches(r"^\^(ct-\d{3})\s*$", cases)
    case_anchor_ids = {f"CT-{number[3:]}" for number in case_anchors}
    case_id_set = set(case_ids)
    if not case_ids:
        add_error(errors, "nenhum CT foi encontrado em 03 - Casos de teste.md")
    if len(case_ids) != len(case_anchor_ids):
        add_error(errors, "quantidade de CTs e âncoras não coincide")
    if len(case_ids) != len(set(case_ids)):
        add_error(errors, "há CTs duplicados em 03 - Casos de teste.md")
    if case_id_set != {f"CT-{number}" for number in sorted(criteria_ids, key=lambda value: int(value[1:]))} and criteria_ids:
        # A cardinalidade pode ser diferente quando um critério tem mais de um CT;
        # a cobertura abaixo é a fonte de verdade nesse caso.
        pass

    coverage_cts = set(unique_matches(r"\[\[03 - Casos de teste#\^ct-\d{3}\\\|(CT-\d{3})\]\]", cases))
    coverage_criteria = set(unique_matches(r"\[\[01 - Demanda#\^c\d+\\\|(C\d+)\]\]", cases))
    if coverage_criteria != criteria_ids:
        add_error(errors, f"matriz não cobre exatamente os critérios: esperado {sorted(criteria_ids)}, encontrado {sorted(coverage_criteria)}")
    if not case_id_set.issubset(coverage_cts):
        add_error(errors, "há CT sem entrada na matriz de cobertura")

    plan_cts = set(unique_matches(r"\[\[03 - Casos de teste#\^ct-\d{3}\\\|(CT-\d{3})\]\]", plan))
    if plan_cts != case_id_set:
        add_error(errors, f"plano de teste não corresponde aos CTs: esperado {sorted(case_id_set)}, encontrado {sorted(plan_cts)}")

    for case_id in case_ids:
        number = case_id[-3:]
        block_match = re.search(
            rf"^> \[!example\]- {re.escape(case_id)}\b.*?(?=^\^ct-{number}\s*$)",
            cases,
            flags=re.MULTILINE | re.DOTALL,
        )
        block = block_match.group(0) if block_match else ""
        if not block_match:
            add_error(errors, f"{case_id} não possui âncora única")
        if "[[04 - Validação dev#Resultado dos casos de teste]]" not in block:
            add_error(errors, f"{case_id} não possui link para a validação")
        if not re.search(r"\*\*Critérios cobertos:\*\*.*\[\[01 - Demanda#\^c\d+\|C\d+\]\]", block):
            add_error(errors, f"{case_id} não aponta para critério coberto")

    validation_rows = set(unique_matches(r"^\| \[\[03 - Casos de teste#\^ct-\d{3}\\\|(CT-\d{3})\]\]", validation))
    yaml_results = set(unique_matches(r"^  (ct_\d{3}):", validation))
    yaml_case_ids = {f"CT-{key[-3:]}" for key in yaml_results}
    if validation_rows != case_id_set:
        add_error(errors, f"validação não tem uma linha para cada CT: esperado {sorted(case_id_set)}, encontrado {sorted(validation_rows)}")
    if yaml_case_ids != case_id_set:
        add_error(errors, f"YAML da validação não corresponde aos CTs: esperado {sorted(case_id_set)}, encontrado {sorted(yaml_case_ids)}")

    canonical_checks = {
        "03 - Casos de teste.md": ("## Matriz de cobertura", "> [!example]-", "^ct-", "meta-bind-button"),
        "04 - Validação dev.md": ("## Resultado dos casos de teste", "^ct-", "ct_resultados:", "Pontos entregues"),
    }
    for filename, markers in canonical_checks.items():
        for marker in markers:
            if marker not in files[filename]:
                add_error(errors, f"{filename} perdeu bloco canônico: {marker}")

    template_text = "\n".join(
        files[filename]
        for filename in REQUIRED_FILES
        if filename not in {"00 README.md", "05 - Preparação Qase.md"}
    )
    placeholders = re.findall(r"^# .*<ID>|^# .*<projeto>|^# .*<PROJ>|^\s*(?:demanda|projeto):\s*\"?\"?$|TÍTULO DO|Título claro do cenário", template_text, flags=re.MULTILINE)
    if placeholders:
        add_error(errors, f"há placeholders de template não substituídos: {sorted(set(placeholders))}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="pasta da demanda QA")
    args = parser.parse_args()

    errors = validate(args.package)
    print(f"Pacote: {args.package}")
    if errors:
        print("\n".join(errors))
        print("\nPACOTE QA REPROVADO NO GATE DE INTEGRIDADE")
        return 1

    print("✅ arquivos obrigatórios presentes")
    print("✅ critérios, CTs, âncoras, matriz e validação coerentes")
    print("✅ estrutura canônica e links essenciais preservados")
    print("\nPACOTE QA APROVADO NO GATE DE INTEGRIDADE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
