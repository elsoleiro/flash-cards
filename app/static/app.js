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
function flipCard() {
  var x = document.getElementById("card");
  var k = j % objects.length
  if (x.innerHTML === objects[k].front) {
    x.innerHTML = objects[k].back;
  } else {
    x.innerHTML = objects[k].front;
  }
};

function nextCard() {
    j += 1;
    var k = j % objects.length;
    document.getElementById("card").innerHTML = objects[k].front;
};

var k = j % objects.length;
var obj = objects[k].id;

const url = "/_mark_known"
const data = obj

async function knownCard() {
    postData(url, data);
};

async function postData (url, data) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })

  if (response.status < 200 || response.status >= 400) {
    throw new Error(`Recived HTTP status ${response.status}`);
  }

  return response.json();
}

document.getElementById("card").innerHTML = objects[j].front;
