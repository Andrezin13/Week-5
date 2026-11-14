def likelihood():

    """Cria a tuple de probabilidades e retorna o menor valor."""

    likelihoods = (58,38,27,99,4)
    return min(likelihoods)

def run_task1():

    """Chama a função likelihood e exibe o resultado formatado."""

    min_likelihood = likelihood()
    print (f"Minimum likelihood of falling {min_likelihood}%")


# Bloco para executar o programa diretamente
if __name__ == "__main__":

    run_task1()
