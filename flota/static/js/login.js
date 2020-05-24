document.addEventListener("DOMContentLoaded", function () {

    var info = document.querySelector("#bad_login_text");
    var stroboskop = document.querySelectorAll("#stroboskop");
    var url = window.location.href;
    var button = document.querySelector("#button");
    function visibile() {
            for (i = 0; i < stroboskop.length; i++) {
        stroboskop[i].style.visibility = "visible";
    }
    }
if (info.innerText.includes("Nieudane logowanie")) {
    visibile();
}
if (url.includes("login")) {
button.style.visibility="hidden";
}
});
