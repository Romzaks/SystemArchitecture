class Vertex:
    def __init__(self, num, edges=None):
        edges = list(map(lambda x: int(x), edges))
        edges = sorted(edges)
        if num in edges:
            edges.pop(num)  # удаляем замыкание в себе
        self.__edges = edges
        self.__num = num
        self.__valence = len(self.__edges)

    def get_edges(self):
        m = list(map(lambda x: int(x), self.__edges))
        return m

    def get_valence(self):
        return self.__valence

    def reduce_valence(self):
        self.__valence -= 1

    def get_num(self):
        return self.__num

    def new_edge(self, edge):
        self.__edges.append(edge)


def main():
    v = init_matrix()
    print_matrix(v)
    t = build_tree_v2(v)
    print_matrix(t)


def init_matrix():
    n = int(input('Введите число вершин: '))
    v = list()
    for i in range(n):
        print(f'Введите связи с {i} вершиной')
        edges = input().split(' ')
        v.append(Vertex(i, edges))
    return v


def print_matrix(v):
    print('-', end='\t')
    for i in range(len(v)):
        print(i, end='\t')
    print()
    print()
    for i in range(len(v)):
        print(i, end='\t')
        for j in range(len(v)):
            if j in v[i].get_edges():
                print(1, end='\t')
            else:
                print(0, end='\t')
        print()
    print()


def build_tree_v2(v):
    t = list(range(len(v)))  # хранятся вершины деревьев
    v_all_num = set(range(len(v)))
    t_num = set()
    v_fut_num = v_all_num - t_num
    while len(v_fut_num) > 0:
        new_t = v_fut_num.pop()
        new_edges = set(v[new_t].get_edges())
        p = v_fut_num & new_edges
        q = t_num & new_edges
        for el in p:
            t[el] = (Vertex(el, [new_t]))
        if len(q) > 0:
            this_q = q.pop()
            p.add(this_q)
            t[new_t] = Vertex(new_t, list(p))
            (t[this_q]).new_edge(new_t)
            t_num |= set(p)
        else:
            t[new_t] = Vertex(new_t, list(p))
            t_num |= set(p)
        v_fut_num -= p
    return t


main()
