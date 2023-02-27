def test_kwargs(arg1, arg2, **kwargs) -> None:
    """
    The function prints all arguments to standard output.
    """

    print(f"arg1 = {arg1}")
    print(f"arg2 = {arg2}")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

    print("\n")


test_kwargs("Carro", 100, nome="jose", chave="teste")

test_kwargs("Carro", 100, nome="jose", chave="teste",
            outrachave="brasil", oo="python")
