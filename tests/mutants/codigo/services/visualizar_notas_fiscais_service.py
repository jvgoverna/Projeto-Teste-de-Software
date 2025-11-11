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

class VisualizarNotasFiscaisService:

    BASE_URL = "http://127.0.0.1:8000"

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_orig(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_1(self):
        response = None
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_2(self):
        response = requests.get(None)
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_3(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = None
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_4(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() and []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_5(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = None

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_6(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = None
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_7(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get(None, "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_8(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", None)
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_9(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_10(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", )
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_11(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("XXNUMERO_PEDIDOXX", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_12(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("numero_pedido", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_13(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "XXN/AXX")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_14(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "n/a")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_15(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = None
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_16(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get(None, "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_17(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", None)
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_18(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_19(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", )
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_20(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("XXNOME_CLIENTEXX", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_21(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("nome_cliente", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_22(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "XXN/AXX")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_23(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "n/a")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_24(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = None
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_25(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get(None, "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_26(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", None)
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_27(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_28(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", )
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_29(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("XXCPFXX", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_30(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("cpf", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_31(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "XXN/AXX")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_32(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "n/a")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_33(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = None
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_34(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get(None, "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_35(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", None)
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_36(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_37(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", )
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_38(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("XXPRECOXX", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_39(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("preco", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_40(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "XX0XX")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_41(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = None
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_42(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) * 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_43(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(None) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_44(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 101
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_45(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = None

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_46(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 1.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_47(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append(None)
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_48(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "XXNUMERO_PEDIDOXX": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_49(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "numero_pedido": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_50(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "XXNOME_CLIENTEXX": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_51(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "nome_cliente": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_52(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "XXCPFXX": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_53(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "cpf": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_54(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "XXPRECOXX": preco_reais
            })
        return notas_fiscais

    def xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_55(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "preco": preco_reais
            })
        return notas_fiscais
    
    xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_1': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_1, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_2': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_2, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_3': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_3, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_4': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_4, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_5': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_5, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_6': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_6, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_7': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_7, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_8': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_8, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_9': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_9, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_10': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_10, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_11': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_11, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_12': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_12, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_13': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_13, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_14': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_14, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_15': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_15, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_16': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_16, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_17': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_17, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_18': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_18, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_19': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_19, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_20': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_20, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_21': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_21, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_22': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_22, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_23': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_23, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_24': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_24, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_25': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_25, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_26': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_26, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_27': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_27, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_28': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_28, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_29': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_29, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_30': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_30, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_31': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_31, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_32': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_32, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_33': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_33, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_34': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_34, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_35': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_35, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_36': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_36, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_37': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_37, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_38': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_38, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_39': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_39, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_40': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_40, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_41': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_41, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_42': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_42, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_43': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_43, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_44': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_44, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_45': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_45, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_46': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_46, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_47': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_47, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_48': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_48, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_49': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_49, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_50': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_50, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_51': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_51, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_52': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_52, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_53': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_53, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_54': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_54, 
        'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_55': xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_55
    }
    
    def listar_notas_fiscais(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_orig"), object.__getattribute__(self, "xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar_notas_fiscais.__signature__ = _mutmut_signature(xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_orig)
    xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais__mutmut_orig.__name__ = 'xǁVisualizarNotasFiscaisServiceǁlistar_notas_fiscais'
    """

    Exemplo
    --------
    GET /notas-fiscais

    Resposta (200):
    [
      { "id": 1, "NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "11122233344", "PRECO": "2100" },
      { "id": 2, "NUMERO_PEDIDO": "1002", "NOME_CLIENTE": "Maria Oliveira", "CPF": "99988877766", "PRECO": "1700" }
    ]
    """