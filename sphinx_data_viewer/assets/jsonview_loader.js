$(document).ready(function() {
  // get json data
  const data2 = '{"name": "json-view","version": "1.0.0"}';


  $("div.sdv-data").each(function(index){
    console.log(index)
    // JsonView.render(tree, document.querySelector('div.sphinx-data-viewer'));
    let data = $(this).attr('data-sdv')

    try {
      let tree = JsonView.createTree(data);
      JsonView.render(tree, $(this)[0]);
    } catch(e) {
      $(this).html('<p>Error: Could not parse json data</p>')
    }
  })




} );
