// Dans votre fichier JavaScript (telechargement.js)
document.addEventListener("DOMContentLoaded", function () {
    var boutonsTelechargement = document.querySelectorAll('.download');

    boutonsTelechargement.forEach(function (bouton) {
        bouton.addEventListener('click', function () {
            var urlLivre = bouton.getAttribute('data-url');
            telechargerLivre(urlLivre);
        });
    });

    function telechargerLivre(url) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = 'blob';

        xhr.onload = function () {
            var blob = xhr.response;
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = 'NomDuLivre.pdf';  // Nom du fichier de téléchargement
            link.click();
        };

        xhr.send();
    }
});
