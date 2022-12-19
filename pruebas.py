import os
archivo = open("Salida.dot", 'w', encoding='utf-8')
archivo.write('digraph G { \n')
archivo.write('fontname="Helvetica,Arial,sans-serif"  \n')
archivo.write('node [fontname="Helvetica,Arial,sans-serif"] \n')
archivo.write('edge [fontname="Helvetica,Arial,sans-serif"]\n')
archivo.write('a0 [shape=none  label=<\n')
archivo.write('<TABLE border="0" cellspacing="10" cellpadding="10" >\n')
for i in range(10):
    archivo.write('<TR>\n')
    for j in range(10):
        archivo.write('<TD style="radial" bgcolor="yellow"  gradientangle="60">'+str(i)+str(j)+'</TD>\n')
    archivo.write('</TR>\n')
archivo.write('</TABLE>>]; \n')
archivo.write('}\n')
archivo.close()
os.system('dot -Tpng Salida.dot -o Salida.png')