function main() {
  const n = parseInt(readLine(), 10);

  const arr = readLine()
    .split(" ")
    .map(arrTemp => parseInt(arrTemp, 10));
  var aux = "";
  for (var i = n - 1; i >= 0; i--) {
    aux = aux + arr[i] + " ";
  }
  console.log(aux);
}
