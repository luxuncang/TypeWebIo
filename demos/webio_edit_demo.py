from typewebio import *
from pywebio import start_server
from functools import partial


async def run_code():
    code = await pin.code
    with Scope.use_scope("webio_edit_demo_web"):
        exec(code)


def edit_demo():

    # Create the main layoutthe main layout
    main = Scope("webio_edit_demo_main")
    web = Scope("webio_edit_demo_web")
    edit = Scope("webio_edit_demo_edit")
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
        ButtonGroup(["Run", "Clear"], [run_code, partial(Scope.clear, "webio_edit_demo_web")])
    )

    # Create Web layout
    web.add_content(Code("Hello World"))
    return main


app = TypeWebIo("webio_edit_demo")
app.add_content(edit_demo())
app.run()
