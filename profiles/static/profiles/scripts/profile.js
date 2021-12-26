// Get selected value
let countrySelected = $("#id_default_country").val();
// If not selected, set text color
if (!countrySelected) {
  $("#id_default_country").css("color", "#aab7c4");
}
// If selected, set text color
$("#id_default_country").change(function () {
  countrySelected = $(this).val();
  if (!countrySelected) {
    $(this).css("color", "#aab7c4");
  } else {
    // other options that are not selected in menu
    $(this).css("color", "#000");
  }
});
