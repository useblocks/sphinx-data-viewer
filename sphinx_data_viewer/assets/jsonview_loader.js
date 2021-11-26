$(document).ready(function() {
  // get json data
  const data2 = '{"name": "json-view","version": "1.0.0"}';


  $("div.sdv-data").each(function(index){
    let data = $(this).attr('data-sdv')
    let expand = $(this).attr('data-expand')

    try {
      let tree = JsonView.createTree(data);
      JsonView.render(tree, $(this)[0]);
      if(expand==="True") {
        JsonView.expandChildren(tree);
      }
    } catch(e) {
      $(this).html('<p>Error: Could not parse json data</p>')
    }
  })




} );
