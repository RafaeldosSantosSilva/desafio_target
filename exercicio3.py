#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
# na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
# Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média;

import json
arquivo = 'faturamento.json'

try:
    with open(arquivo, 'r') as file:
        dados = json.load(file)

    faturamento_diario = [item['valor'] for item in dados['faturamento']]
    valores = [valor for valor in faturamento_diario if valor > 0]

    if not valores:
        print("Não há dados de faturamento para calcular a média.")
    else:
        menor_valor = min(valores)
        maior_valor = max(valores)
        media_faturamento = sum(valores) / len(valores)
        dias_acima_da_media = sum(1 for valor in valores if valor > media_faturamento)
        
        print(f"Menor valor de faturamento: R${menor_valor:.2f}")
        print(f"Maior valor de faturamento: R${maior_valor:.2f}")
        print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")

except Exception as e:
    print("Ocorreu um erro:", str(e))