function main() {
  const n = parseInt(readLine(), 10);
  var result;
  for (var i = 1; i <= 10; i++) {
    result = n * i;
    console.log(n + " x " + i + " = " + result);
  }
}
