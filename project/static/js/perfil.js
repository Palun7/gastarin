const boton_editar_perfil = document.querySelector('.boton-editar-datos-perfil');

boton_editar_perfil.addEventListener('click', () => {
    const boton_cerrar_perfil = document.querySelector('.boton-cerrar-editar-perfil');
    const div_editar_perfil = document.querySelector('.editar-datos-perfil');

    div_editar_perfil.classList.remove('display-none');

    boton_cerrar_perfil.addEventListener('click', () =>{
        div_editar_perfil.classList.add('display-none');
    })

    cerrar(div_editar_perfil, boton_cerrar_perfil);
});

function cerrar(contenedor, boton){
    window.addEventListener('click', function(e) {
        if (e.target === contenedor || e.target === boton) {
            contenedor.classList.add('display-none');
        }
    });
};