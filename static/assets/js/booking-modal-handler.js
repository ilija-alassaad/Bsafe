$(document).ready(function () {
  $("#staticBackdrop").on("show.bs.modal", function (e) {
    var modal = $("#staticBackdrop");
    var url = $(e.relatedTarget).data("url");

    $.ajax({
      url: url,
      success: function (data) {
        modal.find("#dialog").html(data);
      },
    });
  });
});