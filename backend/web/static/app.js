$(document).ready(function() {
  window.mdc.autoInit();

  /* Update the hidden input when the select has changed. */
  $("#board-select").on("MDCSelect:change", function() {
    let select = new mdc.select.MDCSelect(this);
    $('input[name=board]').val(select.value);
  });
});
