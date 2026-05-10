const boton_recomendaciones = document.querySelector('.boton-recomendacion');

boton_recomendaciones.addEventListener('click', () => {
    const hacer_recomendacion = document.querySelector('.hacer-recomendacion');
    const boton_cerrar = document.querySelector('.cerrar-recomendacion');
    hacer_recomendacion.classList.remove('display-none');
    boton_cerrar.addEventListener('click', () => {
        hacer_recomendacion.classList.add('display-none');
    });
    cerrar(hacer_recomendacion, boton_cerrar);
});

function cerrar(contenedor, boton){
    window.addEventListener('click', function(e) {
        if (e.target === contenedor || e.target === boton) {
            contenedor.classList.add('display-none');
        }
    });
};