def likelihood_min_max():

    """Cria a tupla de probabilidades e retorna o valor mínimo e máximo."""
    likelihoods = (50, 38, 27, 99, 4)
    likelihoods = (50,38,27,99,4)
    return min(likelihoods), max(likelihoods)

def run_task2():

    """Chama a função likelihood_min_max e exibe ambos os valores formatados."""
    min_value, max_value = likelihood_min_max()
    print(f"Minimum likelihood of falling {min_value}%")
    print(f"Maximum likelihood of falling {max_value}%")

if __name__ == "__main__":
    run_task2()