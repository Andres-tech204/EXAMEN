from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre_cliente = ''
    total_sin_descuento = 0
    descuento = 0
    total_a_pagar = 0

    if request.method == 'POST':
        nombre_cliente = request.form['nombre']
        edad = float(request.form['edad'])
        cantidad_tarros = float(request.form['cantidadtarros'])

        total_sin_descuento = cantidad_tarros * 9000

        if edad >= 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_a_pagar = total_sin_descuento - descuento

        flash('Cálculos realizados con éxito.')

    return render_template('ejercicio1.html',
                           nombre_cliente=nombre_cliente,
                           total_sin_descuento=total_sin_descuento,
                           descuento=descuento,
                           total_a_pagar=total_a_pagar)



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje_bienvenida = None
    mensaje_error = None

    if request.method == 'POST':
        try:
            nombre_usuario = request.form['nombre-usuario']
            contrasena_usuario = request.form['contraseña-usuario']

            # Definir usuarios y contraseñas
            usuarios = {"juan": "admin", "pepe": "user"}

            if nombre_usuario in usuarios and contrasena_usuario == usuarios[nombre_usuario]:
                if nombre_usuario == "juan":
                    mensaje_bienvenida = "Bienvenido administrador juan"
                elif nombre_usuario == "pepe":
                    mensaje_bienvenida = "Bienvenido usuario pepe"
            else:
                mensaje_error = "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo."
        except Exception as e:
            mensaje_error = f"Error: {str(e)}"

    return render_template('ejercicio2.html', mensaje_bienvenida=mensaje_bienvenida, mensaje_error=mensaje_error)




if __name__ == '__main__':
    app.run(debug=True)
