"""Core analysis functions for TaskAnalyzer."""

from datetime import datetime
from typing import Any


class TaskValidationError(ValueError):
    """Raised when a task contains inconsistent or invalid data."""


def _validate_task(task: dict[str, Any]) -> None:
    """Validate the fields required by the TaskAnalyzer contract.

    Args:
        task: Task record to validate.

    Raises:
        TaskValidationError: If required fields are missing or invalid.
    """
    required = {"id", "titulo", "prioridade", "data_criacao", "status"}
    missing = required - task.keys()
    if missing:
        raise TaskValidationError(f"Campos obrigatórios ausentes: {sorted(missing)}")

    if task["prioridade"] not in {"baixa", "média", "alta"}:
        raise TaskValidationError("Prioridade inválida. Use baixa, média ou alta.")

    if task["status"] not in {"concluída", "pendente"}:
        raise TaskValidationError("Status inválido. Use concluída ou pendente.")

    if not isinstance(task["data_criacao"], datetime):
        raise TaskValidationError("data_criacao deve ser um datetime.")

    conclusion = task.get("data_conclusao")
    if task["status"] == "concluída":
        if not isinstance(conclusion, datetime):
            raise TaskValidationError("Tarefa concluída precisa de data_conclusao.")
        if conclusion < task["data_criacao"]:
            raise TaskValidationError(
                "data_conclusao não pode ser anterior a data_criacao."
            )

    deadline = task.get("prazo")
    if deadline is not None and not isinstance(deadline, datetime):
        raise TaskValidationError("prazo deve ser um datetime ou None.")


def analyze_tasks(tasks: list[dict[str, Any]]) -> dict[str, Any]:
    """Analyze tasks according to the SDD contract.

    Args:
        tasks: List of task dictionaries.

    Returns:
        Dictionary with totals, average completion times and delay rate.

    Raises:
        TaskValidationError: If a task violates the contract.
    """
    for task in tasks:
        _validate_task(task)

    total_tarefas = len(tasks)
    total_concluidas = sum(task["status"] == "concluída" for task in tasks)
    total_pendentes = sum(task["status"] == "pendente" for task in tasks)
    completed = [task for task in tasks if task["status"] == "concluída"]

    def average_hours(items: list[dict[str, Any]]) -> float:
        if not items:
            return 0.0
        total_seconds = sum(
            (task["data_conclusao"] - task["data_criacao"]).total_seconds()
            for task in items
        )
        return total_seconds / len(items) / 3600

    tempo_medio_conclusao_horas = average_hours(completed)
    tempo_medio_por_prioridade = {
        priority: average_hours(
            [task for task in completed if task["prioridade"] == priority]
        )
        for priority in ("baixa", "média", "alta")
    }

    with_deadline = [task for task in completed if task.get("prazo") is not None]
    delayed = [
        task for task in with_deadline
        if task["data_conclusao"] > task["prazo"]
    ]
    taxa_atraso_percentual = (
        len(delayed) / len(with_deadline) * 100 if with_deadline else 0.0
    )

    return {
        "total_tarefas": total_tarefas,
        "total_concluidas": total_concluidas,
        "total_pendentes": total_pendentes,
        "tempo_medio_conclusao_horas": tempo_medio_conclusao_horas,
        "tempo_medio_conclusao_horas_por_prioridade": tempo_medio_por_prioridade,
        "taxa_atraso_percentual": taxa_atraso_percentual,
    }
