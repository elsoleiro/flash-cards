console.log(cardFront, cardBack)
console.log(singleCard)
document.getElementById("card").innerHTML = cardFront;


function flipCard() {
  var x = document.getElementById("card");
  if (x.innerHTML === cardFront) {
    x.innerHTML = cardBack;
  } else {
    x.innerHTML = cardFront;
  }
} 

