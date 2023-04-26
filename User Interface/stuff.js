$(document).ready(function() {
    $('.search').on('click', function() {
      var popup = $('<div class="popup">Not found, try a Zip Code or City Name</div>');
      $('body').append(popup);
    });
  });

  