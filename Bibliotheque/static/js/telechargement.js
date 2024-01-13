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
        xhr.open('GET', url, true);
        xhr.responseType = 'blob';

        xhr.onload = function () {
            var blob = xhr.response;
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = nomFichier;  
            link.click();
        };

        xhr.onerror = function () {
            console.error('XHR encountered an error.');
        };

        console.log('Before XHR send.');
        xhr.send();
        console.log('After XHR send.');
    }
});
