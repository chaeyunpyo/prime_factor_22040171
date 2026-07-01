class PrimeFactor:
    def factorial(self, num):
        factor = []


        if num > 1 :
            if num == 4:
                while num > 1:
                    if num % 2 == 0:
                        factor.append(2)
                        num /= 2
            else : factor.append(num)

        return factor
