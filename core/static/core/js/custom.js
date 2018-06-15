$(function(){
  $("#pl,#uk").click(function() {
    var language = this.value;
    $("#language").val(language);
    $("#lang-form").submit();
  });
});
