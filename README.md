## PyInvest — Simulador de Investimentos

Projeto que fiz pra praticar bibliotecas nativas do Python aplicadas a um caso real: comparar diferentes tipos de investimento.

O programa pede capital inicial, aporte mensal, prazo e taxas, e simula quanto você teria em CDB, LCI/LCA, Poupança e FII no final do período. Também calcula o IR sobre o CDB e mostra se a meta financeira foi atingida.

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

### O que aprendi fazendo esse projeto

Foi o primeiro projeto em que usei várias bibliotecas juntas, então mexi bastante com formatação de saída e organização do código pra não ficar uma bagunça. Ainda dá pra melhorar — por exemplo separar em funções.
