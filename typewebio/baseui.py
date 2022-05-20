from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

from abc import ABC, abstractmethod
from typing import Callable, Dict, Any, Tuple
import inspect

class BaseUi(ABC):

    @abstractmethod
    def show(self):
        ...

    def get_kw(self):
        self.kw.pop('self', None)
        return {k:getattr(self, k) for k in self.kw.keys()}

    @classmethod
    def ui_to_show(cls, ui):
        return ui.show() if isinstance(ui, BaseUi) else ui

    @classmethod
    def get_func_bind(cls, func: Callable, *args, **kwargs) -> Dict[str, Any]:
        sig = inspect.signature(func)
        return dict(sig.bind(*args, **kwargs).arguments.items())

    @classmethod
    def general_parameters(cls, func: Callable, d: dict) -> Tuple[tuple, dict]:
        args = []
        kwargs = {}
        parse_bind = {name:parse.kind for name, parse in inspect.signature(func).parameters.items()}
        for k,v in d.items():
            if k in parse_bind:
                if parse_bind[k] == inspect.Parameter.VAR_POSITIONAL:
                    args += list(v)
                elif parse_bind[k] == inspect.Parameter.VAR_KEYWORD:
                    kwargs |= v
                elif parse_bind[k] in [
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    inspect.Parameter.POSITIONAL_ONLY,
                ]:
                    args.append(v)
                elif parse_bind[k] == inspect.Parameter.KEYWORD_ONLY:
                    kwargs[k] = v
        return tuple(args), kwargs