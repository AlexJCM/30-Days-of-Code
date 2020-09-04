function main() {
  var n = parseInt(readLine());
  a = readLine().split(" ");
  a = a.map(Number);

  // Write Your Code Here
  var numberOfSwaps = 0;
  for (var i = 0; i < n; i++) {
    for (var j = 0; j < n - 1; j++) {
      // Swap adjacent elements if they are in decreasing order
      if (a[j] > a[j + 1]) {
        var temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
        numberOfSwaps++;
      }
    }
  }

  console.log("Array is sorted in " + numberOfSwaps + " swaps.");
  console.log("First Element: " + a[0]);
  console.log("Last Element: " + a[a.length - 1]);
}
