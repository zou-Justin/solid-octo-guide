// Team Tofu :: Justin Zou, Annabel Zhang
// SoftDev pd2
// K30: JSDraw
// 2022-02-14t
// --------------------------------------------------


 var c = document.getElementById("slate");

 var ctx = c.getContext("2d");

 var mode = "rect";

 var toggleMode = (e) => {
  //  console.log("toggling");
   if (btT.innerHTML == "rect|circ"){
     btT.innerHTML = "rect"
   }
   else if (btT.innerHTML == "rect"){
      btT.innerHTML = "circ"
   }
   else{
      btT.innerHTML = "rect"
   }
 }
 
 var drawRect = function(e){
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    ctx.fillRect(mouseX, mouseY, 100, 100);
 }

 var drawCircle = (e) => {
   var mouseX = e.clientX;
   var mouseY = e.clientY;
   ctx.beginPath();
   ctx.arc(mouseX,mouseY,100,0, 2 * Math.PI);
   ctx.stroke();
   ctx.fill();
 }
 
 var wipeCanvas = () => {
   ctx.clearRect(0, 0, c.width, c.height);

 }

 var draw = (e) => {
  
   if (c.getContext) {
     if (btT.innerHTML == "rect"){
        drawRect(e);
     }
     else if (btT.innerHTML == "circ"){
        drawCircle(e);
     }
     
   }

 }

c.addEventListener("click",draw);
var btT = document.getElementById("buttonToggle");
btT.addEventListener('click', toggleMode);
var clearBt = document.getElementById("buttonClear");
clearBt.addEventListener('click', wipeCanvas);
 toggleMode();