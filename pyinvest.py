import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, '')

capital = float(input('Capital inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual (%)'))/100
perc_cdb = float(input('Percentual do CDI (%)'))/100
perc_lci = float(input('Percentual do LCI (%)'))/100
taxa_fii = float(input('Rentabiliadade mensal FII (%)'))/100
meta = float(input('Meta financeira (R$)'))

cdi_mensal = math.pow(1+cdi_anual, 1/12) -1

total_investido = capital + (aporte * meses)

taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 +taxa_cdb), meses) + (aporte *meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses))

taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses) + (aporte*meses))

resultados_fii = []
montante_fii_base = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))

fii1 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii2 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii3 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii4 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii5 = montante_fii_base * (1 + random.uniform(-0.03,0.03))

resultados_fii = [fii1,fii2,fii3,fii4,fii5]

fii_media = statistics.mean (resultados_fii)
fii_mediana = statistics.median (resultados_fii)
fii_desvio = statistics.pstdev (resultados_fii)

data_simulacao = datetime.date.today()

data_resgate = data_simulacao + datetime.timedelta(days = meses * 30)

data_simulacao_formatada = data_simulacao.strftime("%d/%m/%Y")
data_resgate_formatada = data_resgate.strftime("%d/%m/%Y")

print("\nPyInvest - Simulador de Investimentos\n")
print("Data da Simulação:", data_simulacao_formatada)
print("Data estimada de resgate:", data_resgate_formatada)

print("Total investido", locale.currency(total_investido, grouping=True))

print ("\nResultados Financeiros")
print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print("LCI/LCA:", locale.currency(montante_lci, grouping=True))
print("Poupança:", locale.currency(montante_poupanca, grouping=True))
print("FII (média):", locale.currency(fii_media, grouping=True))

print("\nEstatísticas FII")
print("Mediana:", locale.currency(fii_mediana, grouping=True))
print("Desvio Padrão:", locale.currency(fii_desvio, grouping=True))

maior_valor = max(montante_cdb_liquido, montante_lci, montante_poupanca, fii_media)
meta_atingida = maior_valor >= meta
print("\nMeta Atingida?", meta_atingida)

blocos_cdb = int(montante_cdb_liquido // 1000) 
print("CDB:",      "█" * blocos_cdb)

blocos_lci = int(montante_lci // 1000)
print("LCI/LCA:",  "█" * blocos_lci)

blocos_poupanca = int(montante_poupanca // 1000)
print("Poupança:", "█" * blocos_poupanca)

blocos_fii = int(fii_media // 1000)
print("FII:",      "█" * blocos_fii)