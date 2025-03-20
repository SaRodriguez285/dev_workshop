class Magic:

    
    def fibonacci(self, n):

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    
    def secuencia_fibonacci(self, n):

        secuencia = []
        for i in range(n):
            secuencia.append(self.fibonacci(i))
        return secuencia
    
    
    def es_primo(self, n):

        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    
    def generar_primos(self, n):

        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos
    
    
    def es_numero_perfecto(self, n):

        if n < 2:
            return False
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n


    def triangulo_pascal(self, filas):

        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo

    
    def factorial(self, n):

        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    
    def mcd(self, a, b):

        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):

        return abs(a * b) // self.mcd(a, b) if a and b else 0

        
    def suma_digitos(self, n):

        return sum(int(digito) for digito in str(abs(n)))

    def es_numero_armstrong(self, n):

        digitos = [int(d) for d in str(n)]
        potencia = len(digitos)
        return sum(d ** potencia for d in digitos) == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass
    

"Mañana tengo parcial de calculo y no he estudiado nada"
