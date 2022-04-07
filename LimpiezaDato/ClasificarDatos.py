import csv
with open('/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/salida.csv') as File:
    reader = csv.DictReader(File)

    with open('salida2.csv','w') as csvfile:
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
        writer = csv.DictWriter(csvfile,fieldnames=misDatos)
        writer.writeheader()

        for row in reader:
            if row['resdefin'] == '0' or row['resdefin'] == '1':
                if row['evoluci'] == '0' or row['evoluci'] == '1':
                    writer.writerow(row)
