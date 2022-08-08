function desplegar(seccion,chevron){
  if (document.getElementById(seccion,chevron).style.display == "none"){
    document.getElementById(seccion).style.display = "block";
    document.getElementById(chevron).className = "btn float-end fa-solid fa-arrows-up-to-line";
    
} else {
    document.getElementById(seccion).style.display = "none";
    document.getElementById(chevron).className = "btn float-end fa-solid fa-chevron-down";
  }
}
