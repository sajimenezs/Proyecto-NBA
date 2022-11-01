
$(document).ready(function() {
    $(".buscador-equipos").select2();
});       


function change_image(){
    var cod = document.getElementById("equipoA").value;
    
    var new_image = " /static/images/logos/imagen_equipo_" + cod + ".png"
    
    document.getElementById("imagen-equipo-A").src=new_image;
    
}

function change_imageB(){
    var codB = document.getElementById("equipoB").value;

    var new_imageB = " /static/images/logos/imagen_equipo_" + codB + ".png"

    document.getElementById("imagen-equipo-B").src=new_imageB;

}
  


