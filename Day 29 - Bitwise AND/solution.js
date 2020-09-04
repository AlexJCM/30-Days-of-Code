function main() {
  const t = parseInt(readLine(), 10);
  for (let tItr = 0; tItr < t; tItr++) {
    const nk = readLine().split(" ");
    const n = parseInt(nk[0], 10);
    const k = parseInt(nk[1], 10);
    // Add your code here
    var a = k - 1;
    var b = ~a & -~a;
    if ((a | b) > n) console.log(a - 1);
    else console.log(a);
  }
}
