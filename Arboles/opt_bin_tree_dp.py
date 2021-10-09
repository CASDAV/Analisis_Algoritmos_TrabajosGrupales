
import heapq
import math
from os import pardir
import pprint
import unicodedata
import re
import sys
import binascii

# -------------------------------------------------------------------------


class BinTree:
    m_L = None
    m_R = None
    m_D = None
    m_F = None

    def __init__(self, d, f):
        self.m_D = d
        self.m_F = f
    # end def

    def __lt__(self, other):  # <
        if self.m_F == other.m_F:
            return self.m_D < other.m_D
        else:
            return self.m_F < other.m_F
    # end def

    def binSearchInit(self, v):
        actual = str(self.m_D)
        if actual == v:
            return "0"
        else:
            return self.bin_search(v)

    def bin_search(self, v):
        codigo = ""
        actual = str(self.m_D)
        #print("busco a " + v)

        if actual == v or actual == None:
            return ""

        # mirar a la izquierda

        if actual > v:
            if not self.m_L is None:
                if BinTree.bin_search(self.m_L, v) != None:
                    codigo += "0" + BinTree.bin_search(self.m_L, v)
                    return codigo
        if not self.m_R is None:
            if BinTree.bin_search(self.m_R, v) != None:
                codigo += "1" + BinTree.bin_search(self.m_R, v)
                return codigo

    # end def

    def leaf_searh(self, v):
        codigo = ""
        actual = str(self.m_D)

        if actual == v or actual == None:
            return ""

        # mirar a la izquierda
        if not self.m_L is None:
            if BinTree.leaf_searh(self.m_L, v) != None:
                codigo += "0" + BinTree.leaf_searh(self.m_L, v)
                return codigo

        # mirar a la derecha
        if not self.m_R is None:
            if BinTree.leaf_searh(self.m_R, v) != None:
                codigo += "1" + BinTree.leaf_searh(self.m_R, v)
                return codigo


def search_recursively(key, node):
    if node is None or key == node.key:
        return node
    if key < node.key:
        return search_recursively(key, node.left)
    return search_recursively(key, node.right)

    # end def


def __str__(self):
    r = str(self.m_D) + ':' + str(self.m_F) + '\n'
    if not self.m_L is None:
        r += '--L--> ' + str(self.m_L) + '\n'
    # end if
    if not self.m_R is None:
        r += '--R--> ' + str(self.m_R) + '\n'
    # end if
        return r
    # end def

# end class

# -------------------------------------------------------------------------


def opt_bin_tree_bt(D, P, B, i, j):
    if B[i][j] == -1:
        return None
    else:
        r = B[i][j]
        root = BinTree(D[r - 1], P[r - 1])
        root.m_L = opt_bin_tree_bt(D, P, B, i, r - 1)
        root.m_R = opt_bin_tree_bt(D, P, B, r + 1, j)
        return root

# end def

# -------------------------------------------------------------------------


def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))


def opt_bin_tree(D, P, Q):
    M = [[0 for j in range(len(Q) + 1)] for i in range(len(Q) + 1)]
    B = [[-1 for j in range(len(Q) + 1)] for i in range(len(Q) + 1)]

    for i in range(1, len(Q) + 1):
        M[i][i - 1] = Q[i - 1]
    # end for

    for i in range(len(P), 0, -1):
        for j in range(i, len(P) + 1):
            q = math.inf
            b = -1
            for r in range(i, j + 1):
                v = 0.0
                for l in range(i, j + 1):
                    v += P[l - 1]
                # end for
                for l in range(i - 1, j + 1):
                    v += Q[l]
                # end for
                v += M[i][r - 1]
                v += M[r + 1][j]
                if v < q:
                    q = v
                    b = r
                # end if
            # end for
            M[i][j] = q
            B[i][j] = b
        # end for
    # end for

    return opt_bin_tree_bt(D, P, B, 1, len(P))
# end def

# -------------------------------------------------------------------------


def build_huffman(D, P):
    # Forest build
    forest = []
    for i in range(len(D)):
        heapq.heappush(forest, BinTree(D[i], P[i]))
    # end for

    # Tree build
    while len(forest) > 1:
        t0 = heapq.heappop(forest)
        t1 = heapq.heappop(forest)
        n = BinTree('', t0.m_F + t1.m_F)
        n.m_L = t0
        n.m_R = t1
        heapq.heappush(forest, n)
    # end while

    return forest[0]

# end def

# -------------------------------------------------------------------------
# D = [ 'a' , 'b', 'c',  'd', 'e' ]
# P = [ 0.15, 0.1, 0.05, 0.10, 0.2 ]
# Q = [ 0.05, 0.1, 0.05, 0.05, 0.05, 0.1 ]


# -- Read file
file_hnd = open('el_quijote_3.txt', 'r', encoding="UTF-8")
txt = file_hnd.read().replace('\n', ' ')
file_hnd.close()

# Split delimiters
delimiters = " ,.!?/&-:;@'...()[]<>¡«–\""
"["+"\\".join(delimiters)+"]"
tokens = re.split("["+"\\".join(delimiters)+"]", txt)

# Remove empty strings
tokens = [t for t in tokens if len(t) != 0]

# Remove accents and transform to lower-case
tokens = [''.join(c for c in unicodedata.normalize('NFD', t)
                  if unicodedata.category(c) != 'Mn').lower() for t in tokens]

# Build histogram
histogram = {}
for t in tokens:
    if t in histogram:
        histogram[t][0] += 1
    else:
        histogram[t] = [1, 0]
    # end if
# end for

# Compute frequencies
for b in histogram:
    histogram[b][1] = float(histogram[b][0]) / float(len(tokens))
# end for
D = sorted(histogram.keys())
print(type(D))


# 1. Convertir el histograma en P y Q


suma = 0
minimo = 1000000000
cont = 0
for b in histogram:
    suma += histogram[b][1]
    cont += 1
    if(histogram[b][1] < minimo):
        minimo = histogram[b][1]
print("suma de probabilidades: " + str(suma))

print("minimo: " + str(minimo))
P = []
Q = []


for b in histogram:
    Q.append(minimo)
Q.append(minimo)

a = 0
for b in histogram:
    histogram[b][1] = float(histogram[b][0]) / float(len(tokens))
    P.append(float(histogram[D[a]][0]) / (float(len(tokens))))
    if a == 0:
        print(histogram[D[a]])
    a += 1


suma = 0
cont = 0
for b in histogram:
    suma += P[cont]
    cont += 1
print(suma)


opt = opt_bin_tree(D, P, Q)
huf = build_huffman(D, P)

# 2. Comprimir el mensaje usando opt

file_hnd = open('el_quijote_bin_OPT.bin', 'wb')


for token in tokens:
    #print(bytes(BinTree.binSearchInit(opt, token), encoding='utf8'))
    #txt = file_hnd.write( bytes( BinTree.binSearchInit(opt, token), encoding='utf8'))
    txt = file_hnd.write(  binascii.a2b_uu(BinTree.binSearchInit(opt, token)))
file_hnd.close()

# 3. Comprimir el mensaje usando huf

# -- Read file

file_hnd = open('el_quijote_bin.bin', 'wb')

for token in tokens:
    txt = file_hnd.write(
        bytes(bits2a(BinTree.leaf_searh(huf, token)), encoding='utf8'))
file_hnd.close()


# 4. Comparar la calidad de comprension
