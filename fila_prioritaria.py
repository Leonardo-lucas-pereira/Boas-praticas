from typing import Dict, List, Union

from fila_base import FilaBase
from costantes import CODIGO_PRIORITARIO
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


Estatisticas = Union[EstatisticaResumida, EstatisticaDetalhada]

class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> List[str]:
        display = []
        cliente_atual = self.fila.pop(0)
        display.append(f'Cliente: ]{cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.clientes_atendidos.append(cliente_atual)

        return display
        
    def estatistica(self, retorna_statistica: Estatisticas) -> dict:
        
        return retorna_statistica.roda_estatistica(self.clientes_atendidos)
