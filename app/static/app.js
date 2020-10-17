var objects = [];
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};


console.log(x)


console.log(objects)
// technically speaking, we can use js to call the backend
// we could also, since we have the cards, push the cards

// look into pagination, there may be a lot of load on the db depending
// on the traffic, one option is to learn how to serve x at a time
//
// look into design patterns, search solid principles, book called
// clean architecture, good high level overview of an application

// look into cacheing
//
// use ajax request to whatever URL
// if you pass data you use post
// ajax is async java pretty much, js has a method
// called fetch

var j = 0;
document.getElementById("card").innerHTML = objects[j].front;
function flipCard() {
  var x = document.getElementById("card");
  if (x.innerHTML === objects[j].front) {
    x.innerHTML = objects[j].back;
  } else {
    x.innerHTML = objects[j].front;
  }
};


