quantidade_unidades = 3
unidades = [{"nome": "Unidade 1", "temperatura": 4},
                   {"nome": "Unidade 2", "temperatura": 6}, 
                   {"nome": "Unidade 3", "temperatura": 1}]


def monitorarTemperaturas(unidades):
    alerta = []
    for unidade in unidades:
        temp = unidade["temperatura"]
        alerta_temperatura = temp < 2 or temp > 8
        alerta.append({
            "nome": unidade["nome"],
            "alerta_temperatura": alerta_temperatura
        })
    return alerta

print("lista atual:\n", unidades)
print("alertas:\n", monitorarTemperaturas(unidades))