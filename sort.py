import pandas as pd
import argparse
import bib

parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store', dest='list_integers', help='Arquivo com os números a serem ordenados')
parser.add_argument('-s', action='store_const', dest='sort_method', const='selection', help='Algoritmo selection sort selecionado')
parser.add_argument('-i', action='store_const', dest='sort_method', const='insertion', help='Algoritmo insertion sort selecionado')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

data = pd.read_csv(results.list_integers, header=None)
arr = data.to_numpy().ravel()
res = []

if(results.sort_method == 'selection'):
    res = bib.selection_sort(arr)
elif(results.sort_method == 'insertion'):
    res = bib.insertion_sort(arr)

for i in range(len(res)):
    print(res[i])