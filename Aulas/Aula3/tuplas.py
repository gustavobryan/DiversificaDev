# variáveis compostas tuplas e dicts 
# Tuplas são imutáveis

marcas_de_carro = ("Ford", "Chevrolet", "Fiat", "Volkswagen")
print(type(marcas_de_carro))

# Dicionários
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2020
}  
carro["ano"] = 2021 # Dicionários são mutáveis

print(carro)