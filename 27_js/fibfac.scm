Team Tofu :: Justin Zou(Piggy), Annabel Zhang(Mang)
Softdev Pd2
K27 -- Basic functions in JavaScript
2022-02-03r


(define fact
  (lambda (n)
    (if (= n 0 )
        1
        (*(fact(- n 1))n)
        )
    )
  )



(define fib
    (lambda (n)
        (if (<= n 1)
            n
        (+ (fib(- n 1))(fib(- n 2)))
                )
        )
    )
