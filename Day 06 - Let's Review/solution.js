function processData(input) {
  //Enter your code here
  var mensaje = input.split("\n");
  for (var i = 1; i < mensaje.length; i++) {
    var aux1 = "";
    var aux2 = "";
    for (var j = 0; j < mensaje[i].length; j++) {
      if (j % 2 == 0) {
        aux1 = aux1 + mensaje[i][j];
      } else {
        aux2 = aux2 + mensaje[i][j];
      }
    }
    console.log(aux1 + " " + aux2);
  }
}
