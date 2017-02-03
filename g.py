custo_refeicao = 44.50
impostos = 6.75/100
gorjeta = 15/100
custo_refeicaoTotal = custo_refeicao + (custo_refeicao * impostos)
gorjetaTotal = gorjeta + (custo_refeicaoTotal * gorjeta)
print("Gojeta $ %.2f " % gorjetaTotal)
