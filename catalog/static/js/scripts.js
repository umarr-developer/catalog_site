const modal = document.getElementById("modal");

const button = document.getElementById("register");

const close = document.getElementById("close")

button.onclick = function () {
    modal.style.display = "block";
}

close.onclick = function () {
    modal.style.display = "none";
}
