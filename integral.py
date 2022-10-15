import scipy.integrate as integrate
import scipy.special as special
resultado = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
resultado

