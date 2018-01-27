# General description
The solution proposed uses multivariate Bernoulli Bayesian model. 
The data have been preprocessed and aggregated by user; each user is 
represented with a vector showing sum of transactions per type and MCC code
over the period observed.

The solution achieves 0.792 in AUC.


# Most valuable feature list
The following features got aggregated (sum) value of transactions per user.
## Class "0"
'Плата за взнос наличных через POS (в своем тер.банке)', 0.9797297297297299, 
'Звонки с использованием телефонов, считывающих магнитную ленту', 0.9490171990171997, 
'Плата за обслуживание банковской карты (за первый год)', 0.9468673218673221, 
'Плата за предоставление отчета по счету карты почтой', 0.9158476658476665, 
'Плата за получение наличных в Сбербанке (в других ТБ)', 0.8808353808353809, 
'Бакалейные магазины, супермаркеты', 0.8780712530712532, 
'Финансовые институты — снятие наличности автоматически', 0.7831695331695332, 
'Денежные переводы', 0.7822481572481572, 
'Аптеки', 0.7552211302211306, 
'Различные продовольственные магазины — рынки, магазины со спец-ассортиментом, продажа полуфабрикатов, фирменных блюд, продажа с помощью торговых автоматов', 0.6710687960687961)

## Class "1"
'Плата за взнос наличных через POS (в своем тер.банке)', 0.9859208523592087, 
'Звонки с использованием телефонов, считывающих магнитную ленту', 0.9410197869101977, 
'Плата за обслуживание банковской карты (за первый год)', 0.9349315068493151, 
'Плата за предоставление отчета по счету карты почтой', 0.9025875190258751, 
'Плата за получение наличных в Сбербанке (в других ТБ)', 0.8816590563165909, 
'Бакалейные магазины, супермаркеты', 0.8588280060882799, 
'Денежные переводы', 0.7926179604261795, 
'Финансовые институты — снятие наличности автоматически', 0.772831050228311, 
'Различные продовольственные магазины — рынки, магазины со спец-ассортиментом, продажа полуфабрикатов, фирменных блюд, продажа с помощью торговых автоматов', 0.6716133942161341, 
'Аптеки', 0.6640030441400306

## Spearman's correlation
Here is Spearman's rank correlation between individual variables per user and the gender variable.
Spearman's rank correlation for feature 195: SpearmanrResult(correlation=0.16995799082067498, pvalue=1.802761309860826e-55)
Spearman's rank correlation for feature 20: SpearmanrResult(correlation=0.02824308816204457, pvalue=0.009635215712240332)
Spearman's rank correlation for feature 186: SpearmanrResult(correlation=0.024344647220595376, pvalue=0.025666402658631175)
Spearman's rank correlation for feature 185: SpearmanrResult(correlation=0.04224588076061349, pvalue=0.00010748101494992016)
Spearman's rank correlation for feature 188: SpearmanrResult(correlation=0.10031109047759364, pvalue=3.096975887147338e-20)
Spearman's rank correlation for feature 56: SpearmanrResult(correlation=0.030141144483802295, pvalue=0.005732577094969927)
Spearman's rank correlation for feature 124: SpearmanrResult(correlation=0.09887155614977966, pvalue=1.0597254608245527e-19)
Spearman's rank correlation for feature 22: SpearmanrResult(correlation=0.09089776560802375, pvalue=7.004158414447863e-17)
Spearman's rank correlation for feature 94: SpearmanrResult(correlation=-0.11256328055311615, pvalue=4.274953474270099e-25)
Spearman's rank correlation for feature 61: SpearmanrResult(correlation=0.01455617420840944, pvalue=0.18221449838784712)

