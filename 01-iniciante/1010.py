cod_prod1, qtd_prod1, vlr_prod1 = input().split()
cod_prod2, qtd_prod2, vlr_prod2 = input().split()
print(f"VALOR A PAGAR: R$ {((int(qtd_prod1)*float(vlr_prod1))+(int(qtd_prod2)*float(vlr_prod2))):.2f}")