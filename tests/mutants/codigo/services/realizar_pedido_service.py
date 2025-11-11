import requests
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
class RealizarPedidoService:
    BASE_URL = "http://127.0.0.1:8000"

    @staticmethod
    def _reais_para_centavos_str(valor_reais: float) -> str:
        return str(int(round(valor_reais * 100)))

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_orig(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_1(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = None

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_2(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "XXNUMERO_PEDIDOXX": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_3(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "numero_pedido": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_4(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(None),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_5(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(None)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_6(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "XXNOME_CLIENTEXX": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_7(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "nome_cliente": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_8(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "XXCPFXX": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_9(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "cpf": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_10(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "XXCOMIDASXX": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_11(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "comidas": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_12(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(None),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_13(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": "XX,XX".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_14(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "XXPRECOXX": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_15(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "preco": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_16(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(None),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_17(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "XXTEMPO_PREPAROXX": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_18(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "tempo_preparo": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_19(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(None),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_20(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(None)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_21(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = None
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_22(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(None, json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_23(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=None, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_24(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=None)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_25(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_26(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", timeout=10)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_27(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, )
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_28(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=11)
        resp.raise_for_status()
        return resp.json() or {}

    def xǁRealizarPedidoServiceǁcriar_pedido__mutmut_29(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() and {}
    
    xǁRealizarPedidoServiceǁcriar_pedido__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_1': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_1, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_2': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_2, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_3': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_3, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_4': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_4, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_5': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_5, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_6': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_6, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_7': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_7, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_8': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_8, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_9': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_9, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_10': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_10, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_11': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_11, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_12': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_12, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_13': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_13, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_14': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_14, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_15': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_15, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_16': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_16, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_17': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_17, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_18': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_18, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_19': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_19, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_20': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_20, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_21': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_21, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_22': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_22, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_23': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_23, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_24': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_24, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_25': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_25, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_26': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_26, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_27': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_27, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_28': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_28, 
        'xǁRealizarPedidoServiceǁcriar_pedido__mutmut_29': xǁRealizarPedidoServiceǁcriar_pedido__mutmut_29
    }
    
    def criar_pedido(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRealizarPedidoServiceǁcriar_pedido__mutmut_orig"), object.__getattribute__(self, "xǁRealizarPedidoServiceǁcriar_pedido__mutmut_mutants"), args, kwargs, self)
        return result 
    
    criar_pedido.__signature__ = _mutmut_signature(xǁRealizarPedidoServiceǁcriar_pedido__mutmut_orig)
    xǁRealizarPedidoServiceǁcriar_pedido__mutmut_orig.__name__ = 'xǁRealizarPedidoServiceǁcriar_pedido'
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_orig(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_1(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = None
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_2(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(None, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_3(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", timeout=None)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_4(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_5(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", )
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_6(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", timeout=11)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_7(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", timeout=10)
        resp.raise_for_status()
        data = None
        return data if isinstance(data, list) else []
    
    xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_1': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_1, 
        'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_2': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_2, 
        'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_3': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_3, 
        'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_4': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_4, 
        'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_5': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_5, 
        'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_6': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_6, 
        'xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_7': xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_7
    }
    
    def listar_pedidos_ativos(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_orig"), object.__getattribute__(self, "xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar_pedidos_ativos.__signature__ = _mutmut_signature(xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_orig)
    xǁRealizarPedidoServiceǁlistar_pedidos_ativos__mutmut_orig.__name__ = 'xǁRealizarPedidoServiceǁlistar_pedidos_ativos'
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_orig(self) -> dict:
        resp = requests.post(f"{self.BASE_URL}/pedidos/atualizar-status", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_1(self) -> dict:
        resp = None
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_2(self) -> dict:
        resp = requests.post(None, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_3(self) -> dict:
        resp = requests.post(f"{self.BASE_URL}/pedidos/atualizar-status", timeout=None)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_4(self) -> dict:
        resp = requests.post(timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_5(self) -> dict:
        resp = requests.post(f"{self.BASE_URL}/pedidos/atualizar-status", )
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_6(self) -> dict:
        resp = requests.post(f"{self.BASE_URL}/pedidos/atualizar-status", timeout=11)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}
    
    def xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_7(self) -> dict:
        resp = requests.post(f"{self.BASE_URL}/pedidos/atualizar-status", timeout=10)
        resp.raise_for_status()
        data = None
        return data if isinstance(data, dict) else {}
    
    xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_1': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_1, 
        'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_2': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_2, 
        'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_3': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_3, 
        'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_4': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_4, 
        'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_5': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_5, 
        'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_6': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_6, 
        'xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_7': xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_7
    }
    
    def atualizar_status_pedidos(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_orig"), object.__getattribute__(self, "xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_mutants"), args, kwargs, self)
        return result 
    
    atualizar_status_pedidos.__signature__ = _mutmut_signature(xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_orig)
    xǁRealizarPedidoServiceǁatualizar_status_pedidos__mutmut_orig.__name__ = 'xǁRealizarPedidoServiceǁatualizar_status_pedidos'