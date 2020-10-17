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

function old() {
    xhr = new XMLHttpRequest(); 
    xhr.open('POST', '_mark_known'); 
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() { 
        if (xhr.status === 200) {
            alert('Something went wrong' + xhr.responseText);
        }
        else if (xhr.status !== 200) {
            alert('Request failed.  Returned status of ' + xhr.status);
        }   
    };
    var k = j % objects.length
    xhr.send(encodeURI(objects[k].id));
};



function knownCard() {
    var req = new XMLHttpRequest();
    var k = j % objects.length
    var obj = objects[k].id;
    req.open('POST', '/_mark_known', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    req.send(obj);
};












document.getElementById("card").innerHTML = objects[j].front;
