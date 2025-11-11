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

class EditarItensCardapioService:
    
    BASE_URL = "http://127.0.0.1:8000"

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_orig(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(f"{self.BASE_URL}/cardapio/unidade", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_1(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = None
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_2(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(None, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_3(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(f"{self.BASE_URL}/cardapio/unidade", timeout=None)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_4(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_5(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(f"{self.BASE_URL}/cardapio/unidade", )
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_6(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(f"{self.BASE_URL}/cardapio/unidade", timeout=11)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_7(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(f"{self.BASE_URL}/cardapio/unidade", timeout=10)
        resp.raise_for_status()
        data = None
        return data if isinstance(data, list) else []
    
    xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_1': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_1, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_2': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_2, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_3': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_3, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_4': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_4, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_5': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_5, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_6': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_6, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_7': xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_7
    }
    
    def listar_cardapio_unidade(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_orig"), object.__getattribute__(self, "xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar_cardapio_unidade.__signature__ = _mutmut_signature(xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_orig)
    xǁEditarItensCardapioServiceǁlistar_cardapio_unidade__mutmut_orig.__name__ = 'xǁEditarItensCardapioServiceǁlistar_cardapio_unidade'

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_orig(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_1(self, ids: list[int]) -> dict:

        if ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_2(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError(None)
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_3(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("XXA lista de IDs não pode ser vazia.XX")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_4(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("a lista de ids não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_5(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A LISTA DE IDS NÃO PODE SER VAZIA.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_6(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = None
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_7(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "XXitensXX": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_8(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "ITENS": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_9(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(None)
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_10(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["XXitensXX"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_11(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["ITENS"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_12(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(None))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_13(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_14(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["XXitensXX"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_15(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["ITENS"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_16(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError(None)


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_17(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("XXNenhum ID válido foi informado.XX")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_18(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("nenhum id válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_19(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("NENHUM ID VÁLIDO FOI INFORMADO.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_20(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = None
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_21(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(None,json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_22(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=None,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_23(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=None)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_24(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_25(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_26(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_27(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=11)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_28(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = None
        return data if isinstance(data, list) else []
    
    xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_1': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_1, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_2': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_2, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_3': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_3, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_4': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_4, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_5': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_5, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_6': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_6, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_7': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_7, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_8': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_8, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_9': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_9, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_10': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_10, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_11': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_11, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_12': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_12, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_13': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_13, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_14': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_14, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_15': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_15, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_16': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_16, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_17': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_17, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_18': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_18, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_19': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_19, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_20': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_20, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_21': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_21, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_22': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_22, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_23': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_23, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_24': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_24, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_25': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_25, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_26': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_26, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_27': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_27, 
        'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_28': xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_28
    }
    
    def ativar_itens_cardapio_unidade(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_orig"), object.__getattribute__(self, "xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_mutants"), args, kwargs, self)
        return result 
    
    ativar_itens_cardapio_unidade.__signature__ = _mutmut_signature(xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_orig)
    xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade__mutmut_orig.__name__ = 'xǁEditarItensCardapioServiceǁativar_itens_cardapio_unidade'
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_orig(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_1(self, ids: list[int]) -> dict:
        if ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_2(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError(None)
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_3(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("XXA lista de IDs não pode ser vazia.XX")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_4(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("a lista de ids não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_5(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A LISTA DE IDS NÃO PODE SER VAZIA.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_6(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = None
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_7(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "XXitensXX": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_8(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "ITENS": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_9(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(None)
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_10(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["XXitensXX"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_11(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["ITENS"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_12(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(None))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_13(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_14(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["XXitensXX"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_15(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["ITENS"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_16(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError(None)


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_17(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("XXNenhum ID válido foi informado.XX")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_18(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("nenhum id válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_19(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("NENHUM ID VÁLIDO FOI INFORMADO.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_20(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = None

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_21(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(None, json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_22(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=None)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_23(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_24(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", )

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_25(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = None
        return data if isinstance(data, list) else []
    
    xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_1': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_1, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_2': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_2, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_3': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_3, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_4': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_4, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_5': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_5, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_6': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_6, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_7': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_7, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_8': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_8, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_9': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_9, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_10': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_10, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_11': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_11, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_12': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_12, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_13': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_13, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_14': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_14, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_15': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_15, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_16': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_16, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_17': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_17, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_18': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_18, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_19': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_19, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_20': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_20, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_21': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_21, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_22': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_22, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_23': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_23, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_24': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_24, 
        'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_25': xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_25
    }
    
    def remover_itens_cardapio_unidade(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_orig"), object.__getattribute__(self, "xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_mutants"), args, kwargs, self)
        return result 
    
    remover_itens_cardapio_unidade.__signature__ = _mutmut_signature(xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_orig)
    xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade__mutmut_orig.__name__ = 'xǁEditarItensCardapioServiceǁremover_itens_cardapio_unidade'


    def xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_orig(self) -> dict:
        resp = requests.get(f"{self.BASE_URL}/cardapio/central")
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []


    def xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_1(self) -> dict:
        resp = None
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []


    def xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_2(self) -> dict:
        resp = requests.get(None)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []


    def xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_3(self) -> dict:
        resp = requests.get(f"{self.BASE_URL}/cardapio/central")
        resp.raise_for_status()
        data = None
        return data if isinstance(data, list) else []
    
    xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_1': xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_1, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_2': xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_2, 
        'xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_3': xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_3
    }
    
    def listar_cardapio_central(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_orig"), object.__getattribute__(self, "xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar_cardapio_central.__signature__ = _mutmut_signature(xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_orig)
    xǁEditarItensCardapioServiceǁlistar_cardapio_central__mutmut_orig.__name__ = 'xǁEditarItensCardapioServiceǁlistar_cardapio_central'
