function check(){
  const check_box = document.getElementById("check");
  const button = document.getElementById("button")
  if(check_box.checked){
    button.disabled = false;
  }else{
    button.disabled = true;
  }
};