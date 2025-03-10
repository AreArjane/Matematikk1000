
import numpy as np 
import math as m

class Complex: 

    def tetha_add(self, real, imaginary):
        
        while(real > 0):
            if(imaginary > 0):
                tetha = m.atan(imaginary/real)
                break
            elif(imaginary < 0):
                tetha = m.atan(imaginary/real) + 2*m.pi
                break 
            elif(imaginary == 0):
                tetha = 0
                break
            else:
                break
        while(real < 0):
            tetha = m.atan(imaginary/ real) + m.pi 
            break
        while(real == 0):
            if(imaginary < 0):
                tetha =  -m.pi/2
                break
            elif(imaginary > 0):
                tetha = m.pi/2
                break
            elif(imaginary == 0):
                tetha = None
                break
        return tetha

               
    
    
    def ComplexCalculator(self, n,product):
        product = product.replace(" ", "").replace("i", "j")
        
        if "/" in product: 
            
            num_str , den_str = product.split("/")
            
            
            try: 
                numerator   = complex(num_str)
                denominator = complex(den_str)
                print(numerator)
                print(denominator)
                
                result = numerator / denominator
                
                relle_nr     = np.real(result)
                imaginary_nr = np.imag(result)
                print("The real number is : " , relle_nr)
                print("The imaginary number is : " , imaginary_nr)
                
                r = m.sqrt((relle_nr**2)+(imaginary_nr**2))
                print("The R is : " , r)
                
                tan_tetha = self.tetha_add(relle_nr, imaginary_nr)
                
                
                
                print("The invers tanginus is : " , tan_tetha)
        
                
            except ValueError:
                raise ValueError("Format in complex number is not applicable")
        else:

            try:
                product = complex(product)
                print("The product is here", product)
                relle_nr = np.real(product)
                imaginary_nr = np.imag(product)
                print("The real number is : " , relle_nr)
                print("The imaginary number is : " , imaginary_nr)
            
                r = m.sqrt((relle_nr**2)+(imaginary_nr**2))
                print("The R is : " , r)

                tan_tetha = self.tetha_add(relle_nr, imaginary_nr)
                
                
                
                print("The invers tanginus is : " , tan_tetha)
                
            except ValueError:
                raise ValueError("Format in complex number is not applicable")
   






test = Complex()
#test.ComplexCalculator("2 - j / 2 + 3j")
#test.ComplexCalculator("2+2i")
#test.ComplexCalculator("3.17-1.14i")
#test.ComplexCalculator("-1+2i")
#test.ComplexCalculator("-i")
test.ComplexCalculator(1,"1")
