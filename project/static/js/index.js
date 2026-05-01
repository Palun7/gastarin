const filtros = document.getElementById('filtros');
const svg = document.getElementById('svg');

svg.addEventListener('click', () => {
    filtros.classList.toggle('display-none');
})