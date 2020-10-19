var objects = []
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};

const card = document.querySelector('.card__inner')

card.addEventListener('click', function() {
    card.classList.toggle('is-flipped')
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


