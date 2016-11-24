$('button').on('click', function(event) {
  event.preventDefault();
  var element = $(this);

  $.ajax({
    url:     '/like_treasure/',
    type:    'POST',
    data:    { treasure_id: element.attr('data-id') },
    success: function(response) {
      element.html(heart() + ' ' + response);
    }
  });

  function heart() {
    return '<svg aria-hidden="true" class="treasure-icon"><use xlink:href="/static/images/site-icons.svg#icon-heart"></use></svg>'
  }
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    }
  }
})