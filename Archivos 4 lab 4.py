manejador_arch = open ('mbox.txt')
for linea in manejador_arch:
    linea = linea.upper()
    if linea.find('From:') == -1: continue
    print(linea)