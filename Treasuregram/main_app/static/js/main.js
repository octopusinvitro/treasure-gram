$('button').on('click', function(event) {
  event.preventDefault();
  var element = $(this);

  $.ajax({
    url:     '/like_treasure/',
    type:    'GET',
    data:    { treasure_id: element.attr('data-id') },
    success: function(response) {
      element.html(heart() + ' ' + response);
    }
  });

  function heart() {
    return '<svg aria-hidden="true" class="treasure-icon"><use xlink:href="/static/images/site-icons.svg#icon-heart"></use></svg>'
  }
});
