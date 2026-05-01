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
