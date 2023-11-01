import csv
from datetime import datetime
from tqdm import tqdm
from ..models import RNC
from django.db import IntegrityError

def agregar_datos_desde_csv(file_path, batch_size=1000):
    total_registros = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Omitir la primera línea si contiene encabezados

            registros_lote = []
            pbar = tqdm(total=0, unit=' registros')  # Inicializar la barra de progreso (asegúrate de importar tqdm)

            for row in csv_reader:
                if len(row) == 11:
                    rnc = row[0]
                    if not RNC.objects.filter(rnc=rnc).exists():  # Verificar si ya existe un registro con el mismo RNC
                        fecha = row[8].strip()
                        if fecha and fecha != '00/00/0000':
                            try:
                                fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
                            except ValueError:
                                print(f'Error: Fecha no válida para RNC {rnc}: {fecha}')
                                fecha = None  # Asignar None si la fecha no es válida
                        else:
                            fecha = None  # Asignar None si la fecha está en blanco

                        # Crear una instancia del modelo RNC y agregarla al lote
                        nuevo_registro = RNC(
                            rnc=rnc,
                            nombre_apellido=row[1],
                            actividad_economica=row[3],
                            fecha=fecha,
                            estado=row[9],
                            tipo_contribuyente=row[10]
                        )

                        registros_lote.append(nuevo_registro)

                    if len(registros_lote) >= batch_size:
                        try:
                            RNC.objects.bulk_create(registros_lote)
                            total_registros += len(registros_lote)
                            registros_lote = []  # Reiniciar el lote
                            pbar.update(batch_size)  # Actualizar la barra de progreso
                        except Exception as e:
                            print('Error al agregar registros a la base de datos', e)

            # Insertar cualquier lote restante
            if registros_lote:
                try:
                    RNC.objects.bulk_create(registros_lote)
                    total_registros += len(registros_lote)
                    pbar.update(len(registros_lote))  # Actualizar la barra de progreso con el lote restante
                except IntegrityError as e:
                    print('Registros duplicados detectados. Se omitieron.', e)
                except Exception as e:
                    print('Error al agregar registros a la base de datos', e)

            pbar.close()  # Cerrar la barra de progreso al final

        print(f'Total de registros agregados: {total_registros}')
    except FileNotFoundError:
        print('El archivo CSV no existe.')

