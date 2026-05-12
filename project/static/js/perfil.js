const boton_editar_perfil = document.querySelector('.boton-editar-datos-perfil');
const boton_cerrar_perfil = document.querySelector('.boton-cerrar-editar-perfil');
const div_editar_perfil = document.querySelector('.editar-datos-perfil');

boton_editar_perfil.addEventListener('click', (e) => {
    e.preventDefault();
    div_editar_perfil.classList.remove('display-none');
});

boton_cerrar_perfil.addEventListener('click', (e) => {
    e.preventDefault();
    div_editar_perfil.classList.add('display-none');
});

window.addEventListener('click', (e) => {
    if (e.target === div_editar_perfil) {
        div_editar_perfil.classList.add('display-none');
    }
});