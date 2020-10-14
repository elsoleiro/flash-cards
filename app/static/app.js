console.log(x)
console.log(x["front"])
document.getElementById("card").innerHTML = cardFront;


function flipCard() {
  var x = document.getElementById("card");
  if (x.innerHTML === cardFront) {
    x.innerHTML = cardBack;
  } else {
    x.innerHTML = cardFront;
  }
} 

