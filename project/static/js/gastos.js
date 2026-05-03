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

// 👉 abrir modal
document.querySelectorAll('.editar-gasto').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();

        const id = this.dataset.id;

        fetch(`/gastos/gasto-fijo/${id}/data/`)
            .then(res => res.json())
            .then(data => {

                document.getElementById('edit-id').value = id;
                document.getElementById('edit-monto').value = data.monto;
                document.getElementById('edit-cuotas').value = data.cuotas || '';
                document.getElementById('edit-fecha').value = data.fecha;
                document.getElementById('edit-nota').value = data.nota || '';
                document.getElementById('edit-categoria').value = data.categoria;

                document.getElementById('modal-editar').style.display = 'flex';
            });
    });
});


// 👉 guardar (IMPORTANTE: FormData)
document.getElementById('form-editar').addEventListener('submit', function(e) {
    e.preventDefault();

    const id = document.getElementById('edit-id').value;
    const form = document.getElementById('form-editar');

    const formData = new FormData(form);

    fetch(`/gastos/gasto-fijo/${id}/editar/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(() => location.reload());
});


// 👉 cerrar modal al hacer click afuera
window.addEventListener('click', function(e) {
    const modal = document.getElementById('modal-editar');
    const boton = this.document.getElementById('boton_cerrar_modal');
    if (e.target === modal || e.target === boton) {
        modal.style.display = 'none';
    }
});

window.addEventListener('click', function(e) {
    const foto = document.getElementById('foto_referencia_contenedor');
    const boton = this.document.getElementById('boton_cerrar_modal');
    if (e.target === foto || e.target === boton) {
        foto.classList.add('display-none');
    }
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