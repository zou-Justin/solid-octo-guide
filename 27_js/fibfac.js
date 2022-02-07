// Team Tofu :: Justin Zou(Piggy), Annabel Zhang(Mang)
// Softdev Pd2
// K27 -- Basic functions in JavaScript
// 2022-02-03r


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

