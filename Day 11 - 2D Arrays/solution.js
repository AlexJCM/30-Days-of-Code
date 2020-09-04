function main() {
  let arr = Array(6);
  for (let i = 0; i < 6; i++) {
    arr[i] = readLine()
      .split(" ")
      .map(arrTemp => parseInt(arrTemp, 10));
  }

  //-63 is the minimum value that the hourglass can have
  let totalSum = -63;

  //We subtract -2 to the length of each row and column
  //because in the last 2 rows and columns there is no way
  //to get an hourglass
  for (let i = 0; i < arr.length - 2; i++) {
    for (let j = 0, curSum = 0; j < arr[i].length - 2; j++) {
      curSum =
        arr[i][j] +
        arr[i][j + 1] +
        arr[i][j + 2] +
        arr[i + 1][j + 1] +
        arr[i + 2][j] +
        arr[i + 2][j + 1] +
        arr[i + 2][j + 2];
      if (curSum > totalSum) {
        totalSum = curSum;
      }
    }
  }
  console.log(totalSum);
}
