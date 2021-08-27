from collections import deque

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """


    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    indexLacuna = estado.find("_")
    listaEstadosVálidos:list = []

    if indexLacuna - 1 >= 0 and indexLacuna % 3 != 0:
        charTrocado = estado[indexLacuna - 1]
        novoEstado = estado.replace(charTrocado, '*')
        novoEstado = novoEstado.replace('_', charTrocado)
        novoEstado = novoEstado.replace('*', '_')

        tupla = ("esquerda", novoEstado)
        listaEstadosVálidos.append(tupla)

    if indexLacuna + 1 <= 8 and indexLacuna % 3 != 2:
        charTrocado = estado[indexLacuna + 1]
        novoEstado = estado.replace(charTrocado, '*')
        novoEstado = novoEstado.replace('_', charTrocado)
        novoEstado = novoEstado.replace('*', '_')

        tupla = ("direita", novoEstado)
        listaEstadosVálidos.append(tupla)

    if indexLacuna - 3 >= 0:
        charTrocado = estado[indexLacuna - 3]
        novoEstado = estado.replace(charTrocado, '*')
        novoEstado = novoEstado.replace('_', charTrocado)
        novoEstado = novoEstado.replace('*', '_')

        tupla = ("acima", novoEstado)
        listaEstadosVálidos.append(tupla)

    if indexLacuna + 3 <= 8:
        charTrocado = estado[indexLacuna + 3]
        novoEstado = estado.replace(charTrocado, '*')
        novoEstado = novoEstado.replace('_', charTrocado)
        novoEstado = novoEstado.replace('*', '_')

        tupla = ("abaixo", novoEstado)
        listaEstadosVálidos.append(tupla)

    return listaEstadosVálidos


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    listaSucessores = sucessor(nodo.estado)
    listaNodosFilhos = []

    for tuplaSucc in listaSucessores:
        novoNodo = Nodo(tuplaSucc[1], nodo, tuplaSucc[0], nodo.custo+1)
        listaNodosFilhos.append(novoNodo)

    return listaNodosFilhos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    nodoRaiz = Nodo(estado, None, None, 0)
    #nodoRaiz = Nodo("1234567_8", None, None, 0)


    X = {}
    F = deque([nodoRaiz])

    while True:
        if not F:
            return None
        v = F.popleft()
        if v.estado == "12345678_":
            listaRetorno = []
            while v.pai is not None:
                listaRetorno.append(v)
                v = v.pai
            return listaRetorno

            #retornar caminho
        if v.estado not in X:
            X[v.estado] = v.estado
            filhos = expande(v)
            for filho in filhos:
                if filho.estado not in X:
                    F.append(filho)

            #for filho in expande(v):
            #    F.append(filho)



def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
