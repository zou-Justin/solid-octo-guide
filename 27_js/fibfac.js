// Team Tofu :: Justin Zou(Piggy), Annabel Zhang(Mang)
// 2022-02-03
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fact(n){
    if (n == 0){
        return 1;
    }
    else{
        return fact(n-1) * n
    }
}

function fib(n){
    if (n <= 1){
        return n;
    }
    return fib(n-1) + fib(n-2)
}
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
