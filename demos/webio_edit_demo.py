from typewebio import *
from pywebio import start_server
from functools import partial

from pywebio.output import *


async def run_code():
    code = await pin.code
    with Scope.use_scope("web"):
        exec(code)


def edit_demo():

    # Create the main layoutthe main layout
    main = Scope("main")
    web = Scope("web")
    edit = Scope("edit")
    mc = Row([web, None, edit], size="50% 1% 49%")
    main.add_content(mc)

    # Create Edit layout
    edit.add_content(
        PinTextarea(
            "code",
            label="TypeWebIO Edit",
            rows=40,
            code={"mode": "python", "theme": "darcula"},
            value="from typewebio import *\n",
        )
    )

    edit.add_content(
        ButtonGroup(["Run", "Clear"], [run_code, partial(Scope.clear, "web")])
    )

    # Create Web layout
    web.add_content(Code("Hello World"))
    return main


app = edit_demo()


async def main_typewebio():
    Session.set_env(output_max_width="100%")
    app.show()


start_server(main_typewebio, port=8080, debug=True)
