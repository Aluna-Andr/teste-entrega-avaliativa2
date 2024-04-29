import math
import random
import time

def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heapsort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

def particao_bloco(lista, tam_bloco):
    particoes = []
    for i in range(0, len(lista), tam_bloco):
        particoes.append(lista[i:i + tam_bloco])
    return particoes

def selecao_raiz_quadrada_sort(lista):
    n = len(lista)
    tam_bloco = int(math.sqrt(n))

    particoes = particao_bloco(lista, tam_bloco)

    # saber o indice para o proximo elemento escolhido de cd partição
    indices_particoes = [0] * len(particoes)
    for i in range(n):
        menor_valor = float("inf")
        indice_menor = -1
        for j, particao in enumerate(particoes):
            if indices_particoes[j] < len(particao) and particao[indices_particoes[j]] < menor_valor:
                menor_valor = particao[indices_particoes[j]]
                indice_menor = j
        lista[i] = menor_valor
        indices_particoes[indice_menor] += 1


def ordenarArquivosAleatorios(tamanhos):
    for tamanho in tamanhos:
        nome_arquivo_entrada = "DadosLista_{}.txt".format(tamanho)
        nome_arquivo_saida = "DadosOrdenadosRaiz_Heap_Crescente_{}.txt".format(tamanho)

        with open(nome_arquivo_entrada, "r") as arquivo_entrada:
            lista_numeros = [int(linha.strip()) for linha in arquivo_entrada]

        inicio = time.time()
        heapsort(lista_numeros)
        fim = time.time()

        tempo_execucao = fim - inicio
        print("Tempo de execução para ordenar o arquivo {}: {:.6f} segundos".format(nome_arquivo_entrada, tempo_execucao))

        with open(nome_arquivo_saida, "w") as arquivo_saida:
            for numero in lista_numeros:
                arquivo_saida.write(str(numero) + "\n")

def gerarListaAleatoriaArquivo(nome_arquivo, tamanho):
    with open(nome_arquivo, "w") as arquivo:
        for _ in range(tamanho):
            numeroAleatorio = random.randint(0, 10 * tamanho)
            arquivo.write(str(numeroAleatorio) + "\n")

def gerarArquivosAleatorios(tamanhos):
    for tamanho in tamanhos:
        nome_arquivo_entrada = "DadosLista_{}.txt".format(tamanho)
        gerarListaAleatoriaArquivo(nome_arquivo_entrada, tamanho)

# Casos de teste
tamanhos = [10000, 100000, 1000000, 10000000]
gerarArquivosAleatorios(tamanhos)
ordenarArquivosAleatorios(tamanhos)
