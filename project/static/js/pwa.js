if (window.matchMedia('(display-mode: standalone)').matches) {

    history.pushState(null, null, location.href);

    window.addEventListener('popstate', function () {

        if (window.location.pathname !== '/') {

            window.location.href = '/';

        } else {

            history.back();

        }

    });

}