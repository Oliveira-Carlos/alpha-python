def teste_args(param, other_param, *args) -> None:
    """
    The function prints all arguments to standard output.
    """

    print(param)
    print(other_param)
    for arg in args:
        print(arg)

    print("\n")


teste_args("carlos", "oliveira", 24, "python")

teste_args("Carro", 100, 50, "Pedra")

teste_args("brasil", "Paí", "Mundo", "Carro", 100, 50, "Pedra")

teste_args("brasil", "País", "Gol", "Carro", 10)
