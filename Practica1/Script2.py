class Nodo:
    def __init__(self, valor):
        """
        Constructor de la clase Nodo.
        Args:
            valor: El valor que contendra el nodo.
        """
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioOrdenado:
    def __init__(self):
        """
        Constructor de la clase ArbolBinarioOrdenado.
        Inicializa el arbol con una raiz nula.
        """
        self.raiz = None

    def agregar(self, valor):
        """
        Metodo para agregar un nuevo nodo con un valor dado al arbol.
        Args:
            valor: El valor del nuevo nodo.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo):
        """
        Metodo privado para agregar recursivamente un nodo a un subarbol.
        Args:
            valor: El valor del nuevo nodo.
            nodo: El nodo actual en el subarbol.
        """
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo.derecho)

    def recorrido_preorden(self):
        """
        Realiza un recorrido preorden en el arbol.
        Returns:
            Una lista con los valores en el recorrido preorden.
        """
        return self._recorrido_preorden_recursivo(self.raiz)

    def _recorrido_preorden_recursivo(self, nodo):
        """
        Metodo privado para realizar el recorrido preorden recursivamente.
        Args:
            nodo: El nodo actual en el recorrido.
        Returns:
            Una lista con los valores en el recorrido preorden.
        """
        if nodo is None:
            return []
        return [nodo.valor] + self._recorrido_preorden_recursivo(nodo.izquierdo) + self._recorrido_preorden_recursivo(nodo.derecho)

    def recorrido_inorden(self):
        """
        Realiza un recorrido inorden en el arbol.
        Returns:
            Una lista con los valores en el recorrido inorden.
        """
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        """
        Metodo privado para realizar el recorrido inorden recursivamente.
        Args:
            nodo: El nodo actual en el recorrido.
        Returns:
            Una lista con los valores en el recorrido inorden.
        """
        if nodo is None:
            return []
        return self._recorrido_inorden_recursivo(nodo.izquierdo) + [nodo.valor] + self._recorrido_inorden_recursivo(nodo.derecho)

    def recorrido_postorden(self):
        """
        Realiza un recorrido postorden en el arbol.
        Returns:
            Una lista con los valores en el recorrido postorden.
        """
        return self._recorrido_postorden_recursivo(self.raiz)

    def _recorrido_postorden_recursivo(self, nodo):
        """
        Metodo privado para realizar el recorrido postorden recursivamente.
        Args:
            nodo: El nodo actual en el recorrido.
        Returns:
            Una lista con los valores en el recorrido postorden.
        """
        if nodo is None:
            return []
        return self._recorrido_postorden_recursivo(nodo.izquierdo) + self._recorrido_postorden_recursivo(nodo.derecho) + [nodo.valor]


def contar_valles(caminata):
    """
    Funcion para contar valles en una secuencia de pasos de una caminata.
    Args:
        caminata: La secuencia de pasos de la caminata.
    Returns:
        El numero de valles en la caminata.
    """
    nivel = 0
    valles = 0

    for paso in caminata:
        if paso == 'U':
            nivel += 1
            if nivel == 0:
                valles += 1
        else:
            nivel -= 1

    return valles


if __name__ == "__main__":
    # Ingresar los datos del arbol binario
    print("Ingrese los valores del árbol binario separados por espacios:")
    datos_arbol = list(map(int, input().split()))

    # Crear un arbol binario ordenado y agregar elementos
    arbol = ArbolBinarioOrdenado()
    for dato in datos_arbol:
        arbol.agregar(dato)

    # Imprimir recorridos del arbol
    print("Recorrido Preorden:", arbol.recorrido_preorden())
    print("Recorrido Inorden:", arbol.recorrido_inorden())
    print("Recorrido Postorden:", arbol.recorrido_postorden())

    # Ingresar la caminata
    print("Ingrese la secuencia de pasos de la caminata (U para arriba, D para abajo) la cadena debe pasarse sin espacios:")
    caminata = input()

    # Ejemplo de contar valles en la caminata ingresada
    print("Número de valles:", contar_valles(caminata))