$(document).ready(function () {
    function loadImages() {
        $.ajax({
            url: '/api/images/', // The URL of your Django view
            method: 'GET',
            success: function (data) {
                data.images.forEach(function (image) {
                    $('#images').append(
                        `
                        <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app">
                          <img src="${image.url}" class="img-fluid" alt="${image.name}">
                        </div>
                        `
                    );
                });
            },
            error: function () {
                console.log('Error loading images');
            }
        });
    }
    loadImages();
});
