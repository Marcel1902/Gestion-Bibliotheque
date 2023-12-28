document.addEventListener("DOMContentLoaded", function () {
    var boutonsTelechargement = document.querySelectorAll('.download');

    boutonsTelechargement.forEach(function (bouton) {
        bouton.addEventListener('click', function () {
            var url = bouton.getAttribute('data-url');
            var nomFichier = bouton.getAttribute('data-nom');
            telechargerLivre(url, nomFichier);
        });
    });

    function telechargerLivre(url, nomFichier) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, nomFichier, true);
        xhr.responseType = 'blob';

        xhr.onload = function () {
            var blob = xhr.response;
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = nomFichier;  // Utiliser la variable nomFichier ici
            link.click();
        };

        xhr.send();
    }
});
