const boton_editar_perfil = document.querySelector('.boton-editar-datos-perfil');
const boton_cerrar_perfil = document.querySelector('.boton-cerrar-editar-perfil');
const div_editar_perfil = document.querySelector('.editar-datos-perfil');
const abrir_categorias = document.querySelector('.abrir-categorias');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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

function cerrar_ventana(elemento, boton) {
    window.addEventListener('click', function(e) {
        if (e.target === elemento || e.target === boton) {
            elemento.classList.add('display-none');
        }
    });
};

abrir_categorias.addEventListener('click', ()=> {
    const cerrar_categorias = document.querySelector('.cerrar-categorias');
    const modal_categorias = document.querySelector('.modal-categorias');
    modal_categorias.classList.remove('display-none');
    cerrar_ventana(modal_categorias, cerrar_categorias);
})

document.querySelectorAll('.categoria-perfil').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();

        const id = this.dataset.id;

        fetch(`/usuarios/categoria/${id}/data/`)
            .then(res => res.json())
            .then(data => {

                document.getElementById('edit-id').value = id;
                document.getElementById('h4').innerHTML = data.h4;
                document.getElementById('edit-nombre').value = data.nombre;
                document.getElementById('edit-icono').value = data.icono;

                document.querySelector('.editar-categoria').classList.remove('display-none');
            });
    });

    const cerrar_editar = document.querySelector('.cerrar-editar');
    const ventana_editar = document.querySelector('.editar-categoria');
    cerrar_ventana(ventana_editar, cerrar_editar);
});

document.getElementById('form-categoria').addEventListener('submit', function(e) {
    e.preventDefault();

    const id = document.getElementById('edit-id').value;
    const form = document.getElementById('form-categoria');

    const formData = new FormData(form);

    fetch(`/usuarios/categoria/${id}/editar/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(() => location.reload());
});