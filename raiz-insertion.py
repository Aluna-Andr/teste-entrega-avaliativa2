import math
import random
import time

def selecao_raiz_quadrada_sort_iterativa(lista):
    n = len(lista)
    tam_bloco = int(math.sqrt(n))

    for inicio_bloco in range(0, n, tam_bloco):
        fim_bloco = min(inicio_bloco + tam_bloco, n)
        bloco = lista[inicio_bloco:fim_bloco]
        bloco = insertion_sort(bloco)
        lista[inicio_bloco:fim_bloco] = bloco

    # Ordenação final usando Insertion Sort
    lista = insertion_sort(lista)
    return lista

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1

        # Corrigir valor inicial de j (evita que j seja negativo quando i = 0)
        if j < 0:
            j = 0

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def gerarListaAleatoriaArquivo(nome_arquivo, tamanho):
    with open(nome_arquivo, "w") as arquivo:
        for _ in range(tamanho):
            numeroAleatorio = random.randint(0, 10 * tamanho)
            arquivo.write(str(numeroAleatorio) + "\n")

def gerarArquivosAleatorios(tamanhos):
    for tamanho in tamanhos:
        nome_arquivo_entrada = "DadosLista_{}.txt".format(tamanho)
        nome_arquivo_saida = "DadosOrdenadosRaiz_Insertion_{}.txt".format(tamanho)
        gerarListaAleatoriaArquivo(nome_arquivo_entrada, tamanho)

        # Ordenar a lista
        lista_ordenada = selecao_raiz_quadrada_sort_iterativa(ler_arquivo_para_lista(nome_arquivo_entrada))

        # Medir e imprimir tempo de execução
        inicio = time.time()
        salvar_lista_em_arquivo(lista_ordenada, nome_arquivo_saida)
        fim = time.time()
        tempo_execucao = fim - inicio
        print("Tempo de execução para ordenar o arquivo {}: {:.6f} segundos".format(nome_arquivo_entrada, tempo_execucao))


# Funções auxiliares para leitura e gravação de arquivos (não inclusas no código original)
def ler_arquivo_para_lista(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    return [int(linha.strip()) for linha in linhas]

def salvar_lista_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for numero in lista:
            arquivo.write(str(numero) + "\n")

# Casos de teste
tamanhos = [100, 1000, 10000, 100000, 1000000]
gerarArquivosAleatorios(tamanhos)
