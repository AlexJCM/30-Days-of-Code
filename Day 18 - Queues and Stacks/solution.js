function Solution() {
  this.stack = [];
  this.queue = [];

  //Adds character onto top of stack.
  this.pushCharacter = function(ch) {
    this.stack.push(ch);
  };

  //Returns character on top of stack.
  this.popCharacter = function() {
    return this.stack.pop();
  };

  //Adds character to end of queue.
  this.enqueueCharacter = function(ch) {
    this.queue.push(ch);
  };

  //Returns the first character of the queue.
  this.dequeueCharacter = function() {
    return this.queue.shift();
  };

  //Alternative solution with proptotype
  /* 
     Solution.prototype.pushCharacter = this.stack.push;
     Solution.prototype.popCharacter = this.stack.pop;
     Solution.prototype.enqueueCharacter = this.queue.push;
     Solution.prototype.dequeueCharacter = this.queue.shift;
     */
}
