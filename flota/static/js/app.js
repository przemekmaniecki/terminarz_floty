document.addEventListener("DOMContentLoaded", function () {
var rows = document.querySelectorAll(".rows");
    for (i=0; i<rows.length; i++){
rows[i].addEventListener("mouseover", function (event) {
    this.style.backgroundColor="cadetblue";
    });
rows[i].addEventListener("mouseout", function (event) {
    this.style.backgroundColor="white"
});
}
var url = window.location.href;
var url2 = document.URL;
console.log(url);
console.log(url2);
var button = document.querySelector("#button");
var button2=document.querySelector("#button2")
if (url.includes("search")) {
    console.log("Ala ma psa" );

} else {
    console.log("Ala ma kota" );
    button.style.visibility="hidden";
    button2.style.visibility="visible";
}
});