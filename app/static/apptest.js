var objects = []
x.forEach(loopObjects);
function loopObjects(item, index) {
    objects.push(JSON.parse(item))
};

document.getElementById('cardFront').innerHTML = objects[0].front
document.getElementById('cardBack').innerHTML = objects[0].back

document.addEventListener('DOMContentLoaded', function(event) {
    document.getElementById('flip-card-btn-turn-to-back').style.visibility = 'visible';
    document.getElementById('flip-card-btn-turn-to-front').style.visibility = 'visible';
    document.getElementById('next-card-btn').style.visibility = 'visible';
    document.getElementById('flip-card-btn-turn-to-back').onclick = function() {
        document.getElementById('flip-card').classList.toggle('do-flip');
    };
    document.getElementById('flip-card-btn-turn-to-front').onclick = function() {
        document.getElementById('flip-card').classList.toggle('do-flip');
    };
});
