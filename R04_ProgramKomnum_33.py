from math import factorial

def round2(x):
    return round(x, 2)

class NewtonGregoryForwardCustom:
    def __init__(self, deltas, h):
        self.delta_f0 = deltas[0]
        self.delta2_f0 = deltas[1]
        self.delta3_f0 = deltas[2]
        self.delta4_f0 = deltas[3]
        self.h = h

    def derivative(self, x, x0):
        # s
        s = round2((x - x0) / self.h)  

        # Term 1
        term1 = self.delta_f0

        # Term 2
        coef2 = round2((2 * s - 1) / factorial(2))
        term2 = round2(coef2 * self.delta2_f0)

        # Term 3
        numerator3 = round2(round2(3 * round2(s * s)) - round2(6 * s) + 2)
        coef3 = round2(numerator3 / factorial(3))
        term3 = round2(coef3 * self.delta3_f0)

        # Term 4
        part1 = round2(4 * round2(round2(s * s) * s))  
        part2 = round2(18 * round2(s * s)) 
        part3 = round2(22 * s)  
        numerator4 = round2(part1 - part2 + part3 - 6)
        coef4 = round2(numerator4 / factorial(4))
        term4 = round2(coef4 * self.delta4_f0)


        total = term1 + term2 + term3 + term4
        f_prime = round2(total / self.h)

        return f_prime

deltas = [205940, 244032, 157152, 53760]
ng = NewtonGregoryForwardCustom(deltas, h=2)
hasil = ng.derivative(x=11, x0=10)
print("f'(11) =", hasil)
