$(document).ready(function() {
  // get json data
  const data = '{"name": "json-view","version": "1.0.0"}';
  // create json tree object
  const tree = JsonView.createTree(data);

  // render tree into dom element
  JsonView.render(tree, document.querySelector('div.sphinx-data-viewer'));

} );
