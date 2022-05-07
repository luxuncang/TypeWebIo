from ast import Raise
from numpy import put_along_axis
from pywebio import pin as pwpin
from pywebio.pin import *
from pywebio.pin import OutputPosition

from .baseui import BaseUi

__all__ = ["BasePin", "PinInput", "PinTextarea", "PinSelect", "PinCheckbox", "PinRadio", "PinSlider", "PinActions"]

class BasePin(BaseUi):
    def show(self):
        func = getattr(pwpin, self.uitype)
        agrg, kwarg = self.general_parameters(func, self.get_kw())
        obj = func(*agrg, **kwarg)
        if hasattr(self, 'style'):
            obj.style(self.style)
        if hasattr(self, 'onclick'):
            obj.onclick(self.onclick)
        return obj

    @property
    def uitype(self):
        cls_naem = self.__class__.__name__
        if cls_naem == "PinInput":
            return "pin_input"
        elif cls_naem == "PinTextarea":
            return "pin_textarea"
        elif cls_naem == "PinSelect":
            return "pin_select"
        elif cls_naem == "PinCheckbox":
            return "pin_checkbox"
        elif cls_naem == "PinRadio":
            return "pin_radio"
        elif cls_naem == "PinSlider":
            return "pin_slider"
        elif cls_naem == "PinActions":
            return "pin_actions"
        raise Exception("Unknown type")


class PinInput(BasePin):
    def __init__(
        self,
        name,
        type="text",
        *,
        label="",
        value=None,
        placeholder=None,
        readonly=None,
        datalist=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ) -> None:
        self.kw = locals()
        self.name = name
        self.type = type
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.readonly = readonly
        self.datalist = datalist
        self.help_text = help_text
        self.scope = scope
        self.position = position


class PinTextarea(BasePin):
    def __init__(
        self,
        name,
        *,
        label="",
        rows=6,
        code=None,
        maxlength=None,
        minlength=None,
        value=None,
        placeholder=None,
        readonly=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.name = name
        self.label = label
        self.rows = rows
        self.code = code
        self.maxlength = maxlength
        self.minlength = minlength
        self.value = value
        self.placeholder = placeholder
        self.readonly = readonly
        self.help_text = help_text
        self.scope = scope
        self.position = position


class PinSelect(BasePin):
    def __init__(
        self,
        name,
        options=None,
        *,
        label="",
        multiple=None,
        value=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.name = name
        self.label = label
        self.multiple = multiple
        self.options = options
        self.value = value
        self.help_text = help_text
        self.scope = scope
        self.position = position


class PinCheckbox(BasePin):
    def __init__(
        self,
        name,
        options=None,
        *,
        label="",
        inline=None,
        value=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.name = name
        self.options = options
        self.label = label
        self.inline = inline
        self.value = value
        self.help_text = help_text
        self.scope = scope
        self.position = position


class PinRadio(BasePin):
    def __init__(
        self,
        name,
        options=None,
        *,
        label="",
        inline=None,
        value=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.name = name
        self.options = options
        self.label = label
        self.inline = inline
        self.value = value
        self.help_text = help_text
        self.scope = scope
        self.position = position


class PinSlider(BasePin):
    def __init__(
        self,
        name,
        *,
        label="",
        value=0,
        min_value=0,
        max_value=100,
        step=1,
        required=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.name = name
        self.label = label
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.required = required
        self.help_text = help_text
        self.scope = scope
        self.position = position


class PinActions(BasePin):
    def __init__(
        self,
        name,
        *,
        label="",
        buttons=None,
        help_text=None,
        scope=None,
        position=OutputPosition.BOTTOM
    ) -> None:
        self.kw = locals()
        self.name = name
        self.label = label
        self.buttons = buttons
        self.help_text = help_text
        self.scope = scope
        self.position = position
