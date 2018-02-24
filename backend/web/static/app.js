$(document).ready(function() {
  window.mdc.autoInit();

  /* Update the hidden input when the form submits. */
  $('#create-thread-form').submit(function() {
    let select = new mdc.select.MDCSelect($('#board-select')[0]);
    $('input[name=board]').val(select.value);
  });
});
