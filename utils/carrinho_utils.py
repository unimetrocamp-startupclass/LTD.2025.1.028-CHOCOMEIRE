def montar_item_carrinho(produto, quantidade, sabores_escolhidos=None):
    nome = produto['nome'].lower()
    sabores = []
    limite_sabores = 0

    if 'meio cento de docinhos' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Moranguinho', 'Limão', 'Paçoquinha']
        limite_sabores = 2
    elif 'cento de docinhos' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Moranguinho', 'Limão', 'Paçoquinha']
        limite_sabores = 3
    elif 'bombom ao leite' in nome:
        sabores = []
        limite_sabores = 0
    elif 'bombons sortidos' in nome:
        import re
        match = re.search(r'\(([^)]+)\)', produto['nome'])
        if match:
            sabores = [s.strip() for s in match.group(1).split(',')]
            limite_sabores = quantidade
        else:
            sabores = []
            limite_sabores = 0
    elif 'cone trufado' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Moranguinho', 'Limão', 'Paçoquinha']
        limite_sabores = quantidade
    else:
        sabores = []
        limite_sabores = 0

    return {
        'id': produto['id'],
        'nome': produto['nome'],
        'imagem': produto.get('imagem', ''),
        'quantidade': quantidade,
        'preco': produto['preco'],
        'subtotal': produto['preco'] * quantidade,
        'sabores': sabores,
        'limite_sabores': limite_sabores,
        'sabores_escolhidos': sabores_escolhidos or []
    }