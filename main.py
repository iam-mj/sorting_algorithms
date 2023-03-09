import time
from generate import gen
from mergesort import merge
from bucketsort import bucket
from quicksort import quick
from radixsort import radix
from shellsort import shell


f = open("tests.txt")
nr_teste = int([x for x in f.readline().split()][2])
#teste - lista cu informatii despre testele noastre
sorts = [bucket, radix, shell]
ch_sorts = ["bucket", "radix", "shell"]
teste = []
for i in range(nr_teste):
    test = [x for x in f.readline().split()]
    test = [int(test[i]) for i in [2, 5]]
    teste.append(test)

cnt = 0
for test in teste:
    cnt += 1
    #generam numerele
    lista = gen(test[0], test[1])
    print("\n Testul " + str(cnt) + " N = " + str(test[0]) + " Max = " + str(test[1]), end = ':')

    lista_py = sorted(lista)

    cnt_ch = 0
    for sort in sorts:
        timp_start = time.time()
        myList = sort(lista, test[0], test[1] - 1)
        #myList = bucket(lista, test[0], test[1] - 1)
        #myList = merge(lista, 0, test[0] - 1)
        #myList = shell(lista, test[0])
        #myList = quick(lista, 0, test[0] - 1)
        #myList = radix(lista, test[0], test[1] - 1)
        timp_stop = time.time()

        if lista_py == myList:
            status = " OK"
        else: 
            status = " Failed =(("

        print("\n - a durat " + str(timp_stop - timp_start) + status + " cu metoda " + ch_sorts[cnt_ch], end = '')
        cnt_ch += 1