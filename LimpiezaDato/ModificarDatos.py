import csv
from datetime import date

with open('/home/axel/Descargas/sisver_public.csv') as File:
    reader = csv.DictReader(File)
    misDatos = [['sexo','entresi','evoluci','intubado','edad','estaemba',
                'mesesemb','esindige','ocupacio','diassint','fiebre','tos',
                'odinogia','disnea','irritabi','diarrea','dotoraci','calofrios',
                'cefalea','mialgias','artral','ataedoge','rinorrea','polipnea',
                'vomito','dolabdo','conjun','cianosis','inisubis','diabetes',
                'epoc','asma','inmusupr','hiperten','vih_sida','otracon',
                'enfcardi','obesidad','insrencr','tabaquis','antivira',
                'conocaso','contaves','concerdo','conanima','vacunado',
                'resdefin','puerperio','diaspuerp','antipireticos','uci',
                'viaje']]
    miArchivo = open('salida.csv','w')
    with miArchivo:
        writer = csv.writer(miArchivo)
        writer.writerows(misDatos)
        for row in reader:
            if row['sexo'] == 'MASCULINO':
                sexo = 1
            else:
                sexo = 0

            if row['entresi'] == 'AGUASCALIENTES':
                entresi = 1
            elif row['entresi'] == 'BAJA CALIFORNIA':
                entresi = 2
            elif row['entresi'] == 'BAJA CALIFORNIA SUR':
                entresi = 3
            elif row['entresi'] == 'CAMPECHE':
                entresi = 4
            elif row['entresi'] == 'CHIAPAS':
                entresi = 5
            elif row['entresi'] == 'CHIHUAHUA':
                entresi = 6
            elif row['entresi'] == 'CIUDAD DE MEXICO':
                entresi = 7
            elif row['entresi'] == 'COAHUILA':
                entresi = 8
            elif row['entresi'] == 'COLIMA':
                entresi = 9
            elif row['entresi'] == 'DURANGO':
                entresi = 10
            elif row['entresi'] == 'GUANAJUATO':
                entresi = 11
            elif row['entresi'] == 'GUERRERO':
                entresi = 12
            elif row['entresi'] == 'HIDALGO':
                entresi = 13
            elif row['entresi'] == 'JALISCO':
                entresi = 14
            elif row['entresi'] == 'MEXICO':
                entresi = 15
            elif row['entresi'] == 'MICHOACAN':
                entresi = 16
            elif row['entresi'] == 'MORELOS':
                entresi = 17
            elif row['entresi'] == 'NAYARIT':
                entresi = 18
            elif row['entresi'] == 'NUEVO LEON':
                entresi = 19
            elif row['entresi'] == 'OAXACA':
                entresi = 20
            elif row['entresi'] == 'PUEBLA':
                entresi = 21
            elif row['entresi'] == 'QUERETARO':
                entresi = 22
            elif row['entresi'] == 'QUINTANA ROO':
                entresi = 23
            elif row['entresi'] == 'SAN LUIS POTOSI':
                entresi = 24
            elif row['entresi'] == 'SINALOA':
                entresi = 25
            elif row['entresi'] == 'SONORA':
                entresi = 26
            elif row['entresi'] == 'TABASCO':
                entresi = 27
            elif row['entresi'] == 'TAMAULIPAS':
                entresi = 28
            elif row['entresi'] == 'TLAXCALA':
                entresi = 29
            elif row['entresi'] == 'VERACRUZ':
                entresi = 30
            elif row['entresi'] == 'YUCATAN':
                entresi = 31
            elif row['entresi'] == 'ZACATECAS':
                entresi = 32
            else:
                entresi = -1

            if row['evoluci'] == 'CASO NO GRAVE':
                evoluci = 0
            elif row['evoluci'] == 'CASO GRAVE -':
                evoluci = 1
            elif row['evoluci'] == 'ALTA - CURACION':
                evoluci = 2
            elif row['evoluci'] == 'ALTA - MEJORIA':
                evoluci = 3
            elif row['evoluci'] == 'ALTA - TRASLADO':
                evoluci = 4
            elif row['evoluci'] == 'ALTA - VOLUNTARIA':
                evoluci = 5
            elif row['evoluci'] == 'CASO GRAVE - TRASLADO':
                evoluci = 6
            elif row['evoluci'] == 'DEFUNCION':
                evoluci = 7
            elif row['evoluci'] == 'EN TRATAMIENTO':
                evoluci = 8
            elif row['evoluci'] == 'REFERENCIA':
                evoluci = 9
            elif row['evoluci'] == 'SEGUIMIENTO DOMICILIARIO':
                evoluci = 10
            elif row['evoluci'] == 'SEGUIMIENTO TERMINADO':
                evoluci = 11
            else:
                evoluci = -1

            if row['intubado'] == 'SI':
                intubado = 1
            elif row['intubado'] == 'NO':
                intubado = 0
            else:
                intubado = -1

            edad = int(row['edad'])

            mesesemb = -1
            if row['estaemba'] == 'NO':
                estaemba = 0
            elif row['estaemba'] == 'SI':
                estaemba = 1
                if row['mesesemb'] == 'NA':
                    mesesemb = -1
                else:
                    mesesemb = int(row['mesesemb'])
            elif row['estaemba'] == 'SE IGNORA':
                estaemba = 2
            else:
                estaemba = -1

            if row['esindige'] == 'SI':
                esindige = 1
            elif row['esindige'] == 'NO':
                esindige = 0
            else:
                esindige = -1

            if row['ocupacio'] == 'CAMPESINOS':
                ocupacio = 1
            elif row['ocupacio'] == 'CHOFERES':
                ocupacio = 2
            elif row['ocupacio'] == 'COMERCIANTES DE MERCADOS FIJOS O AMBULANTES':
                ocupacio = 3
            elif row['ocupacio'] == 'DENTISTA':
                ocupacio = 4
            elif row['ocupacio'] == 'DESEMPLEADOS':
                ocupacio = 5
            elif row['ocupacio'] == 'EMPLEADOS':
                ocupacio = 6
            elif row['ocupacio'] == 'ENFERMERAS':
                ocupacio = 7
            elif row['ocupacio'] == 'ESTUDIANTES':
                ocupacio = 8
            elif row['ocupacio'] == 'GERENTES O PROPIETARIOS DE EMPRESAS O NEGOCIOS':
                ocupacio = 9
            elif row['ocupacio'] == 'HOGAR':
                ocupacio = 10
            elif row['ocupacio'] == 'JUBILADO / PENSIONADO':
                ocupacio = 11
            elif row['ocupacio'] == 'LABORATORISTA':
                ocupacio = 12
            elif row['ocupacio'] == 'MAESTROS':
                ocupacio = 13
            elif row['ocupacio'] == 'MEDICOS':
                ocupacio = 14
            elif row['ocupacio'] == 'OBREROS':
                ocupacio = 15
            elif row['ocupacio'] == 'OTROS':
                ocupacio = 16
            elif row['ocupacio'] == 'OTROS PROFESIONISTAS':
                ocupacio = 17
            elif row['ocupacio'] == 'OTROS TRABAJADORES DE LA SALUD':
                ocupacio = 18
            else:
                ocupacio = -1

            fecingre = row['fecingre']
            fecinisi = row['fecinisi']
            fecha1 = date(int(fecingre[0:4]),int(fecingre[5:7]),int(fecingre[8:10]))
            fecha2 = date(int(fecinisi[0:4]),int(fecinisi[5:7]),int(fecinisi[8:10]))

            diassint = (fecha1-fecha2).days

            if row['fiebre'] == 'SI':
                fiebre = 1
            elif row['fiebre'] == 'NO':
                fiebre = 0
            else:
                fiebre = -1

            if row['tos'] == 'SI':
                tos = 1
            elif row['tos'] == 'NO':
                tos = 0
            else:
                tos = -1

            if row['odinogia'] == 'SI':
                odinogia = 1
            elif row['odinogia'] == 'NO':
                odinogia = 0
            else:
                odinogia = -1

            if row['disnea'] == 'SI':
                disnea = 1
            elif row['disnea'] == 'NO':
                disnea = 0
            else:
                disnea = -1

            if row['irritabi'] == 'SI':
                irritabi = 1
            elif row['irritabi'] == 'NO':
                irritabi = 0
            else:
                irritabi = -1

            if row['diarrea'] == 'SI':
                diarrea = 1
            elif row['diarrea'] == 'NO':
                diarrea = 0
            else:
                diarrea = -1

            if row['dotoraci'] == 'SI':
                dotoraci = 1
            elif row['dotoraci'] == 'NO':
                dotoraci = 0
            else:
                dotoraci = -1

            if row['calofrios'] == 'SI':
                calofrios = 1
            elif row['calofrios'] == 'NO':
                calofrios = 0
            else:
                calofrios = -1

            if row['cefalea'] == 'SI':
                cefalea = 1
            elif row['cefalea'] == 'NO':
                cefalea = 0
            else:
                cefalea = -1

            if row['mialgias'] == 'SI':
                mialgias = 1
            elif row['mialgias'] == 'NO':
                mialgias = 0
            else:
                mialgias = -1

            if row['artral'] == 'SI':
                artral = 1
            elif row['artral'] == 'NO':
                artral = 0
            else:
                artral = -1

            if row['ataedoge'] == 'SI':
                ataedoge = 1
            elif row['ataedoge'] == 'NO':
                ataedoge = 0
            else:
                ataedoge = -1

            if row['rinorrea'] == 'SI':
                rinorrea = 1
            elif row['rinorrea'] == 'NO':
                rinorrea = 0
            else:
                rinorrea = -1

            if row['polipnea'] == 'SI':
                polipnea = 1
            elif row['polipnea'] == 'NO':
                polipnea = 0
            else:
                polipnea = -1

            if row['vomito'] == 'SI':
                vomito = 1
            elif row['vomito'] == 'NO':
                vomito = 0
            else:
                vomito = -1

            if row['dolabdo'] == 'SI':
                dolabdo = 1
            elif row['dolabdo'] == 'NO':
                dolabdo = 0
            else:
                dolabdo = -1

            if row['conjun'] == 'SI':
                conjun = 1
            elif row['conjun'] == 'NO':
                conjun = 0
            else:
                conjun = -1

            if row['cianosis'] == 'SI':
                cianosis = 1
            elif row['cianosis'] == 'NO':
                cianosis = 0
            else:
                cianosis = -1

            if row['inisubis'] == 'SI':
                inisubis = 1
            elif row['inisubis'] == 'NO':
                inisubis = 0
            else:
                inisubis = -1

            if row['diabetes'] == 'SI':
                diabetes = 1
            elif row['diabetes'] == 'NO':
                diabetes = 0
            else:
                diabetes = -1

            if row['epoc'] == 'SI':
                epoc = 1
            elif row['epoc'] == 'NO':
                epoc = 0
            else:
                epoc = -1

            if row['asma'] == 'SI':
                asma = 1
            elif row['asma'] == 'NO':
                asma = 0
            else:
                asma = -1

            if row['inmusupr'] == 'SI':
                inmusupr = 1
            elif row['inmusupr'] == 'NO':
                inmusupr = 0
            else:
                inmusupr = -1

            if row['hiperten'] == 'SI':
                hiperten = 1
            elif row['hiperten'] == 'NO':
                hiperten = 0
            else:
                hiperten = -1

            if row['vih_sida'] == 'SI':
                vih_sida = 1
            elif row['vih_sida'] == 'NO':
                vih_sida = 0
            else:
                vih_sida = -1

            if row['otracon'] == 'SI':
                otracon = 1
            elif row['otracon'] == 'NO':
                otracon = 0
            else:
                otracon = -1

            if row['enfcardi'] == 'SI':
                enfcardi = 1
            elif row['enfcardi'] == 'NO':
                enfcardi = 0
            else:
                enfcardi = -1

            if row['obesidad'] == 'SI':
                obesidad = 1
            elif row['obesidad'] == 'NO':
                obesidad = 0
            else:
                obesidad = -1

            if row['insrencr'] == 'SI':
                insrencr = 1
            elif row['insrencr'] == 'NO':
                insrencr = 0
            else:
                insrencr = -1

            if row['tabaquis'] == 'SI':
                tabaquis = 1
            elif row['tabaquis'] == 'NO':
                tabaquis = 0
            else:
                tabaquis = -1

            if row['antivira'] == 'NO ESPECIFICA':
                antivira = 0
            elif row['antivira'] == 'ACICLOVIR':
                antivira = 1
            elif row['antivira'] == 'AMANTADINA':
                antivira = 2
            elif row['antivira'] == 'RITONAVIR':
                antivira = 3
            elif row['antivira'] == 'KALETRA':
                antivira = 4
            elif row['antivira'] == 'LOPINAVIR':
                antivira = 5
            elif row['antivira'] == 'OSELTAMIVIR':
                antivira = 6
            elif row['antivira'] == 'RIMANTADINA':
                antivira = 7
            elif row['antivira'] == 'ZANAMIVIR':
                antivira = 8
            else:
                antivira = -1

            if row['conocaso'] == 'SI':
                conocaso = 1
            elif row['conocaso'] == 'NO':
                conocaso = 0
            else:
                conocaso = -1

            if row['contaves'] == 'SI':
                contaves = 1
            elif row['contaves'] == 'NO':
                contaves = 0
            else:
                contaves = -1

            if row['concerdo'] == 'SI':
                concerdo = 1
            elif row['concerdo'] == 'NO':
                concerdo = 0
            else:
                concerdo = -1

            animal = row['conanima']
            if animal[0] == 'N':
                conanima = 0
            elif animal == 'SIN DATO':
                conanima = -1
            else:
                conanima = 1

            if row['vacunado'] == 'SI':
                vacunado = 1
            elif row['vacunado'] == 'NO':
                vacunado = 0
            else:
                vacunado = -1

            if row['resdefin'] == 'NEGATIVO':
                resdefin = 0
            elif row['resdefin'] == 'SARS-CoV-2':
                resdefin = 1
            elif row['resdefin'] == 'AH3':
                resdefin = 2
            elif row['resdefin'] == 'CORONA HKU1':
                resdefin = 3
            elif row['resdefin'] == 'CORONA HNL63':
                resdefin = 4
            elif row['resdefin'] == 'ENTEROV / RHINOVIRUS':
                resdefin = 5
            elif row['resdefin'] == 'INF 1':
                resdefin = 6
            elif row['resdefin'] == 'INF AH1N1 PMD':
                resdefin = 7
            elif row['resdefin'] == 'NO ADECUADO':
                resdefin = 8
            elif row['resdefin'] == 'NO RECIBIDA':
                resdefin = 9
            elif row['resdefin'] == 'NO SUBTIPICADO':
                resdefin = 10
            elif row['resdefin'] == 'PARAINFLIENCIA 1':
                resdefin = 11
            elif row['resdefin'] == 'PARAINFLIENCIA 2':
                resdefin = 12
            elif row['resdefin'] == 'RECHAZADA':
                resdefin = 13
            elif row['resdefin'] == 'VSR':
                resdefin = 14
            else:
                resdefin = -1

            diaspuerp = -1
            if row['puerperio'] == 'SI':
                puerperio = 1
                diaspuerp = int(row['diaspuerp'])
            elif row['puerperio'] == 'NO':
                puerperio = 0
            else:
                puerperio = -1

            if row['antipireticos'] == 'SI':
                antipireticos = 1
            elif row['antipireticos'] == 'NO':
                antipireticos = 0
            else:
                antipireticos = -1

            if row['uci'] == 'SI':
                uci = 1
            elif row['uci'] == 'NO':
                uci = 0
            else:
                uci = -1

            if row['viaje1'] == 'NA':
                viaje = 0
            else:
                viaje = 1

            misDatos = [[sexo,entresi,evoluci,intubado,edad,estaemba,
                        mesesemb,esindige,ocupacio,diassint,fiebre,tos,
                        odinogia,disnea,irritabi,diarrea,dotoraci,calofrios,
                        cefalea,mialgias,artral,ataedoge,rinorrea,polipnea,
                        vomito,dolabdo,conjun,cianosis,inisubis,diabetes,
                        epoc,asma,inmusupr,hiperten,vih_sida,otracon,
                        enfcardi,obesidad,insrencr,tabaquis,antivira,
                        conocaso,contaves,concerdo,conanima,vacunado,
                        resdefin,puerperio,diaspuerp,antipireticos,uci,
                        viaje]]
            writer.writerows(misDatos)
