// technically speaking, we can use js to call the backend
// we could also, since we have the cards, push the cards

// look into pagination, there may be a lot of load on the db depending
// on the traffic, one option is to learn how to serve x at a time

// look into design patterns, search solid principles, book called
// clean architecture, good high level overview of an application

// look into cacheing

var objects = []
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};
console.log(objects);

// flip card
const card = document.querySelector('.card__inner');
card.addEventListener('click', () => {
    card.classList.toggle('is-flipped');
});

// retrieve ele
const nextButton = document.querySelector('.nextButton');
nextButton.addEventListener('click', (e) => {
    // reset transition
    e.preventDefault;
    // remove class
    card.classList.remove('is-next');
    // black magic
    void card.offsetWidth;
    // re-add class
    card.classList.add('is-next');
    
}, false);

var j = 0;
var cardFront = document.querySelector('.cardFront').innerHTML = objects[j].front
var cardBack = document.querySelector('.cardBack').innerHTML = objects[j].back

var k = j % objects.length
function nextCard() {
    j += 1;
    var k = j % objects.length
    document.querySelector('.cardFront').innerHTML = objects[k].front;
    document.querySelector('.cardBack').innerHTML = objects[k].back;
    
};

var obj = objects[k].id
const url = "/_mark_known"
const data = obj

// asynchronous fetch for marking a card as known on sqlite, maps to
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

// hide pw
function myFunction() {
    let x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
