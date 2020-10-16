var objects = [];
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};


// technically speaking, we can use js to call the backend
// we could also, since we have the cards, push the cards



var j = 0;
document.getElementById("card").innerHTML = objects[j].front;
function flipCard() {
  var x = document.getElementById("card");
  if (x.innerHTML === objects[j].front) {
    x.innerHTML = objects[j].back;
  } else {
    x.innerHTML = objects[j].front;
  }
}

