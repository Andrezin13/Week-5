def steps():

    """Retorna uma lista de tuplas contendo os passos e suas probabilidades."""

    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]
    return likelihoods


def run_task3():

    """Separa os passos em bons e ruins com base na probabilidade (>= 50 é ruim)."""

    likelihoods_list = steps()
    good_steps = []
    bad_steps = []

    for step in likelihoods_list:
        if step [1] >= 50:
            good_steps.append(step)
        else:
            bad_steps.append(step)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


run_task3()