const boton_regsitrar = document.getElementById('boton_registrar');
const boton_login = document.getElementById('boton_login');

boton_regsitrar.addEventListener('click',()=>{
    const login = document.getElementById('login');
    const registro = document.getElementById('registro');
    login.classList.add('right-40');
    login.classList.toggle('opacity-0');
    registro.classList.add('right-40');
    registro.classList.toggle('opacity-0');
});

boton_login.addEventListener('click',()=>{
    const login = document.getElementById('login');
    const registro = document.getElementById('registro');
    login.classList.remove('right-40');
    login.classList.toggle('opacity-0');
    registro.classList.remove('right-40');
    registro.classList.toggle('opacity-0');
});