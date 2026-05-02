const filtros = document.getElementById('filtros');
const svg = document.getElementById('svg');

svg.addEventListener('click', () => {
    filtros.classList.toggle('display-none');
})

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

boton_abrir_foto.addEventListener('click', () => {
    const foto_referencia_contenedor = document.getElementById('foto_referencia_contenedor');
    const boton_cerrar_foto = document.getElementById('boton_cerrar_foto');
    foto_referencia_contenedor.classList.remove('display-none');
    boton_cerrar_foto.addEventListener('click', () => {
        foto_referencia_contenedor.classList.add('display-none');
    })
})