from pywebio import input as pwinput
from pywebio.input import *

from .baseui import BaseUi

__all__ = [
    "BaseInput",
    "Input",
    "Textarea",
    "Select",
    "Checkbox",
    "Radio",
    "Slider",
    "Actions",
    "FileUpload",
    "InputGroup",
    "input_update"
]


class BaseInput(BaseUi):
    
    def show(self):
        func = getattr(pwinput, self.uitype)
        agrg, kwarg = self.general_parameters(func, self.get_kw())
        return func(*agrg, **kwarg)

    @property
    def uitype(self):
        cls_naem = self.__class__.__name__
        if cls_naem == "Input":
            return "input"
        if cls_naem == "Textarea":
            return "textarea"
        if cls_naem == "Select":
            return "select"
        if cls_naem == "Checkbox":
            return "checkbox"
        if cls_naem == "Radio":
            return "radio"
        if cls_naem == "Slider":
            return "slider"
        if cls_naem == "Actions":
            return "actions"
        if cls_naem == "FileUpload":
            return "file_upload"
        if cls_naem == "InputGroup":
            return "input_group"
        raise Exception("Unknown type")


class Input(BaseInput):
    def __init__(
        self,
        label="",
        type=TEXT,
        *,
        validate=None,
        name=None,
        value=None,
        action=None,
        onchange=None,
        placeholder=None,
        required=None,
        readonly=None,
        datalist=None,
        help_text=None,
        **other_html_attrs
    ):
        self.kw = locals()
        self.label = label
        self.type = type
        self.validate = validate
        self.name = name
        self.value = value
        self.action = action
        self.onchange = onchange
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.datalist = datalist
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class Textarea(BaseInput):
    def __init__(
        self,
        label="",
        *,
        rows=6,
        code=None,
        maxlength=None,
        minlength=None,
        validate=None,
        name=None,
        value=None,
        onchange=None,
        placeholder=None,
        required=None,
        readonly=None,
        help_text=None,
        **other_html_attrs
    ):
        self.kw = locals()
        self.label = label
        self.rows = rows
        self.code = code
        self.maxlength = maxlength
        self.minlength = minlength
        self.validate = validate
        self.name = name
        self.value = value
        self.onchange = onchange
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class Select(BaseInput):
    def __init__(
        self,
        label="",
        options=None,
        *,
        multiple=None,
        validate=None,
        name=None,
        value=None,
        onchange=None,
        required=None,
        help_text=None,
        **other_html_attrs
    ):  
        self.kw = locals()
        self.label = label
        self.options = options
        self.multiple = multiple
        self.validate = validate
        self.name = name
        self.value = value
        self.onchange = onchange
        self.required = required
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class Checkbox(BaseInput):
    def __init__(
        self,
        label="",
        options=None,
        *,
        inline=None,
        validate=None,
        name=None,
        value=None,
        onchange=None,
        help_text=None,
        **other_html_attrs
    ):
        self.kw = locals()
        self.label = label
        self.options = options
        self.inline = inline
        self.validate = validate
        self.name = name
        self.value = value
        self.onchange = onchange
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class Radio(BaseInput):
    def __init__(
        self,
        label="",
        options=None,
        *,
        inline=None,
        validate=None,
        name=None,
        value=None,
        onchange=None,
        help_text=None,
        **other_html_attrs
    ):
        self.kw = locals()
        self.label = label
        self.options = options
        self.inline = inline
        self.validate = validate
        self.name = name
        self.value = value
        self.onchange = onchange
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class Slider(BaseInput):
    def __init__(
        self,
        label="",
        *,
        name=None,
        value=0,
        min_value=0,
        max_value=100,
        step=1,
        validate=None,
        onchange=None,
        required=None,
        help_text=None,
        **other_html_attrs
    ):
        self.kw = locals()
        self.label = label
        self.name = name
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.validate = validate
        self.onchange = onchange
        self.required = required
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class Actions(BaseInput):
    def __init__(self, label="", buttons=None, name=None, help_text=None):
        self.kw = locals()
        self.label = label
        self.buttons = buttons
        self.name = name
        self.help_text = help_text


class FileUpload(BaseInput):
    def __init__(
        self,
        label="",
        accept=None,
        name=None,
        placeholder="Choose file",
        multiple=False,
        max_size=0,
        max_total_size=0,
        required=None,
        help_text=None,
        **other_html_attrs
    ):
        self.kw = locals()
        self.label = label
        self.accept = accept
        self.name = name
        self.placeholder = placeholder
        self.multiple = multiple
        self.max_size = max_size
        self.max_total_size = max_total_size
        self.required = required
        self.help_text = help_text
        self.other_html_attrs = other_html_attrs


class InputGroup(BaseInput):
    def __init__(self, label="", inputs=None, validate=None, cancelable=False):
        self.kw = locals()
        self.label = label
        self.inputs = inputs
        self.validate = validate
        self.cancelable = cancelable
