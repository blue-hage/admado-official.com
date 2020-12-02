const check_box = document.getElementById("check_box");
const button = document.getElementById("submit_button")
function check(){
  if(check_box.checked){
    button.disabled = false;
  }else{
    button.disabled = true;
  }
};

const check_box_cli = document.getElementById("check_box_cli");
const button_cli = document.getElementById("submit_button_cli")
function check_cli(){
  if(check_box_cli.checked){
    button_cli.disabled = false;
  }else{
    button_cli.disabled = true;
  }
};