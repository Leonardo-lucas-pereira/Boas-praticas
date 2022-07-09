# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# print(fila_teste_2.chamacliente(10))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

test_fabrica = FabricaFila.pega_fila('prioritaria')
test_fabrica.atualiza_fila()
test_fabrica.atualiza_fila()
test_fabrica.atualiza_fila()
print(test_fabrica.chama_cliente(5))
print(test_fabrica.estatistica(EstatisticaResumida('20/03/2025', 120)))