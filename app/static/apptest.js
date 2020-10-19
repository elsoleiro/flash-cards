var objects = []
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};
console.log(objects);

const card = document.querySelector('.card__inner');

card.addEventListener('click', function() {
    card.classList.toggle('is-flipped');
});

const nextButton = document.querySelector('.nextButton');

nextButton.addEventListener('click', function() {
    card.classList.toggle('is-next');
});

var j = 0;
var cardFront = document.querySelector('.cardFront').innerHTML = objects[j].front
var cardBack = document.querySelector('.cardBack').innerHTML = objects[j].back

function nextCard() {
    j += 1;
    var k = j % objects.length;
    document.querySelector('.cardFront').innerHTML = objects[k].front;
    document.querySelector('.cardBack').innerHTML = objects[k].back;
    
};
var k = j % objects.length
var obj = objects[k].id
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


