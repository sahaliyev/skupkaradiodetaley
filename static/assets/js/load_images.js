$(document).ready(function () {
    let page = 1; // Page number to handle pagination, if needed
    let loading = false; // Flag to prevent multiple AJAX requests at once

    // Function to fetch and append images
    function loadImages() {
        if (loading) return; // Prevent multiple requests at the same time
        loading = true;

        $.ajax({
            url: '/api/images/', // The URL of your Django view
            data: { page: page }, // If you're paginating, send the page number
            method: 'GET',
            success: function (data) {
                // Loop through images returned by the Django view
                data.images.forEach(function (image) {
                    $('#images').append(
                        `
                        <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app">
                          <img src="${image.url}" class="img-fluid" alt="${image.name}">
                        </div>
                        `
                    );
                });

                // Check if there are more images to load
                if (data.pagination.current_page < data.pagination.total_pages) {
                    page++; // Increase page number for the next request
                } else {
                    $(window).off('scroll', onScroll); // No more images to load
                }

                loading = false; // Allow new requests
            },
            error: function () {
                console.log('Error loading images');
                loading = false;
            }
        });
    }

    // Function to detect when the user scrolls to the bottom
    function onScroll() {
        if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100) {
            loadImages();
        }
    }

    // Initial load
    loadImages();

    // Attach scroll event to trigger loading more images
    $(window).on('scroll', onScroll);
});
