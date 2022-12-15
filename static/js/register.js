
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const handleToggleInput = (e) => {
if(showPasswordToggle.textContent === "SHOW PASSWORD"){
   showPasswordToggle.textContent = "HIDE PASSWORD";
   id_password.setAttribute("type","text")
}else{
    showPasswordToggle.textContent = "SHOW PASSWORD";

    id_password.setAttribute("type","password");
}
};
showPasswordToggle.addEventListener("click", handleToggleInput);


