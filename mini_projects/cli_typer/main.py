import typer

app = typer.Typer()
state = {"verbose": False}

@app.command('hello')
def hello(name: str, lastname: str="", formal: bool = False):
    """
    Say hello to NAME, optionally with a --lastname.
    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")

@app.command('goodbye')
def goodbye(name: str, formal: bool = False):
    """
    Say goodbye to NAME.
    If --formal is used, say bye very formally.
    """
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.callback()
def main(verbose: bool = False):
    """
    Manage users in the awesome CLI app.
    """
    if verbose:
        print("Will write verbose output")
        state["verbose"] = True


if __name__ == "__main__":
   app()



"""
python main.py hello Camila --formal
Good day Ms. Camila .

python main.py hello Camila --lastname Cabello
Hello Camila Cabello.
"""