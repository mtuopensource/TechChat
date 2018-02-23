$(document).ready(function() {
  var drawerEl = document.querySelector('.mdc-drawer');
  var MDCPersistentDrawer = mdc.drawer.MDCPersistentDrawer;
  var drawer = new MDCPersistentDrawer(drawerEl);
  document.querySelector('.tc-menu-toggle').addEventListener('click', function() {
    drawer.open = !drawer.open;
  });
  var activatedClass = 'mdc-list-item--selected';
  document.querySelector('.mdc-drawer__drawer').addEventListener('click', function(event) {
    var el = event.target;
    while (el && !el.classList.contains('mdc-list-item')) {
      el = el.parentElement;
    }
    if (el) {
      var activatedItem = document.querySelector('.' + activatedClass);
      if (activatedItem) {
        activatedItem.classList.remove(activatedClass);
      }
      event.target.classList.add(activatedClass);
    }
  });
});
