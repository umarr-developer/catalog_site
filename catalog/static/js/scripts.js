const auth_modal = document.getElementById("auth_modal");
const auth_button = document.getElementById("auth_button");
const auth_close = document.getElementById("auth_close")

const reg_modal = document.getElementById("reg_modal");
const reg_button = document.getElementById("reg_button");
const reg_close = document.getElementById("reg_close")


auth_button.onclick = function () {
    auth_modal.style.display = "block";
}

auth_close.onclick = function () {
    auth_modal.style.display = "none";
}


reg_button.onclick = function (){
    reg_modal.style.display = "block";
}

reg_close.onclick = function () {
    reg_modal.style.display = "none";
}