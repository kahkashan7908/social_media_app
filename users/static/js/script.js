$(document).on('click', '.btn-like', function(){
    var post_id = $(this).attr('id'); // Use jQuery to get the post ID
    var csrfToken = $('#csrf-token').data('token'); // Retrieve CSRF token from the data attribute

    $.ajax({
        method: "POST",
        url: '/posts/like',
        data: { post_id: post_id, csrfmiddlewaretoken: csrfToken }
    });

    // Optional: Redirect after the AJAX call
    window.location.href = "http://127.0.0.1:8000/posts/feed";
});
