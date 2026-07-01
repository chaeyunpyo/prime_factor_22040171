class PrimeFactor:
    def factorial(self, num):
        factor = []

        if num == 4 :
            self.factorial(2)
            self.factorial(2)
        if num == 6 :
            self.factorial(2)
            self.factorial(3)
        if num > 1 :
            factor.append(num)

        return factor
