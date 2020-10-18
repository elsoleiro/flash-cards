var objects = []
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};

const card = document.querySelector('.card-inner')

card.addEventListener('click', function() {
    card.classList.toggle('is-flipped')
});
