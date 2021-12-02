import numpy as np

km = np.loadtxt(
    fname=r'C:\Users\souza\OneDrive\Documentos\GitHub\heros-journey\heros-journey\Python\Alura\numpy\carros-km.txt', dtype=int)

dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro',
        'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital',
        'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS',
        'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

acessorios = np.array(dados)
print(acessorios)

