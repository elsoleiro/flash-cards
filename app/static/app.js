let max;
const myForm = document.querySelector("#my-form-id")
myForm.addEventListener("click", (e) => {
  e.preventDefault()
  const myInput = document.querySelector("#my-name-input-id")
  const myInputValue = myInput.value
  max = parseInt(myInput.value) + 1
  const myOutput = document.querySelector(".output")
  myOutput.textContent= myInputValue
});
var clicks = 0;
function counter() {
    clicks += 1;
    if (clicks == max) {
        clicks = 0
    };
    document.getElementById("clicks").innerHTML = clicks;
};

