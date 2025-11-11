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

class VisualizarCardapioService:
    BASE_URL = "http://127.0.0.1:8000"

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_orig(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_1(self):
        response = None
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_2(self):
        response = requests.get(None)
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_3(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = None
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_4(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() and []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_5(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = None

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_6(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = None
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_7(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get(None, "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_8(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", None)
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_9(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_10(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", )
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_11(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("XXCOMIDAXX", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_12(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("comida", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_13(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "XXSem nomeXX")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_14(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_15(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "SEM NOME")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_16(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = None
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_17(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get(None, "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_18(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", None)
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_19(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_20(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", )
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_21(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("XXPRECOXX", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_22(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("preco", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_23(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "XX0XX")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_24(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = None
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_25(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) * 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_26(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(None) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_27(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 101
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_28(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = None

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_29(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 1.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_30(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = None
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_31(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get(None, "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_32(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", None)
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_33(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_34(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", )
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_35(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("XXTEMPO_PREPAROXX", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_36(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("tempo_preparo", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_37(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "XXN/AXX")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_38(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "n/a")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_39(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append(None)

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_40(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"XXnomeXX": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_41(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"NOME": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_42(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "XXprecoXX": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_43(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "PRECO": preco_reais, "tempo_preparo": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_44(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "XXtempo_preparoXX": tempo})

        return itens

    def xǁVisualizarCardapioServiceǁview_menu__mutmut_45(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "TEMPO_PREPARO": tempo})

        return itens
    
    xǁVisualizarCardapioServiceǁview_menu__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁVisualizarCardapioServiceǁview_menu__mutmut_1': xǁVisualizarCardapioServiceǁview_menu__mutmut_1, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_2': xǁVisualizarCardapioServiceǁview_menu__mutmut_2, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_3': xǁVisualizarCardapioServiceǁview_menu__mutmut_3, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_4': xǁVisualizarCardapioServiceǁview_menu__mutmut_4, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_5': xǁVisualizarCardapioServiceǁview_menu__mutmut_5, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_6': xǁVisualizarCardapioServiceǁview_menu__mutmut_6, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_7': xǁVisualizarCardapioServiceǁview_menu__mutmut_7, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_8': xǁVisualizarCardapioServiceǁview_menu__mutmut_8, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_9': xǁVisualizarCardapioServiceǁview_menu__mutmut_9, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_10': xǁVisualizarCardapioServiceǁview_menu__mutmut_10, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_11': xǁVisualizarCardapioServiceǁview_menu__mutmut_11, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_12': xǁVisualizarCardapioServiceǁview_menu__mutmut_12, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_13': xǁVisualizarCardapioServiceǁview_menu__mutmut_13, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_14': xǁVisualizarCardapioServiceǁview_menu__mutmut_14, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_15': xǁVisualizarCardapioServiceǁview_menu__mutmut_15, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_16': xǁVisualizarCardapioServiceǁview_menu__mutmut_16, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_17': xǁVisualizarCardapioServiceǁview_menu__mutmut_17, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_18': xǁVisualizarCardapioServiceǁview_menu__mutmut_18, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_19': xǁVisualizarCardapioServiceǁview_menu__mutmut_19, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_20': xǁVisualizarCardapioServiceǁview_menu__mutmut_20, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_21': xǁVisualizarCardapioServiceǁview_menu__mutmut_21, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_22': xǁVisualizarCardapioServiceǁview_menu__mutmut_22, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_23': xǁVisualizarCardapioServiceǁview_menu__mutmut_23, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_24': xǁVisualizarCardapioServiceǁview_menu__mutmut_24, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_25': xǁVisualizarCardapioServiceǁview_menu__mutmut_25, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_26': xǁVisualizarCardapioServiceǁview_menu__mutmut_26, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_27': xǁVisualizarCardapioServiceǁview_menu__mutmut_27, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_28': xǁVisualizarCardapioServiceǁview_menu__mutmut_28, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_29': xǁVisualizarCardapioServiceǁview_menu__mutmut_29, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_30': xǁVisualizarCardapioServiceǁview_menu__mutmut_30, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_31': xǁVisualizarCardapioServiceǁview_menu__mutmut_31, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_32': xǁVisualizarCardapioServiceǁview_menu__mutmut_32, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_33': xǁVisualizarCardapioServiceǁview_menu__mutmut_33, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_34': xǁVisualizarCardapioServiceǁview_menu__mutmut_34, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_35': xǁVisualizarCardapioServiceǁview_menu__mutmut_35, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_36': xǁVisualizarCardapioServiceǁview_menu__mutmut_36, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_37': xǁVisualizarCardapioServiceǁview_menu__mutmut_37, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_38': xǁVisualizarCardapioServiceǁview_menu__mutmut_38, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_39': xǁVisualizarCardapioServiceǁview_menu__mutmut_39, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_40': xǁVisualizarCardapioServiceǁview_menu__mutmut_40, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_41': xǁVisualizarCardapioServiceǁview_menu__mutmut_41, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_42': xǁVisualizarCardapioServiceǁview_menu__mutmut_42, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_43': xǁVisualizarCardapioServiceǁview_menu__mutmut_43, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_44': xǁVisualizarCardapioServiceǁview_menu__mutmut_44, 
        'xǁVisualizarCardapioServiceǁview_menu__mutmut_45': xǁVisualizarCardapioServiceǁview_menu__mutmut_45
    }
    
    def view_menu(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁVisualizarCardapioServiceǁview_menu__mutmut_orig"), object.__getattribute__(self, "xǁVisualizarCardapioServiceǁview_menu__mutmut_mutants"), args, kwargs, self)
        return result 
    
    view_menu.__signature__ = _mutmut_signature(xǁVisualizarCardapioServiceǁview_menu__mutmut_orig)
    xǁVisualizarCardapioServiceǁview_menu__mutmut_orig.__name__ = 'xǁVisualizarCardapioServiceǁview_menu'
