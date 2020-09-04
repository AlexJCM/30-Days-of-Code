/**
 *   Class Constructor
 *
 *   @param firstName - A string denoting the Person's first name.
 *   @param lastName - A string denoting the Person's last name.
 *   @param id - An integer denoting the Person's ID number.
 *   @param scores - An array of integers denoting the Person's test scores.
 **/
class Student extends Person {
  // Write your constructor here
  constructor(firstName, lastName, id, scores) {
    super(firstName, lastName, id);
    this.testScores = scores;
  }

  /**
   *   Method Name: calculate
   *   @return A character denoting the grade.
   **/
  calculate() {
    var score_avg =
      this.testScores.reduce(function(a, b) {
        return a + b;
      }) / this.testScores.length;

    if (score_avg >= 90 && score_avg <= 100) {
      return "O";
    } else if (score_avg >= 80 && score_avg < 90) {
      return "E";
    } else if (score_avg >= 70 && score_avg < 80) {
      return "A";
    } else if (score_avg >= 55 && score_avg < 70) {
      return "P";
    } else if (score_avg >= 40 && score_avg < 55) {
      return "D";
    } else if (score_avg < 40) {
      return "T";
    }
  }
}
