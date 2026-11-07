# Responsável: Pedro Guterres Jaeger Livi

def calcular_desconto(valor_pedido: float) -> float:
    """
    Calcula o desconto de um pedido no LocalEats:
    - Pedidos abaixo de R$ 100,00 não recebem desconto (retorna 0).
    - Pedidos de R$ 100,00 ou mais recebem 10% de desconto.
    - Valores negativos geram ValueError.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if valor_pedido >= 100:
        return valor_pedido * 0.10
    
    return 0.0