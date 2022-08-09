function desplegar(seccion,boton){
  if (document.getElementById(seccion).style.display == "none"){
    document.getElementById(seccion).style.display = "block";
    document.getElementById(boton).className = "btn fa-solid float-end fa-chevron-up";
    
} else {
    document.getElementById(seccion).style.display = "none";
    document.getElementById(boton).className = "btn fa-solid float-end fa-chevron-down";
  }
}
