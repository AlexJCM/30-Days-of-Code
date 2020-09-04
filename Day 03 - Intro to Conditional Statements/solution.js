function main() {
  const N = parseInt(readLine(), 10);
  if (N % 2 == 0) {
    if (N >= 2 && N <= 5) {
      console.log("Not Weird");
    }
    if (N >= 6 && N <= 20) {
      console.log("Weird");
    }
    if (N > 20) {
      console.log("Not Weird");
    }
  } else {
    console.log("Weird");
  }
}
