"""Test Harness for TaskAnalyzer acceptance scenarios."""

from datetime import datetime, timedelta

import pytest

from src.task_analyzer import TaskValidationError, analyze_tasks


def make_task(task_id, priority, status, created, hours=None, deadline_hours=None):
    """Build a task fixture for tests."""
    completed = created + timedelta(hours=hours) if hours is not None else None
    deadline = (
        created + timedelta(hours=deadline_hours)
        if deadline_hours is not None else None
    )
    return {
        "id": task_id,
        "titulo": f"Tarefa {task_id}",
        "prioridade": priority,
        "data_criacao": created,
        "data_conclusao": completed,
        "prazo": deadline,
        "status": status,
    }


def test_cenario_1_calcula_metricas_corretamente():
    """Validate totals, averages and delay rate."""
    base = datetime(2026, 9, 1, 8, 0)
    tasks = [
        make_task(1, "baixa", "concluída", base, hours=2, deadline_hours=3),
        make_task(2, "alta", "concluída", base, hours=4, deadline_hours=3),
        make_task(3, "média", "concluída", base, hours=3, deadline_hours=3),
        make_task(4, "baixa", "pendente", base),
    ]

    result = analyze_tasks(tasks)

    assert result["total_tarefas"] == 4
    assert result["total_concluidas"] == 3
    assert result["total_pendentes"] == 1
    assert result["tempo_medio_conclusao_horas"] == pytest.approx(3.0)
    assert result["tempo_medio_conclusao_horas_por_prioridade"]["baixa"] == pytest.approx(2.0)
    assert result["tempo_medio_conclusao_horas_por_prioridade"]["média"] == pytest.approx(3.0)
    assert result["tempo_medio_conclusao_horas_por_prioridade"]["alta"] == pytest.approx(4.0)
    assert result["taxa_atraso_percentual"] == pytest.approx(33.333333, rel=1e-5)


def test_cenario_2_data_inconsistente_dispara_excecao():
    """Validate TaskValidationError for invalid dates."""
    base = datetime(2026, 9, 1, 10, 0)
    invalid = make_task(1, "alta", "concluída", base, hours=-1, deadline_hours=2)

    with pytest.raises(TaskValidationError):
        analyze_tasks([invalid])


def test_caso_de_borda_lista_vazia_retorna_medias_zero():
    """Validate empty input handling."""
    result = analyze_tasks([])

    assert result["total_tarefas"] == 0
    assert result["total_concluidas"] == 0
    assert result["total_pendentes"] == 0
    assert result["tempo_medio_conclusao_horas"] == 0.0
    assert all(
        value == 0.0
        for value in result["tempo_medio_conclusao_horas_por_prioridade"].values()
    )
    assert result["taxa_atraso_percentual"] == 0.0


def test_caso_de_borda_apenas_pendentes_retorna_medias_zero():
    """Validate input containing only pending tasks."""
    base = datetime(2026, 9, 1, 8, 0)
    tasks = [
        make_task(1, "baixa", "pendente", base),
        make_task(2, "alta", "pendente", base),
    ]

    result = analyze_tasks(tasks)

    assert result["total_tarefas"] == 2
    assert result["total_concluidas"] == 0
    assert result["total_pendentes"] == 2
    assert result["tempo_medio_conclusao_horas"] == 0.0
    assert result["taxa_atraso_percentual"] == 0.0
