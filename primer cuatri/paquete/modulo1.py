#7 
""" 
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
= 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1- (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
"""

def ventas_exportaciones (valor_exportaciones :float , retenciones :float = 15 ) -> float:
    '''
    ventas exportaciones con retenciones
    '''

    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
    return (resultado_exportaciones)
    

def ventas_nacional (valor_nacional :float , iva :float = 21 ) -> float:
    '''
    ventas nacionales con IVA
    '''
    resultado_nacional = valor_nacional *(1 / (1 + (iva / 100)))
    return (resultado_nacional)

def impuestos (resultado_nacional : float , resultado_exportaciones: float) -> float:
    resultado = resultado_exportaciones + resultado_nacional
    return resultado
