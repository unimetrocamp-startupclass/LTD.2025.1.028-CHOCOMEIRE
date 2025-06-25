def montar_item_carrinho(produto, quantidade, sabores_escolhidos=None, tema_escolhido=None, tipo_barra=None):
    """
    Monta o item do carrinho aplicando as regras de sabores e limites conforme o nome do produto.
    Adiciona suporte para temas (Delícias de Ninho) e tipo de barra (Branca, Meio Amargo).

    :param produto: dict com detalhes do produto (deve conter pelo menos 'id', 'nome', 'preco', 'imagem' opcional)
    :param quantidade: int
    :param sabores_escolhidos: lista de sabores escolhidos (opcional)
    :param tema_escolhido: tema escolhido para Delícias de Ninho (opcional)
    :param tipo_barra: tipo escolhido para barras (Branca, Meio Amargo, Dois Recheios) (opcional)
    :return: dict do item do carrinho
    """
    nome = produto['nome'].lower()
    sabores = []
    limite_sabores = 0
    tema = None
    tipo = None

    # Docinhos
    if 'meio cento de docinhos' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Moranguinho', 'Limão', 'Paçoquinha']
        limite_sabores = 2
    elif 'cento de docinhos' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Moranguinho', 'Limão', 'Paçoquinha']
        limite_sabores = 3

    # Bombom
    elif 'bombom ao leite' in nome:
        sabores = []  # Não permite escolha de sabores
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

    # Cone Trufado
    elif 'cone trufado' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Moranguinho', 'Limão', 'Paçoquinha', 'Nutella']
        limite_sabores = quantidade

    # Barras
    elif 'barra recheada (branca, meio amargo, dois recheios)' in nome:
        tipo = tipo_barra or None  # tipo deve ser informado na interface
        sabores = ['Brigadeiro', 'Beijinho',  'Moranguinho', 'Limão', 'Paçoquinha', 'Nutella']  # Exemplo, ajuste para seu contexto
        limite_sabores = 2
    elif 'barra recheada' in nome:
        sabores = ['Brigadeiro', 'Beijinho',  'Moranguinho', 'Limão', 'Paçoquinha', 'Nutella']
        limite_sabores = 1
    elif 'meia barra recheada (branca, meio amargo)' in nome:
        tipo = tipo_barra or None
        sabores = ['Brigadeiro', 'Beijinho',  'Moranguinho', 'Limão', 'Paçoquinha', 'Nutella']
        limite_sabores = 1
    elif 'meia barra ao leite recheada' in nome:
        sabores = ['Brigadeiro', 'Beijinho',  'Moranguinho', 'Limão', 'Paçoquinha', 'Nutella']
        limite_sabores = 1

    # Delícias de Ninho
    elif 'delícias de ninho (unidade)' in nome or 'delícias de ninho (cento)' in nome:
        tema = tema_escolhido or None
        sabores = []  # Não há sabores, apenas tema
        limite_sabores = 0

    # Pão de Mel
    elif 'pão de mel grande' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Doce de Leite']
        limite_sabores = quantidade
    elif 'pão de mel pequeno' in nome:
        sabores = ['Brigadeiro', 'Beijinho', 'Doce de Leite']
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
        'sabores_escolhidos': sabores_escolhidos or [],
        'tema': tema,
        'tipo': tipo,
    }