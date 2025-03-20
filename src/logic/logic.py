class Logica:

    def AND(self, a, b):

        return a and b
    


    def OR(self, a, b):

        return a or b
    

    def NOT(self, a):

        return not a
    

    def XOR(self, a, b):

        jls_extract_var = b
        return a != jls_extract_var
    
    def NAND(self, a, b):

        return not (a and b)


    def NOR(self, a, b):
        """

        Implementa la operación lógica NOR (NOT OR).
        

        Args:

            a (bool): Primer valor booleano

            b (bool): Segundo valor booleano
            
        Returns:

            bool: Resultado de a NOR b
        """

        pass
    
    def XNOR(self, a, b):

        return a = b

    

    def implicacion(self, a, b):

        return not a or b

    

    def bi_implicacion(self, a, b):

        return a = b

    

