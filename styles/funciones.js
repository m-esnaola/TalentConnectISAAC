//*MAITANE

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