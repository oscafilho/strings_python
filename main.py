from extrator_url import ExtratorURL

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print(extrator_url == extrator_url_2)



# extrator = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
# #extrator_url = ExtratorURL(None)
# valor_quantidade = extrator.get_valor_parametro("quantidade")
# print(valor_quantidade)
# print(dir(extrator))

# print("O tamanho da URL: ", len(extrator))
# print(extrator)

"""
#url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
url = ""
url = url.replace(" ", "")
url = url.strip()
if url == "":
    raise value(Error("A URL está vazia"))

#print(url)

# Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
"""