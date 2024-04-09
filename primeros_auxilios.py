print('Pasos a seguir en caso de una Emergencia Medica')
injured = input('La persona accidentada responde a estimulos? Si/No: ')
injured = injured.lower()
if injured == 'si': 
    print('Valorar la necesidad de llevarlo al hospital mas cercano')
    print('Ha finalizado los pasos a seguir en una emergenica')
elif injured == 'no':
    print('Abrir la via Aérea')
    respira = input('¿Respira? si/no: ')
    respira = respira.lower()
    if respira == 'si':
        print('Permitirle posición de suficiente ventilación')
        print('Ha finalizado los pasos a seguir en una emergenica')
    elif respira == 'no':
        print('Administrar 5 ventilaciones y llamar a Ambulancia ')
        signos = input('¿Signos de Vida? si/no ')
        signos =signos.lower()
        if signos == 'si':
            print('Reevaluar a la espera de la Ambulancia')
            ambulancia = input('¿Llegó la Ambulancia? si/no ')
            ambulancia = ambulancia.lower()
        elif signos == 'no': 
            print('Administar compresiones torácicas hasta que llegue ambulancia')
            ambulancia = input('¿Llegó la Ambulancia? si/no ')
            ambulancia = ambulancia.lower()
        while (ambulancia == 'no'): 
            if ambulancia == 'no':
                        signos = input('¿Signos de Vida? si/no ')
                        signos =signos.lower()
                        if signos == 'si':
                            print('Reevaluar a la espera de la Ambulancia')
                            ambulancia = input('¿Llegó la Ambulancia? si/no ')
                            if ambulancia == 'si':
                                print('Ha finalizado los pasos a seguir en una emergenica')
                                break
                        elif signos == 'no': 
                            print('Administar compresiones torácicas hasta que llegue ambulancia')
                            ambulancia = input('¿Llegó la Ambulancia? si/no ')
                            ambulancia = ambulancia.lower()
                            print('Reevaluar a la espera de la Ambulancia')
                            input('¿Llegó la Ambulancia? si/no ')
                            if ambulancia == 'si':
                                print('Ha finalizado los pasos a seguir en una emergenica')
                                break
            elif ambulancia == 'si':
                print('Ha finalizado los pasos a seguir en una emergenica')