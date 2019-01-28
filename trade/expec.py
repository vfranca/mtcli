# encoding: utf-8

def get_expec(taxa_acerto, ganho_medio, prejuizo_medio):
    """Calcula a expectativa matemática."""
    taxa_acerto = taxa_acerto / 100
    return (taxa_acerto * ganho_medio) - ((1 - taxa_acerto) * prejuizo_medio)

def era(expectativa,pm):
    return expectativa / pm
