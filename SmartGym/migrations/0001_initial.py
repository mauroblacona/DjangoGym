# Generated by Django 2.2 on 2020-02-19 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('capacidad', models.IntegerField(blank=True, null=True, verbose_name='Capacidad')),
                ('precio', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombre')),
                ('fecha_apertura', models.DateField(blank=True, null=True, verbose_name='Fecha Apertura')),
            ],
            options={
                'verbose_name': 'Consultorio',
                'verbose_name_plural': 'Consultorios',
            },
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('grupo_muscular', models.CharField(blank=True, choices=[('Piernas', 'Piernas'), ('Hombros', 'Hombros'), ('Biceps', 'Biceps'), ('Triceps', 'Triceps'), ('Pecho', 'Pecho'), ('Espalda', 'Espalda'), ('Core', 'Core'), ('Otro', 'Otro')], max_length=200, null=True, verbose_name='Grupo Muscular')),
            ],
            options={
                'verbose_name': 'Ejercicio',
                'verbose_name_plural': 'Ejercicios',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=120, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('genero', models.CharField(blank=True, choices=[('Indefinido', 'Indefinido'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, null=True, verbose_name='Genero')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('telefono_emergencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de Emergencia')),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Foto de Perfil')),
                ('ficha_medica', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ficha Medica')),
                ('especialidad', models.CharField(blank=True, max_length=200, null=True, verbose_name='Especialidad')),
                ('observaciones_medicas', models.TextField(blank=True, null=True, verbose_name='Observaciones Medicas')),
                ('status', models.CharField(blank=True, choices=[('AC', 'Activo'), ('IN', 'Inactivo')], max_length=150, null=True)),
                ('actividades', models.ManyToManyField(blank=True, to='SmartGym.Actividad')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hora de Inicio')),
                ('hora_fin', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hora de Fin')),
                ('dia', models.CharField(blank=True, choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=150, null=True, verbose_name='Dia de la Actividad')),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Actividad')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Empleado')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios de las Actividades',
            },
        ),
        migrations.CreateModel(
            name='PosibleCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, null=True, verbose_name='Apellido')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electronico')),
                ('fecha_consulta', models.DateField(blank=True, null=True, verbose_name='Fecha de Consulta')),
                ('actividad', models.TextField(blank=True, null=True, verbose_name='Actividad Consultada')),
            ],
            options={
                'verbose_name': 'Posible Cliente',
                'verbose_name_plural': 'Registro de Posibles Clientes',
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=120, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('genero', models.CharField(blank=True, choices=[('Indefinido', 'Indefinido'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, null=True, verbose_name='Genero')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('telefono_emergencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de Emergencia')),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Foto de Perfil')),
                ('profesion', models.CharField(blank=True, max_length=70, null=True, verbose_name='Profesion')),
                ('matricula', models.CharField(blank=True, max_length=50, null=True, verbose_name='Matricula')),
                ('fecha_desde', models.DateField(blank=True, null=True, verbose_name='Fecha Desde')),
                ('fecha_hasta', models.DateField(blank=True, null=True, verbose_name='Fecha Hasta')),
                ('status', models.CharField(blank=True, choices=[('AC', 'Activo'), ('IN', 'Inactivo')], max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Profesional',
                'verbose_name_plural': 'Profesionales',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombre')),
                ('telefono', models.CharField(blank=True, max_length=150, null=True, verbose_name='Telefono de Contacto')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('domicilio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Domicilio')),
                ('rubro', models.CharField(blank=True, max_length=120, null=True, verbose_name='Rubro')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('cuit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cuit')),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Monto')),
                ('saldo', models.BooleanField(blank=True, default=True, null=True, verbose_name='Al dia / Deuda')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('duracion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Duracion de la Rutina')),
                ('cantidad_dias', models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Dias Semanales')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Rutina',
                'verbose_name_plural': 'Rutinas',
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=120, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('genero', models.CharField(blank=True, choices=[('Indefinido', 'Indefinido'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, null=True, verbose_name='Genero')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('telefono_emergencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de Emergencia')),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Foto de Perfil')),
                ('ficha_medica', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Ficha Medica')),
                ('saldo', models.BooleanField(blank=True, default=True, null=True, verbose_name='Al dia / Debe')),
                ('observaciones_medicas', models.TextField(blank=True, null=True, verbose_name='Observaciones Medicas')),
                ('status', models.CharField(blank=True, choices=[('AC', 'Activo'), ('IN', 'Inactivo')], max_length=150, null=True)),
                ('cuenta', models.IntegerField(blank=True, null=True, verbose_name='Cuenta')),
                ('actividades', models.ManyToManyField(blank=True, to='SmartGym.Actividad')),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=50, null=True, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=50, null=True, verbose_name='Telefono')),
                ('encargado', models.CharField(max_length=50, null=True, verbose_name='Encargado')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_fijo', models.BooleanField(blank=True, default=True, null=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Actividad')),
                ('horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Horario')),
                ('socio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Socio')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.AddField(
            model_name='socio',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal'),
        ),
        migrations.CreateModel(
            name='RutinaXEjercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(blank=True, decimal_places=5, max_digits=1000, null=True, verbose_name='Peso')),
                ('repeticiones', models.IntegerField(blank=True, null=True, verbose_name='Repeticiones')),
                ('series', models.IntegerField(blank=True, null=True, verbose_name='Series')),
                ('ejercicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Ejercicio')),
                ('rutina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Rutina')),
            ],
        ),
        migrations.AddField(
            model_name='rutina',
            name='ejercicio',
            field=models.ManyToManyField(blank=True, through='SmartGym.RutinaXEjercicio', to='SmartGym.Ejercicio'),
        ),
        migrations.AddField(
            model_name='rutina',
            name='socio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Socio'),
        ),
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='Fecha del Recordatorio')),
                ('socio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Socio')),
                ('turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Turno')),
            ],
            options={
                'verbose_name': 'Recordatorio',
                'verbose_name_plural': 'Recordatorios',
            },
        ),
        migrations.CreateModel(
            name='ProfesionalXConsultorios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(blank=True, null=True, verbose_name='Dia')),
                ('hora_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Hora Inicio')),
                ('hora_fin', models.DateTimeField(blank=True, null=True, verbose_name='Hora Fin')),
                ('consultorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Consultorio')),
                ('profesional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Profesional')),
            ],
        ),
        migrations.AddField(
            model_name='profesional',
            name='consultorios',
            field=models.ManyToManyField(blank=True, through='SmartGym.ProfesionalXConsultorios', to='SmartGym.Consultorio'),
        ),
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_horas', models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Horas Liquidadas')),
                ('precio_hora', models.IntegerField(blank=True, null=True, verbose_name='Precio Hora Liquidada')),
                ('monto_total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Liquidado')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha de la liquidacion')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Empleado')),
            ],
            options={
                'verbose_name': 'Liquidacion',
                'verbose_name_plural': 'Liquidaciones de Empleados',
            },
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombre')),
                ('estado', models.CharField(blank=True, choices=[('DIS', 'Disponible'), ('NO', 'No Disponible'), ('REP', 'A Reparar')], max_length=150, null=True)),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('codigo_insumo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Codigo del Insumo')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Proveedor')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
            },
        ),
        migrations.CreateModel(
            name='HorarioConsultorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hora de Inicio')),
                ('hora_fin', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hora de Fin')),
                ('dia', models.CharField(blank=True, choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=150, null=True, verbose_name='Dia de Atención')),
                ('consultorios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Consultorio')),
                ('profesionales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Profesional')),
            ],
            options={
                'verbose_name': 'Horario del Consultorio',
                'verbose_name_plural': 'Horarios de los Consultorios',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal'),
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fecha del Vencimiento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('monto', models.IntegerField(blank=True, null=True, verbose_name='Monto')),
                ('metodo_pago', models.CharField(blank=True, choices=[('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Credito', 'Credito'), ('Otro', 'Otro')], max_length=50, null=True, verbose_name='Metodo de Pago')),
                ('codigo_transaccion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Codigo de la transaccion')),
                ('socio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Socio')),
            ],
            options={
                'verbose_name': 'Cuota',
                'verbose_name_plural': 'Control de Cuotas',
            },
        ),
        migrations.AddField(
            model_name='consultorio',
            name='horarios',
            field=models.ManyToManyField(blank=True, to='SmartGym.HorarioConsultorio'),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal'),
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], max_length=150)),
                ('motivo', models.CharField(blank=True, choices=[('Pago a Proveedores', 'Pago a Proveedores'), ('Cobro Cuota', 'Cobro Cuota'), ('Otro', 'Otro')], max_length=50, null=True)),
                ('cuota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Cuota')),
            ],
            options={
                'verbose_name': 'Caja',
                'verbose_name_plural': 'Registro de Cajas',
            },
        ),
        migrations.CreateModel(
            name='Autoridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=120, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('genero', models.CharField(blank=True, choices=[('Indefinido', 'Indefinido'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, null=True, verbose_name='Genero')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('telefono_emergencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de Emergencia')),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Foto de Perfil')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal')),
            ],
            options={
                'verbose_name': 'Autoridad',
                'verbose_name_plural': 'Autoridades',
            },
        ),
        migrations.CreateModel(
            name='AsistenciaSocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.CharField(blank=True, max_length=150, null=True, verbose_name='Fecha de Ingreso')),
                ('hora_ingreso', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hora de Ingreso')),
                ('socio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Socio')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal')),
            ],
            options={
                'verbose_name': 'Asistencia Socio',
                'verbose_name_plural': 'Asistencias Socios',
            },
        ),
        migrations.CreateModel(
            name='AsistenciaEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.CharField(blank=True, max_length=150, null=True, verbose_name='Fecha de Ingreso')),
                ('hora_ingreso', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hora de Ingreso')),
                ('tipo', models.BooleanField(blank=True, choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], null=True)),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Empleado')),
            ],
            options={
                'verbose_name': 'Asistencia Empleado',
                'verbose_name_plural': 'Asistencias Empleados',
            },
        ),
        migrations.AddField(
            model_name='actividad',
            name='empleados',
            field=models.ManyToManyField(blank=True, to='SmartGym.Empleado'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal'),
        ),
    ]
