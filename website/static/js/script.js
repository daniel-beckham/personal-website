$(function() {
  $(".img-preview").on("click", function(event) {
    event.preventDefault();
    $(".img-full").attr({
      src: $(this).find("img").attr("src"),
      alt: $(this).find("img").attr("alt"),
    });
    $("#img-modal").modal("show");
  });
});
