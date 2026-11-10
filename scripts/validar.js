function validarForm(event) {
    event.preventDefault();

    var nombre = document.getElementById("nombre").value;
    var edad = document.getElementById("edad").value;
    var email = document.getElementById("email").value;
    var nacimiento = document.getElementById("nacimiento").value;
    var puesto = document.getElementById("puestoSelect").value;

    var presencial = document.getElementById("presencial").checked;
    var remoto = document.getElementById("remoto").checked;
    var hibrido = document.getElementById("hibrido").checked;
    var privacidad = document.getElementById("privacidad").checked;

    var mensajeError = "";

    if (nombre == "") {
        mensajeError = mensajeError + "Falta poner el nombre.<br>";
    }
    if (edad == "") {
        mensajeError = mensajeError + "Falta poner la edad.<br>";
    }
    if (email == "") {
        mensajeError = mensajeError + "Falta poner el email.<br>";
    }
    if (nacimiento == "") {
        mensajeError = mensajeError + "Falta la fecha de nacimiento.<br>";
    }
    if (puesto == "") {
        mensajeError = mensajeError + "Falta elegir un puesto.<br>";
    }
    if (presencial == false && remoto == false && hibrido == false) {
        mensajeError = mensajeError + "Falta elegir una modalidad.<br>";
    }
    if (privacidad == false) {
        mensajeError = mensajeError + "Debes aceptar la privacidad.<br>";
    }
    var cajaErrores = document.getElementById("errores");

    if (mensajeError != "") {
        // Si la variable tiene algún texto, mostramos los errores
        cajaErrores.innerHTML = mensajeError;
        cajaErrores.style.display = "block";
    } else {
        // Si la variable está vacía, es que todo está bien
        cajaErrores.style.display = "none";
        alert("CV guardado correctamente.");
    }

}

//*MAITANE --> talentconnect.html

// Obtener los elementos HTML mediante sus identificadores
var menu_ofertas = document.getElementById("menu_ofertas");
var boton_ofertas = document.getElementById("boton_ofertas");
var boton_ofertas_oportunidades = document.getElementById("boton_ofertas_oportunidades")
var enlace_interes_ofertas = document.getElementById("enlace_interes_ofertas")

// Mostrar un aviso e impedir que se abra la página de ofertas
function fn_avisar_ofertas(evento) {
    evento.preventDefault();
    alert("PROXIMAMENTE!\nLa sección de ofertas aún no está disponible.")
}

// Asignar el evento click a los enlaces
menu_ofertas.addEventListener("click",fn_avisar_ofertas)
boton_ofertas.addEventListener("click",fn_avisar_ofertas)
boton_ofertas_oportunidades.addEventListener("click",fn_avisar_ofertas)
enlace_interes_ofertas.addEventListener("click",fn_avisar_ofertas)