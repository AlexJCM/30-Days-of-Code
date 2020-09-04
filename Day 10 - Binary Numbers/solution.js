function main() {
  const n = parseInt(readLine());
  var binary = n.toString(2);
  var count = 0;
  var max = 0;
  for (var i = 0; i < binary.length; i++) {
    if (binary[i] == 1) {
      count++;
      if (count > max) {
        max = count;
      }
    } else {
      count = 0;
    }
  }

  console.log(max);
}
