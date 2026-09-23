# CONTEXT_RULES – TaskAnalyzer

## Fonte de verdade
1. O contrato em `specs/task_analyzer_spec.md` é a fonte principal de verdade.
2. Não inventar requisitos ou regras de negócio não especificados.
3. Em caso de ambiguidade, solicitar esclarecimento antes de criar nova regra.

## Regras técnicas
4. Utilizar Python 3.11+.
5. Usar type hints em 100% das funções e parâmetros.
6. Seguir PEP 8 e Single Responsibility Principle.
7. Usar Google style docstrings.
8. Tratar erros com exceções específicas.
9. Prevenir divisão por zero e resultados matematicamente inválidos.
10. Não usar bibliotecas externas além das autorizadas em `requirements.txt`.

## Testes e homologação
11. Toda nova funcionalidade deve ter teste automatizado correspondente.
12. Não alterar os cenários de aceite sem autorização.
13. Executar o pytest antes de considerar uma alteração pronta.
14. O código gerado por IA deve passar por revisão humana.
15. Somente código homologado deve ser integrado à `main`.
