const auth_form = document.getElementById("auth_form");
const auth_button = document.getElementById("auth_button");
const auth_close = document.getElementById("auth_close")

const reg_form = document.getElementById("reg_form");
const reg_button = document.getElementById("reg_button");
const reg_close = document.getElementById("reg_close")


auth_button.onclick = function () {
    auth_form.style.display = "block";
}

auth_close.onclick = function () {
    auth_form.style.display = "none";
}


reg_button.onclick = function (){
    reg_form.style.display = "block";
}

reg_close.onclick = function () {
    reg_form.style.display = "none";
}