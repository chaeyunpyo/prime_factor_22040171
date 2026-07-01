class PrimeFactor:
    def factorial(self, num):
        factor = []

        divide = 2
        while num > 1:
            if num % divide == 0:
                factor.append(divide)
                num = num // divide
            else :
                divide += 1
        return factor
