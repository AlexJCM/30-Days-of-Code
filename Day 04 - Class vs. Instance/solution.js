function Person(age) {
  var age;

  if (age < 0) {
    console.log("Age is not valid, setting age to 0.");
    this.age = 0;
  } else this.age = age;
}

Person.prototype.yearPasses = function() {
  this.age++;
};

Person.prototype.amIOld = function() {
  if (this.age < 13) console.log("You are young.");
  else if (this.age >= 13 && this.age < 18) console.log("You are a teenager.");
  else console.log("You are old.");
};
