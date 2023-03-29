function changeColor(check_sd, sd, span){
    spanText = document.querySelector(span);
    var color = "black";
    if (check_sd >= (sd * 2)){
        color = "red";
    } 
    else if (check_sd >= sd){
        color = "orange";
    }
    spanText.style.color = color;
}
