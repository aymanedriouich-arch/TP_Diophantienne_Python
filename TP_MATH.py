Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...                 print(f"{A} = {B}*{Q} + {R}")
...             print(f"\nPGCD({a},{b}) = {d}")
...             print(f"Pas de solution entière car {d} ne divise pas {c}.\n")
...             print("-" * 60)
...             continue
...
...         d, x0, y0, kx, ky, steps, u, v = result
...         print("\nÉtapes (division euclidienne) :")
...         for A, B, Q, R in steps:
...             print(f"{A} = {B}*{Q} + {R}")
...         print(f"\nPGCD({a},{b}) = {d}")
...         print(f"Coefficients de Bézout : u = {u}, v = {v}")
...         print(f"Vérification : {a}({u}) + {b}({v}) = {a*u + b*v}")
...
...         print("\n--- Solution diophantienne ---")
...         print(f"Solution particulière : (x0, y0) = ({x0}, {y0})   (car c/d = {c}//{d} = {c//d})")
...         print("Solution générale :")
...         print(f"x = {x0} + ({kx})*t")
...         print(f"y = {y0} - ({ky})*t")
...         print("pour tout t ∈ Z")
...         print("\nExemples t = -2,-1,0,1,2 :")
...         for t in (-2, -1, 0, 1, 2):
...             xx = x0 + kx * t
...             yy = y0 - ky * t
...             print(f"t={t} -> (x,y)=({xx},{yy})    vérifie {a}{xx} + {b}{yy} = {a*xx + b*yy}")
...         print("-" * 60 + "\n")
...
... if _name_ == "_main_":
...     main()
...
