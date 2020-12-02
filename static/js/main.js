const check_box = document.getElementById("check_box");
const button = document.getElementById("submit_button")
function check(){
  if(check_box.checked){
    button.disabled = false;
  }else{
    button.disabled = true;
  }
};