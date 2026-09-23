# TaskAnalyzer – SDD / Contrato Executável

## 1. Objetivo
O TaskAnalyzer recebe uma lista de tarefas e produz métricas de produtividade para apoiar a análise do desempenho das tarefas.

## 2. Entrada
Cada tarefa deve possuir:
- `id`: inteiro;
- `titulo`: texto;
- `prioridade`: `baixa`, `média` ou `alta`;
- `data_criacao`: `datetime`;
- `data_conclusao`: `datetime` para tarefas concluídas;
- `prazo`: `datetime` opcional;
- `status`: `concluída` ou `pendente`.

## 3. Saída
A função `analyze_tasks(tasks)` deve retornar:
- `total_tarefas`;
- `total_concluidas`;
- `total_pendentes`;
- `tempo_medio_conclusao_horas`;
- `tempo_medio_conclusao_horas_por_prioridade` para baixa, média e alta;
- `taxa_atraso_percentual`.

## 4. Regras
1. Somente tarefas concluídas participam do cálculo do tempo médio.
2. O tempo de conclusão é `data_conclusao - data_criacao`, convertido para horas.
3. `data_conclusao < data_criacao` é inválido e deve gerar `TaskValidationError`.
4. Prioridade deve ser baixa, média ou alta.
5. Status deve ser concluída ou pendente.
6. A taxa de atraso considera tarefas concluídas que possuem `prazo`.
7. Uma tarefa está atrasada quando `data_conclusao > prazo`.
8. Sem tarefas concluídas, as médias devem retornar `0.0`.
9. Sem tarefas concluídas com prazo, a taxa de atraso deve retornar `0.0`.
10. A função não deve lançar erro não tratado para lista vazia.

## 5. Cenários de aceite

### Cenário 1 – Sucesso
Dado um conjunto de tarefas válidas, quando `analyze_tasks` for executada, então os totais, médias gerais, médias por prioridade e taxa de atraso devem estar corretos.

### Cenário 2 – Exceção/Erro
Dado uma tarefa com `data_conclusao` anterior a `data_criacao`, quando a análise for executada, então `TaskValidationError` deve ser disparada.

### Casos de borda
Entradas vazias ou contendo somente tarefas pendentes devem retornar médias `0.0` e não devem gerar exceções não tratadas.
