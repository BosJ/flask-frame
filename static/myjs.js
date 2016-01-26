$(function() {
  $("#submitBtn").click(function() {
       $.ajax({
          type: "GET",
          url: "/echo/",
          contentType: "application/json; charset=utf-8",
          data: { echoValue: $('input[name="echoText"]').val() },
          success: function(data) {
              $('#echoResult').text(data.value);
          }
      });
  });
});

function load() {
	$.ajax({
		url: '/time',
		success: function(data) {

			$('#p').text(data.value);
		}
	});
}

setInterval('load()', 500);
