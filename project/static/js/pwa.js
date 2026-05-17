(() => {

    // =========================
    // DETECTAR PWA
    // =========================

    const isStandalone =
        window.matchMedia('(display-mode: standalone)').matches ||
        window.navigator.standalone === true;

    if (!isStandalone) return;

    // =========================
    // CONFIG
    // =========================

    const HOME = '/';

    // Rutas que NO deberían acumular historial
    // (pantallas funcionales)
    const REPLACE_ROUTES = [
        '/gastos/',
        '/usuarios/perfil/',
        '/gastos/ingresar-gastos/',
    ];

    // Rutas donde SÍ tiene sentido volver atrás
    // porque son navegación real
    const NORMAL_ROUTES = [
        '/',
    ];

    // =========================
    // HELPERS
    // =========================

    function shouldReplace(pathname) {
        return REPLACE_ROUTES.some(route =>
            pathname.startsWith(route)
        );
    }

    function shouldKeepHistory(pathname) {
        return NORMAL_ROUTES.some(route =>
            pathname === route
        );
    }

    // =========================
    // CONTROL DEL HISTORIAL
    // =========================

    const currentPath = location.pathname;

    // Si es una pantalla funcional:
    // reemplazamos historial para evitar
    // una cadena infinita de pantallas
    if (shouldReplace(currentPath)) {

        history.replaceState(
            {
                gastarin: true,
                path: currentPath
            },
            '',
            location.href
        );

    } else if (shouldKeepHistory(currentPath)) {

        // En páginas principales sí dejamos historial
        history.pushState(
            {
                gastarin: true,
                path: currentPath
            },
            '',
            location.href
        );
    }

    // =========================
    // BOTÓN ATRÁS
    // =========================

    window.addEventListener('popstate', () => {

        const path = location.pathname;

        // Si NO estamos en home:
        // volver al inicio
        if (path !== HOME) {

            location.replace(HOME);
            return;
        }

        // Si YA estamos en home:
        // intentamos salir de la app
        // (depende del navegador)
        window.close();

    });

})();