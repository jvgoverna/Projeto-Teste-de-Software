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

class HistoricoService:
    BASE_URL = "http://127.0.0.1:8000"


    resp = requests.get(f"{BASE_URL}/pedidos/historico")

    def xǁHistoricoServiceǁlistar_historico__mutmut_orig(self) -> list[dict]:
        resp = requests.get(f"{self.BASE_URL}/pedidos/historico", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_1(self) -> list[dict]:
        resp = None
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_2(self) -> list[dict]:
        resp = requests.get(None, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_3(self) -> list[dict]:
        resp = requests.get(f"{self.BASE_URL}/pedidos/historico", timeout=None)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_4(self) -> list[dict]:
        resp = requests.get(timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_5(self) -> list[dict]:
        resp = requests.get(f"{self.BASE_URL}/pedidos/historico", )
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_6(self) -> list[dict]:
        resp = requests.get(f"{self.BASE_URL}/pedidos/historico", timeout=11)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def xǁHistoricoServiceǁlistar_historico__mutmut_7(self) -> list[dict]:
        resp = requests.get(f"{self.BASE_URL}/pedidos/historico", timeout=10)
        resp.raise_for_status()
        data = None
        return data if isinstance(data, list) else []
    
    xǁHistoricoServiceǁlistar_historico__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHistoricoServiceǁlistar_historico__mutmut_1': xǁHistoricoServiceǁlistar_historico__mutmut_1, 
        'xǁHistoricoServiceǁlistar_historico__mutmut_2': xǁHistoricoServiceǁlistar_historico__mutmut_2, 
        'xǁHistoricoServiceǁlistar_historico__mutmut_3': xǁHistoricoServiceǁlistar_historico__mutmut_3, 
        'xǁHistoricoServiceǁlistar_historico__mutmut_4': xǁHistoricoServiceǁlistar_historico__mutmut_4, 
        'xǁHistoricoServiceǁlistar_historico__mutmut_5': xǁHistoricoServiceǁlistar_historico__mutmut_5, 
        'xǁHistoricoServiceǁlistar_historico__mutmut_6': xǁHistoricoServiceǁlistar_historico__mutmut_6, 
        'xǁHistoricoServiceǁlistar_historico__mutmut_7': xǁHistoricoServiceǁlistar_historico__mutmut_7
    }
    
    def listar_historico(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHistoricoServiceǁlistar_historico__mutmut_orig"), object.__getattribute__(self, "xǁHistoricoServiceǁlistar_historico__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar_historico.__signature__ = _mutmut_signature(xǁHistoricoServiceǁlistar_historico__mutmut_orig)
    xǁHistoricoServiceǁlistar_historico__mutmut_orig.__name__ = 'xǁHistoricoServiceǁlistar_historico'