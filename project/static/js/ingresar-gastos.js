const btn_diario = document.querySelector('.btn_diario')
const btn_fijo = document.querySelector('.btn_fijo')
const btn_ingreso = document.querySelector('.btn_ingreso')
const selector = document.querySelector('.selector')
const div_diarios = document.querySelector('.gastos-diarios')
const div_fijos = document.querySelector('.gastos-fijos')
const div_ingresos = document.querySelector('.ingresos')

btn_diario.addEventListener('click', () => {
    selector.classList.remove('selector_centro');
    selector.classList.remove('selector_derecha');
    selector.classList.add('selector_izquierda');
    setTimeout(() => {
    btn_fijo.classList.remove('btn_activo');
    btn_ingreso.classList.remove('btn_activo');
    btn_diario.classList.add('btn_activo');
    check();
    },100);
})

btn_fijo.addEventListener('click', () => {
    selector.classList.remove('selector_izquierda');
    selector.classList.remove('selector_derecha');
    selector.classList.add('selector_centro');
    setTimeout(() => {
        btn_diario.classList.remove('btn_activo');
        btn_ingreso.classList.remove('btn_activo');
        btn_fijo.classList.add('btn_activo');
        check();
    },100);
})

btn_ingreso.addEventListener('click', () => {
    selector.classList.remove('selector_izquierda');
    selector.classList.remove('selector_centro');
    selector.classList.add('selector_derecha');
    setTimeout(() => {
        btn_fijo.classList.remove('btn_activo');
        btn_diario.classList.remove('btn_activo');
        btn_ingreso.classList.add('btn_activo');
        check();
    }, 100);
})

function check(){
    if(btn_diario.classList.contains('btn_activo')){
        div_diarios.classList.remove('display-none');
        div_fijos.classList.remove('z-intex-1000');
        div_fijos.classList.add('opacity-0');
        div_ingresos.classList.remove('z-intex-1000');
        div_ingresos.classList.add('opacity-0');
        setTimeout(() => {
            div_diarios.classList.add('z-intex-1000');
            div_diarios.classList.remove('opacity-0');
            div_fijos.classList.add('display-none');
            div_ingresos.classList.add('display-none');
        }, 200);
    }
    if(btn_fijo.classList.contains('btn_activo')){
        div_diarios.classList.remove('z-intex-1000');
        div_diarios.classList.add('opacity-0');
        div_ingresos.classList.remove('z-intex-1000');
        div_ingresos.classList.add('opacity-0');
        div_fijos.classList.remove('display-none');
        setTimeout(() => {
            div_fijos.classList.add('z-intex-1000');
            div_fijos.classList.remove('opacity-0');
            div_diarios.classList.add('display-none');
            div_ingresos.classList.add('display-none');
        }, 200);
    }
    if(btn_ingreso.classList.contains('btn_activo')){
        div_diarios.classList.remove('z-intex-1000');
        div_diarios.classList.add('opacity-0');
        div_fijos.classList.remove('z-intex-1000');
        div_fijos.classList.add('opacity-0');
        div_ingresos.classList.remove('display-none');
        setTimeout(() => {
            div_diarios.classList.add('display-none');
            div_ingresos.classList.add('z-intex-1000');
            div_ingresos.classList.remove('opacity-0');
            div_fijos.classList.add('display-none');
        },200);
    }
}


function abrirModal() {
    document.getElementById('modalCategoria').style.display = 'flex';
}

function abrirModalIngreso() {
    document.getElementById('modalCategoria_ingreso').style.display = 'flex';
}

function cerrarModal() {
    document.getElementById('modalCategoria').style.display = 'none';
    document.getElementById('modalCategoria_ingreso').style.display = 'none';
    document.getElementById('nombre_categoria').value = '';
    document.getElementById('nombre_categoria_ingreso').value = '';
    document.getElementById('icono_categoria').value = '';
}

window.onclick = function(event) {
    const modal = document.getElementById('modalCategoria');
    const modal_ingreso = document.getElementById('modalCategoria_ingreso');
    if (event.target === modal || event.target === modal_ingreso) {
        modal.style.display = "none";
        modal_ingreso.style.display = "none";
        document.getElementById('nombre_categoria').value = '';
        document.getElementById('nombre_categoria_ingreso').value = '';
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
        document.getElementById('categoria_id').value = categoriaId;

        // Podés guardarlo en un input hidden
        // document.getElementById('categoria_id').value = categoriaId;
    });
});

document.querySelectorAll('.categoria_fijo').forEach(btn => {
    btn.addEventListener('click', () => {

        // Remover selección previa
        document.querySelectorAll('.categoria_fijo')
        .forEach(b => b.classList.remove('active'));

        // Activar seleccionada
        btn.classList.add('active');

        // Obtener id de la categoría
        const categoriaId = btn.dataset.id;
        document.getElementById('categoria_fijo_id').value = categoriaId;

        // Podés guardarlo en un input hidden
        // document.getElementById('categoria_id').value = categoriaId;
    });
});

document.querySelectorAll('.categoria_ingreso').forEach(btn => {
    btn.addEventListener('click', () => {

        // Remover selección previa
        document.querySelectorAll('.categoria_ingreso')
        .forEach(b => b.classList.remove('active'));

        // Activar seleccionada
        btn.classList.add('active');

        // Obtener id de la categoría
        const categoriaId = btn.dataset.id;
        document.getElementById('categoria_ingreso_id').value = categoriaId;

        // Podés guardarlo en un input hidden
        // document.getElementById('categoria_id').value = categoriaId;
    });
});

