# Arquivo professor.py

# ===================================================================
#  Header para hexdump
# ===================================================================

import inspect
import ctypes
dll = ctypes.CDLL(f"./hexdump.so")
dll.hexdump.argtypes = [ ctypes.c_uint64, ctypes.c_int32 ]

def py_hexdump(variavel, nome=None):
    # pega o nome da variavel
    if nome == None:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        nomes = [nome for nome, obj in callers_local_vars if obj is variavel]
        if len(nomes) > 0:
            nome = nomes[0]
    # mostra hexdump
    print(nome, hex(id(variavel)))
    dll.hexdump( id(variavel), 64 )
    print()

# ===================================================================
#  Main
# ===================================================================

lista = [16, 32, 'felipe', 6000]

py_hexdump(lista, 'lista')
py_hexdump(lista[0], 'lista[0]')
py_hexdump(lista[1], 'lista[1]')
py_hexdump(lista[2], 'lista[2]')
py_hexdump(lista[3], 'lista[3]')
