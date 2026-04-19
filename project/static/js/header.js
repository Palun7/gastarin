const boton_abrir = document.getElementById('boton-hamburguesa-abrir');
const boton_cerrar = document.getElementById('boton-hamburguesa-cerrar');
const navbar = document.getElementById('navbar');

boton_abrir.addEventListener('click', ()=>{
    navbar.classList.toggle('mostrar');
    boton_cerrar.classList.toggle('mostrar');
    boton_abrir.classList.toggle('no-mostrar');
})

boton_cerrar.addEventListener('click', ()=>{
    navbar.classList.toggle('mostrar');
    boton_cerrar.classList.toggle('mostrar');
    boton_abrir.classList.toggle('no-mostrar');
})

document.addEventListener("click", (e) => {
    if (!navbar.contains(e.target) && !boton_abrir.contains(e.target) && !boton_cerrar.contains(e.target)) {
        navbar.classList.remove("mostrar");
        boton_cerrar.classList.remove('mostrar');
        boton_abrir.classList.remove('no-mostrar');
    }
});