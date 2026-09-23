# sdd-task-analyzer

Projeto do Bootcamp III – Fase 2: implementação assistida por IA, Test Harness e versionamento Git/GitHub.

## Objetivo
Implementar o TaskAnalyzer a partir do contrato SDD e das regras de governança definidas na Fase 1.

## Estrutura
```text
sdd-task-analyzer/
├── README.md
├── CONTEXT_RULES.md
├── .gitignore
├── requirements.txt
├── specs/
│   └── task_analyzer_spec.md
├── tests/
│   └── test_harness.py
└── src/
    └── task_analyzer.py
```

## Requisitos
- Python 3.11+
- pytest

## Instalação
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Executar testes
Na raiz do projeto:
```bash
python -m pytest -q
```

Objetivo da Fase 2: 100% de aprovação.

## Git/GitHub
Fluxo sugerido:
- `main`
- `feature/sdd-specification`
- `feature/test-harness`
- `feature/task-analyzer-impl`

Os commits devem ser pequenos e descritivos. Deve existir pelo menos um Pull Request documentado.

## Homologação
O código gerado por IA deve ser revisado pelo estudante, validado contra `CONTEXT_RULES.md` e `specs/task_analyzer_spec.md` e aprovado antes de ser integrado à `main`.

## Desenvolvimento

Implementação realizada na branch desenvolvimento para validação do Test Harness e versionamento do projeto.