import csv

i = 1

with open('/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/salida3.csv') as File:
    reader = csv.DictReader(File)
    with open('entrenamiento.csv','w') as entrenamiento:
        with open('prueba.csv','w') as prueba:
            misDatos = ['sexo','entresi','edad','estaemba','mesesemb','esindige',
                        'ocupacio','diassint','fiebre','tos','odinogia','disnea',
                        'irritabi','diarrea','dotoraci','calofrios','cefalea',
                        'mialgias','artral','ataedoge','rinorrea','polipnea','vomito',
                        'dolabdo','conjun','cianosis','inisubis','diabetes','epoc',
                        'asma','inmusupr','hiperten','vih_sida','otracon','enfcardi',
                        'obesidad','insrencr','tabaquis','antivira','conocaso',
                        'contaves','concerdo','conanima','vacunado','puerperio',
                        'diaspuerp','antipireticos','viaje','resdefin','evoluci',
                        'intubado','uci']
            writeEn = csv.DictWriter(entrenamiento,fieldnames=misDatos)
            writePr = csv.DictWriter(prueba,fieldnames=misDatos)
            writeEn.writeheader()
            writePr.writeheader()

            for row in reader:
                if i <= 8:
                    writeEn.writerow(row)
                else:
                    writePr.writerow(row)
                    if i == 10:
                        i = 0
                i = i + 1
