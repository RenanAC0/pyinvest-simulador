## PyInvest — Simulador de Investimentos

Projeto que fiz pra praticar bibliotecas nativas do Python aplicadas a um caso real: comparar diferentes tipos de investimento.

O programa pede capital inicial, aporte mensal, prazo e taxas, e simula quanto você teria em CDB, LCI/LCA, Poupança e FII no final do período, com juros compostos aplicados também sobre os aportes mensais. Calcula o IR regressivo sobre o CDB (22,5% a 15%, conforme o prazo) e mostra se a meta financeira foi atingida.

### Como executar

```
python pyinvest.py
```

### O que usei

- `math` pra calcular juros compostos
- `statistics` pra tirar média, mediana e desvio padrão dos resultados de FII
- `datetime` pra calcular a data de resgate
- `random` pra simular variação nos FIIs
- `locale` pra formatar os valores em R$

### Estrutura do código

O código é separado em funções, cada uma com uma responsabilidade:

- `taxa_mensal_a_partir_do_anual`: converte uma taxa anual em mensal
- `montante_com_aportes`: calcula o montante final com juros compostos sobre capital **e** aportes mensais
- `aliquota_ir_regressiva`: aplica a tabela de IR da Receita Federal, conforme o prazo em dias
- `simular_fii`: gera os cenários aleatórios de FII
- `main`: pede os dados, chama as funções acima e imprime o resultado

### O que aprendi fazendo esse projeto

Foi o primeiro projeto em que usei várias bibliotecas juntas, então mexi bastante com formatação de saída. Na primeira versão, os aportes mensais eram só somados, sem render juros, o que deixava o resultado abaixo do real — corrigi aplicando a fórmula de juros compostos com aportes (`M = C*(1+i)^n + A * (((1+i)^n - 1) / i)`) e organizei o código em funções, que era o que eu já tinha apontado aqui como próximo passo.

### Próximos passos

- Testes automatizados com `pytest` para `montante_com_aportes` e `aliquota_ir_regressiva`
