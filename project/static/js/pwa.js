if (window.matchMedia('(display-mode: standalone)').matches) {

    window.addEventListener('popstate', function () {

        if (window.location.pathname !== '/') {

            window.location.replace('/');

        }

    });

}