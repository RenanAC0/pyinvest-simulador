import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, '')


def taxa_mensal_a_partir_do_anual(taxa_anual):
    """Converte uma taxa anual em taxa mensal equivalente (juros compostos)."""
    return math.pow(1 + taxa_anual, 1 / 12) - 1


def montante_com_aportes(capital, aporte, taxa_mensal, meses):
    """
    Calcula o montante final com juros compostos, aplicados tanto sobre o
    capital inicial quanto sobre os aportes mensais.

    Fórmula: M = C*(1+i)^n + A * (((1+i)^n - 1) / i)
    """
    fator = math.pow(1 + taxa_mensal, meses)

    if taxa_mensal == 0:
        # Sem rendimento: o aporte só se acumula, sem juros.
        return capital * fator + aporte * meses

    montante_capital = capital * fator
    montante_aportes = aporte * ((fator - 1) / taxa_mensal)
    return montante_capital + montante_aportes


def aliquota_ir_regressiva(dias):
    """Tabela regressiva de Imposto de Renda para renda fixa no Brasil."""
    if dias <= 180:
        return 0.225
    elif dias <= 360:
        return 0.20
    elif dias <= 720:
        return 0.175
    else:
        return 0.15


def simular_fii(montante_base, quantidade_cenarios=5, variacao=0.03):
    """Gera cenários aleatórios de FII em torno de um valor base."""
    return [
        montante_base * (1 + random.uniform(-variacao, variacao))
        for _ in range(quantidade_cenarios)
    ]


def barra(valor, escala=1000):
    return "█" * int(valor // escala)


def main():
    capital = float(input('Capital inicial: '))
    aporte = float(input('Aporte Mensal: '))
    meses = int(input('Prazo (meses): '))
    cdi_anual = float(input('CDI anual (%)')) / 100
    perc_cdb = float(input('Percentual do CDI (%)')) / 100
    perc_lci = float(input('Percentual do LCI (%)')) / 100
    taxa_fii = float(input('Rentabilidade mensal FII (%)')) / 100
    meta = float(input('Meta financeira (R$)'))

    cdi_mensal = taxa_mensal_a_partir_do_anual(cdi_anual)
    total_investido = capital + (aporte * meses)
    dias_totais = meses * 30

    # --- CDB ---
    taxa_cdb = cdi_mensal * perc_cdb
    montante_cdb = montante_com_aportes(capital, aporte, taxa_cdb, meses)
    lucro_cdb = montante_cdb - total_investido
    aliquota_cdb = aliquota_ir_regressiva(dias_totais)
    montante_cdb_liquido = total_investido + (lucro_cdb * (1 - aliquota_cdb))

    # --- LCI/LCA (isento de IR) ---
    taxa_lci = cdi_mensal * perc_lci
    montante_lci = montante_com_aportes(capital, aporte, taxa_lci, meses)

    # --- Poupança (isenta de IR) ---
    taxa_poupanca = 0.005
    montante_poupanca = montante_com_aportes(capital, aporte, taxa_poupanca, meses)

    # --- FII (isento de IR sobre os rendimentos distribuídos) ---
    montante_fii_base = montante_com_aportes(capital, aporte, taxa_fii, meses)
    resultados_fii = simular_fii(montante_fii_base)
    fii_media = statistics.mean(resultados_fii)
    fii_mediana = statistics.median(resultados_fii)
    fii_desvio = statistics.pstdev(resultados_fii)

    # --- Datas ---
    data_simulacao = datetime.date.today()
    data_resgate = data_simulacao + datetime.timedelta(days=dias_totais)
    data_simulacao_formatada = data_simulacao.strftime("%d/%m/%Y")
    data_resgate_formatada = data_resgate.strftime("%d/%m/%Y")

    # --- Saída ---
    print("\nPyInvest - Simulador de Investimentos\n")
    print("Data da Simulação:", data_simulacao_formatada)
    print("Data estimada de resgate:", data_resgate_formatada)

    print("Total investido:", locale.currency(total_investido, grouping=True))

    print("\nResultados Financeiros")
    print(f"CDB (IR de {aliquota_cdb:.1%}):", locale.currency(montante_cdb_liquido, grouping=True))
    print("LCI/LCA:", locale.currency(montante_lci, grouping=True))
    print("Poupança:", locale.currency(montante_poupanca, grouping=True))
    print("FII (média):", locale.currency(fii_media, grouping=True))

    print("\nEstatísticas FII")
    print("Mediana:", locale.currency(fii_mediana, grouping=True))
    print("Desvio Padrão:", locale.currency(fii_desvio, grouping=True))

    maior_valor = max(montante_cdb_liquido, montante_lci, montante_poupanca, fii_media)
    meta_atingida = maior_valor >= meta
    print("\nMeta Atingida?", meta_atingida)

    print("\nCDB:     ", barra(montante_cdb_liquido))
    print("LCI/LCA: ", barra(montante_lci))
    print("Poupança:", barra(montante_poupanca))
    print("FII:     ", barra(fii_media))


if __name__ == "__main__":
    main()
