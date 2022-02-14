// Team Tofu :: Justin Zou, Annabel Zhang
// SoftDev pd2
// K30: JSDraw
// 2022-02-14t
// --------------------------------------------------


 var c = document.getElementById("slate");

 var ctx = c.getContext("2d");

 var mode = "rect";

 var toggleMode = (e) => {
  //  console.log(toggling);
   var btT = document.getElementById("buttonToggle");
   if (btT.innerHTML == "rect|circ"){
      console.log("HELoo");
   }
   else{
    console.log("no");
   }
   btT.addEventListener('click', toggleMode);
 }
 toggleMode();