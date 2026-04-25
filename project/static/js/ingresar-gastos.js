function abrirModal() {
    document.getElementById('modalCategoria').style.display = 'flex';
}

function cerrarModal() {
    document.getElementById('modalCategoria').style.display = 'none';
    document.getElementById('nombre_categoria').value = '';
    document.getElementById('icono_categoria').value = '';
}

window.onclick = function(event) {
    const modal = document.getElementById('modalCategoria');
    if (event.target === modal) {
        modal.style.display = "none";
        document.getElementById('nombre_categoria').value = '';
        document.getElementById('icono_categoria').value = '';
    }
}

document.getElementById('boton_nueva_categoria').addEventListener('click', ()=> {
    setTimeout(()=>{
        document.getElementById('nombre_categoria').value = '';
        document.getElementById('icono_categoria').value = '';
    }, 100);
})

document.querySelectorAll('.categoria').forEach(btn => {
    btn.addEventListener('click', () => {

        // Remover selección previa
        document.querySelectorAll('.categoria')
        .forEach(b => b.classList.remove('active'));

        // Activar seleccionada
        btn.classList.add('active');

        // Obtener id de la categoría
        const categoriaId = btn.dataset.id;
        console.log('Categoría seleccionada:', categoriaId);

        // Podés guardarlo en un input hidden
        // document.getElementById('categoria_id').value = categoriaId;
    });
});