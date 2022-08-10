# Rossmann Predict Sales 

<div align="center">
<img src="img/Rossmann.jpg" width="500px">
</div>
</br>

## O Problema de Negócio 

- O CFO (Chief Financial Officer) da Rossmann pretende fazer uma reforma em todas as unidades, para isso, uma parcela do faturamento de cada loja deverá ser destinada para reforma da mesma nas próximas 6 semanas
- Assim, a fim de iniciar o processo de reformas, o CFO solicitou uma previsão de vendas de cada uma das unidades da Rossmann, nas próximas 6 semanas para ter uma maior previsibilidade das receitas de cada loja e poder alocar os recursos de forma mais eficiente

## Solução Esperada

1. Resposta à questão de negócio:
    - A previsão de vendas de cada uma das unidades Rossmann
2. Formato
    - O valor total da previsão de vendas de cada unidade Rossmann solicitada para as próximas 6 semanas
3. Local
    - Bot no Telegram

## Planejamento da Solução

### Etapas da Solução

1. **Questão de Negócio**
2. **Entendimento do Negócio**
3. **Coleta dos Dados**
    1. Entradas (fontes de dados)
        1. Kaggle: [https://www.kaggle.com/c/rossmann-store-sales](https://www.kaggle.com/c/rossmann-store-sales)
4. **Limpeza dos Dados**
    1. Descrição dos Dados
    2. Filtragem dos Dados4
    3. Fillout NA
    4. Feature Engeneering
5. **Exploração dos Dados**
    1. Teste de Hipóteses
6. **Modelagem dos Dados**
    1. Preparação dos dados
    2. Rescaling e Enconding
    3. Seleção de Features
7. **Algoritmos de Machine Learning**
    1. Teste de algoritmos candidatos
8. **Avaliação do Algoritmo**
    1. Cross Validation
    2. Avaliação do erro dos algoritmos escolhidos
    3. Fine Tuning
9. **Deploy do Modelo em Produção**
    1. Criar API para consumo dos dados do modelo
    2. Fazer deploy da API em nuvem
    3. Criar APIs para consulta de dados no Telegram
    4. Testar Bot Telegram

## Dicionário de Dados:

**Store** - a unique Id for each store

**Sales** - the turnover for any given day (this is what you are predicting)

**Customers** - the number of customers on a given day

**Open** - an indicator for whether the store was open: 0 = closed, 1 = open

**StateHoliday** - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None

**SchoolHoliday** - indicates if the (Store, Date) was affected by the closure of public schools

**StoreType** - differentiates between 4 different store models: a, b, c, d

**Assortment** - describes an assortment level: a = basic, b = extra, c = extended

**CompetitionDistance** - distance in meters to the nearest competitor store

**CompetitionOpenSince[Month/Year]** - gives the approximate year and month of the time the nearest competitor was opened

**Promo** - indicates whether a store is running a promo on that day

**Promo2** - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating

**Promo2Since[Year/Week]** - describes the year and calendar week when the store started participating in Promo2

**PromoInterval** - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

### Análise Exploratória dos Dados

H1. Lojas com maior sortimentos deveriam vender mais.

- Verdadeiro. Lojas com maior diversidade de produtos vendem 18% mais em média que as lojas com diversidade estendida

H**2.** Lojas com competidores mais próximos deveriam vender menos.

H**3.** Lojas com competidores à mais tempo deveriam vendem mais.

H**4.** Lojas com promoções ativas por mais tempo deveriam vender mais.

- Verdadeiro. Lojas com promoções ativas por mais tempo possuem um tendencia de crescimento nas vendas ao longo das semanas

H**5.** Lojas com mais dias de promoção deveriam vender mais.

H**7.** Lojas com mais promoções consecutivas deveriam vender mais.

H**8.** Lojas abertas durante o feriado de Natal deveriam vender mais.

H**9.** Lojas deveriam vender mais ao longo dos anos.

- Verdadeiro ao longo dos anos, o crescimento médio das vendas é de 2%

H**10.** Lojas deveriam vender mais no segundo semestre do ano.

H**11.** Lojas deveriam vender mais depois do dia 10 de cada mês.

- Falso, após o dia 10, as vendas são em média 8% menores

H**12.** Lojas deveriam vender menos aos finais de semana.

- Falso, as vendas nos finais de semana são em média 22,5% maiore que nos dias úteis

H**13.** Lojas deveriam vender menos durante os feriados escolares.

### Resultados de Negócio

- Performance total do modelo
    
    → Abaixo, podemos comparar 3 cenários prinicipais, a soma real das vendas de todas as lojas durantes as 6 semanas, a soma das vendas preistas pelo modelo e a soma das vendas no cenário em que a média de vendas de cada loja é generalizda por 6 semenas
    
    Com essa comparação podemos perceber que a utilização de um modelo se justifica frente a utilização da média para a projeção a receita futura
    
- Performance do Negócio
    
    → Com base no erro calculado pelo modelo, podemos traçar cenários pessimistas e otimistas a fim de dar maiores possibilidades ao time de negócio
    
- Performance do Modelo:
    
    → O modeo apresentou uma performance satisfatórias com um MMAPE de 10% aproximadamente