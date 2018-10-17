import matplotlib.pyplot as plt
from pypbe import PBE


def sim(n, d, ):
    alg = PBE(n, d, pbe_map='3e')
    alg.roll_mc()
    i = alg.plot_histogram()
    results = alg.get_results()
    plt.savefig('fig')
    return results
