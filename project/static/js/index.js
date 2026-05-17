const filtros = document.getElementById('filtros');
const svg = document.getElementById('svg');

svg.addEventListener('click', () => {
    filtros.classList.toggle('display-none');
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            };
        };
    };
    return cookieValue;
};

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.checkbox-cuota').forEach(cb => {
        cb.addEventListener('change', function() {
            fetch(`/cuota/${this.dataset.id}/toggle/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
            });
        });
    });
});

const boton_abrir_foto = document.getElementById('boton_abrir_foto');

if (boton_abrir_foto) {

    boton_abrir_foto.addEventListener('click', () => {
        const foto_referencia_contenedor = document.getElementById('foto_referencia_contenedor');
        const boton_cerrar_foto = document.getElementById('boton_cerrar_foto');
        foto_referencia_contenedor.classList.remove('display-none');
        boton_cerrar_foto.addEventListener('click', () => {
            foto_referencia_contenedor.classList.add('display-none');
        })
        cerrar(foto_referencia_contenedor, boton_cerrar_foto);
    });
}

const boton_novedades = document.querySelector('.boton-novedades');

boton_novedades.addEventListener('click', () => {
    const div_novedades = document.querySelector('.novedades');
    div_novedades.classList.remove('display-none');
    const boton_cerrar_novedades = document.querySelector('.boton-cerrar-novedades');
    const contenedor = document.getElementById('contenedor-novedades');
    boton_cerrar_novedades.addEventListener('click', () => {
        div_novedades.classList.add('display-none');
    })
    window.addEventListener('click', function(e) {
        if (e.target === contenedor || e.target === boton_cerrar_novedades || e.target === div_novedades) {
            div_novedades.classList.add('display-none');
        }
    });
});


function cerrar(contenedor, boton){
    window.addEventListener('click', function(e) {
        if (e.target === contenedor || e.target === boton) {
            contenedor.classList.add('display-none');
        }
    });
};

document.querySelectorAll('.checkbox-cuota').forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        sessionStorage.setItem('cuotaAResaltar', checkbox.dataset.cuotaId);
        checkbox.form.submit();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const cuotaId = sessionStorage.getItem('cuotaAResaltar');

    if (cuotaId) {
        const cuota = document.querySelector(`[data-cuota-id="${cuotaId}"]`);

        if (cuota) {
            cuota.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
        }

        sessionStorage.removeItem('cuotaAResaltar');
    }
});

const botonPersonalizado = document.getElementById('boton-personalizado');
const modalPersonalizado = document.getElementById('modal-personalizado');
const cerrarPersonalizado = document.getElementById('cerrar-personalizado');

if (botonPersonalizado && modalPersonalizado) {
    botonPersonalizado.addEventListener('click', (e) => {
        e.preventDefault();
        modalPersonalizado.classList.remove('display-none');
        console.log('boton apretado');
    });
}

if (cerrarPersonalizado && modalPersonalizado) {
    cerrarPersonalizado.addEventListener('click', () => {
        modalPersonalizado.classList.add('display-none');
    });
}

window.addEventListener('click', (e) => {
    if (e.target === modalPersonalizado) {
        modalPersonalizado.classList.add('display-none');
    }
});