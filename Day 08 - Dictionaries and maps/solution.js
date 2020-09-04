function processData(input) {
  //Enter your code here
  const phoneBook = new Map();
  const inputData = input.split("\n");
  const guideSize = Number(inputData.shift()); //3
  // Agregamos cada key:valor en el diccionario
  const queryData = inputData.reduce((target, item, index) => {
    index < guideSize
      ? phoneBook.set(item.split(" ")[0], item.split(" ")[1])
      : target.push(item);

    return target;
  }, []);
  //busca en el diccionario(mapa)
  queryData.forEach((val, index) => {
    console.log(
      phoneBook.get(val) ? `${val}=${phoneBook.get(val)}` : "Not found"
    );
  });
}
