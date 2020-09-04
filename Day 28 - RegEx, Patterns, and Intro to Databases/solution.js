function main() {
  const N = parseInt(readLine(), 10);
  var patt = new RegExp("@gmail.com");
  var names = [];
  for (let NItr = 0; NItr < N; NItr++) {
    const firstNameEmailID = readLine().split(" ");
    const firstName = firstNameEmailID[0];
    const emailID = firstNameEmailID[1];
    //Using our regExp here with the emailID variable. Matching names are kept for the classification below.
    if (patt.test(emailID)) {
      names.push(firstName);
    }
  }
  // Then classify the names in alphabetical order and then we print them.
  names.sort().forEach(function(name) {
    console.log(name);
  });
}
