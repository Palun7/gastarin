const boton_regsitrar = document.getElementById('boton_registrar');
const boton_login = document.getElementById('boton_login');

boton_regsitrar.addEventListener('click',()=>{
    const login = document.getElementById('login');
    const registro = document.getElementById('registro');
    login.classList.toggle('z-index-1000');
    login.classList.toggle('opacity-0');
    registro.classList.toggle('z-index-1000');
    setTimeout(() => {
        registro.classList.toggle('display-none');
        login.classList.toggle('display-none');
    }, 500);
    setTimeout(() => {
        registro.classList.toggle('opacity-0');
    }, 600)
});

boton_login.addEventListener('click',()=>{
    const login = document.getElementById('login');
    const registro = document.getElementById('registro');
    login.classList.toggle('z-index-1000');
    registro.classList.toggle('z-index-1000');
    registro.classList.toggle('opacity-0');
    setTimeout(() => {
        login.classList.toggle('display-none');
        registro.classList.toggle('display-none');
    }, 500);
    setTimeout(() => {
        login.classList.toggle('opacity-0');
    }, 600);
});

const pass = document.getElementById('password');
const pass_confirm = document.getElementById('confirm_password');

pass_confirm.addEventListener('focusout', () => {
    const div_error = document.getElementById('error_password');
    if (pass.value != pass_confirm.value) {
        div_error.classList.remove('display-none');
    };
    if (pass.value == pass_confirm.value) {
        div_error.classList.add('display-none');
    };
});

const error = document.getElementsByClassName('error');

if (error.length != 0) {
    const login = document.getElementById('login');
    const registro = document.getElementById('registro');
    login.classList.toggle('z-index-1000');
    login.classList.toggle('opacity-0');
    registro.classList.toggle('z-index-1000');
    registro.classList.toggle('opacity-0');
    registro.classList.toggle('display-none');
    login.classList.toggle('display-none');
}