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
                const preview = document.getElementById('preview-foto');

                if (data.foto_url) {
                    preview.src = data.foto_url;
                    preview.style.display = 'block';
                } else {
                    preview.style.display = 'none';
                }
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

document.querySelectorAll('.editar-gasto-diario').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();

        const id = this.dataset.id;

        fetch(`/gastos/gasto-diario/${id}/data/`)
            .then(res => res.json())
            .then(data => {

                document.getElementById('edit-id-diario').value = id;
                document.getElementById('edit-monto-diario').value = data.monto;
                document.getElementById('edit-fecha-diario').value = data.fecha;
                document.getElementById('edit-nota-diario').value = data.nota || '';
                const preview = document.getElementById('preview-foto-diario');

                if (data.foto_url) {
                    preview.src = data.foto_url;
                    preview.style.display = 'block';
                } else {
                    preview.style.display = 'none';
                }
                document.getElementById('edit-categoria-diario').value = data.categoria;

                document.getElementById('modal-editar-diario').style.display = 'flex';
            });
    });
});


// 👉 guardar (IMPORTANTE: FormData)
document.getElementById('form-editar-diario').addEventListener('submit', function(e) {
    e.preventDefault();

    const id = document.getElementById('edit-id-diario').value;
    const form = document.getElementById('form-editar-diario');

    const formData = new FormData(form);

    fetch(`/gastos/gasto-diario/${id}/editar/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(() => location.reload());
});

document.querySelectorAll('.editar-ingreso').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();

        const id = this.dataset.id;

        fetch(`/gastos/ingreso/${id}/data/`)
            .then(res => res.json())
            .then(data => {

                document.getElementById('edit-id-ingreso').value = id;
                document.getElementById('edit-monto-ingreso').value = data.monto;
                document.getElementById('edit-fecha-ingreso').value = data.fecha;
                document.getElementById('edit-nota-ingreso').value = data.nota || '';
                const preview = document.getElementById('preview-foto-ingreso');

                if (data.foto_url) {
                    preview.src = data.foto_url;
                    preview.style.display = 'block';
                } else {
                    preview.style.display = 'none';
                }
                document.getElementById('edit-categoria-ingreso').value = data.categoria;

                document.getElementById('modal-editar-ingreso').style.display = 'flex';
            });
    });
});


// 👉 guardar (IMPORTANTE: FormData)
document.getElementById('form-editar-ingreso').addEventListener('submit', function(e) {
    e.preventDefault();

    const id = document.getElementById('edit-id-ingreso').value;
    const form = document.getElementById('form-editar-ingreso');

    const formData = new FormData(form);

    fetch(`/gastos/ingreso/${id}/editar/`, {
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
    const modal = document.getElementById('modal-editar-diario');
    const boton = this.document.getElementById('boton_cerrar_modal-diario');
    if (e.target === modal || e.target === boton) {
        modal.style.display = 'none';
    }
});

window.addEventListener('click', function(e) {
    const modal = document.getElementById('modal-editar-ingreso');
    const boton = this.document.getElementById('boton_cerrar_modal-ingreso');
    if (e.target === modal || e.target === boton) {
        modal.style.display = 'none';
    }
});

function cerrar_ventana(elemento, boton) {
    window.addEventListener('click', function(e) {
        if (e.target === elemento || e.target === boton) {
            elemento.classList.add('display-none');
        }
    });
};

const boton_abrir_foto = document.getElementsByClassName('boton_abrir_foto');

for (let boton of boton_abrir_foto) {
    boton.addEventListener('click', () => {
        const tarjeta = boton.closest('.gasto-fijo-for');
        const foto_referencia_contenedor = document.querySelector('.foto_referencia_contenedor');
        const boton_cerrar_foto = document.querySelector('.boton_cerrar_foto');
        foto_referencia_contenedor.classList.remove('display-none');
        boton_cerrar_foto.addEventListener('click', () => {
            foto_referencia_contenedor.classList.add('display-none');
        })
        cerrar_ventana(foto_referencia_contenedor, boton_cerrar_foto);
    })
}

const boton_abrir_foto_gasto = document.getElementsByClassName('boton_abrir_foto_gasto');

for (let boton of boton_abrir_foto_gasto) {
    boton.addEventListener('click', () => {
        const tarjeta = boton.closest('.gasto-fijo-for');

        const foto_referencia_contenedor_gasto = document.querySelector('.foto_referencia_contenedor_gasto');
        const boton_cerrar_foto_gasto = document.querySelector('.boton_cerrar_foto_gasto');
        foto_referencia_contenedor_gasto.classList.remove('display-none');
        boton_cerrar_foto_gasto.addEventListener('click', () => {
            foto_referencia_contenedor_gasto.classList.add('display-none');
        })
        cerrar_ventana(foto_referencia_contenedor_gasto, boton_cerrar_foto_gasto);
    })
}

const boton_abrir_foto_ingreso = document.getElementsByClassName('boton_abrir_foto_ingreso');

for (let boton of boton_abrir_foto_ingreso) {
    boton.addEventListener('click', () => {
        const tarjeta = boton.closest('.gasto-fijo-for');

        const foto_referencia_contenedor_ingreso = document.querySelector('.foto_referencia_contenedor_ingreso');
        const boton_cerrar_foto_ingreso = document.querySelector('.boton_cerrar_foto_ingreso');
        foto_referencia_contenedor_ingreso.classList.remove('display-none');
        boton_cerrar_foto_ingreso.addEventListener('click', () => {
            foto_referencia_contenedor_ingreso.classList.add('display-none');
        })
        cerrar_ventana(foto_referencia_contenedor_ingreso, boton_cerrar_foto_ingreso)
    })
}

document.querySelectorAll('.form-eliminar-ingreso').forEach(form => {
    form.addEventListener('submit', function(e) {
        const confirmar = confirm('¿Seguro que querés eliminar este ingreso?');
        if (!confirmar) {
            e.preventDefault();
        }
    });
});

document.querySelectorAll('.form-eliminar-gasto').forEach(form => {
    form.addEventListener('submit', function(e) {
        const confirmar = confirm('¿Seguro que querés eliminar este gasto fijo?');
        if (!confirmar) {
            e.preventDefault();
        }
    });
});

document.querySelectorAll('.form-eliminar-gasto-fijo').forEach(form => {
    form.addEventListener('submit', function(e) {
        const confirmar = confirm('¿Seguro que querés eliminar este gasto diario?');
        if (!confirmar) {
            e.preventDefault();
        }
    });
});