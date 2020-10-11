function getVar() {
    document.getElementById("var").innerHTML = max;
    
};


var clicks = 0;
function counter() {
    clicks += 1;
    if (clicks == 10) {
        clicks = 0
    };
    document.getElementById("clicks").innerHTML = clicks;
};

