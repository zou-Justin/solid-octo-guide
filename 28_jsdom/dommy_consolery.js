// Team Tofu: Justin Zou, Annabel Zhang, Jessie Xie
// SoftDev pd2
// K28 -- Manipulating the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

// i and j are now these values when you type them in the console
var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
// In the console you would call it by name f(x) so f(20) returns 50
// Question: why would do we have to have to assign a variable to the function instead of simply doing function f(x)
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
// Object declaration is a dictionary
// You can call the functions within this dictionary with something like 0["func"](2)
// Can see the contents of the value with the key
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

// adds an item to the list
// document.createElement creates the html tag that is given in the parameter
// Innerhtml seems to be what the list states
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// This simply removes one of the items on the list.
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


// It makes the first two items of the list red
// This is because only the first two items don't have any classes on it 
// Adding red adds it to the end so it doesn't ovveride the other classes
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

// This makes all of the elements without a class tag alternate between red and blue
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};




// var buttonFunction = function() { 
//   var bt =  document.createElement("button");
// };
//team dodo

function buttonFunction(){
  var bt = document.createElement("button");
}



function fib(n){
  if (n <= 1)
    return n
  return (fib(n-1) + fib(n-2))
 }

function fact(n){
  if (n == 0)
    return 1
  return n * fact(n-1)
}

function gcd(a,b){
  if (a > b)
    s = b
  else
    s = a
  for (let i = 1; i < s; i++){
    if (a%i == 0 && b%i == 0)
      gcd = i
  }
  return gcd
}
