const boton_abrir = document.getElementById('boton-hamburguesa-abrir');
const boton_cerrar = document.getElementById('boton-hamburguesa-cerrar');
const navbar = document.getElementById('navbar');

boton_abrir.addEventListener('click', ()=>{
    navbar.classList.toggle('mostrar');
    boton_abrir.classList.toggle('opacity-0');
    boton_cerrar.classList.toggle('display-none');
    setTimeout(() => {
        boton_cerrar.classList.toggle('opacity-0');
        boton_abrir.classList.toggle('display-none');
    }, 100);
})

boton_cerrar.addEventListener('click', ()=>{
    navbar.classList.toggle('mostrar');
    boton_cerrar.classList.toggle('opacity-0');
    boton_abrir.classList.toggle('display-none');
    setTimeout(() => {
        boton_abrir.classList.toggle('opacity-0');
        boton_cerrar.classList.toggle('display-none');
    }, 100);
})

document.addEventListener("click", (e) => {
    if (!navbar.contains(e.target) && !boton_abrir.contains(e.target) && !boton_cerrar.contains(e.target)) {
        navbar.classList.remove("mostrar");
        boton_cerrar.classList.add('opacity-0');
        boton_abrir.classList.remove('opacity-0');
        setTimeout(() => {
            boton_cerrar.classList.add('display-none');
            boton_abrir.classList.remove('display-none');
        }, 100);
    }
});

const exito = document.getElementById('exito');

if (exito != null) {
    setTimeout(() => {
        exito.classList.add('opacity-0');
    }, 3000);
}