Лабораторна робота розроблялась під варіантом №4(В).

Функції:
y=x^4*4.968+x^3*2.271-x^2*3.589+x*3.317
y=x^3*3.774-x^2*2.298+x*3.873
y=x^2*4.165+x*3.363
y=x*6.363
Діапазон допустимих значень: [X>=1.045, X<=90.88]

Опис класів програми

Програма для обчислення формул за заданим значенням на Python 3 складається з класу Main. Який включає в себе метод __init__ для ініціалізації основного значення для знаходження значення Y по формулах:
y=x^4*4.968+x^3*2.271-
x^2*3.589+x*3.317
y=x^3*3.774-x^2*2.298+x*3.873
y=x^2*4.165+x*3.363
y=x*6.363
Також цей метод перевіряє основні вимоги до значення Х, це число в межі X>=2.557 або X<=36.868 та чи це число взагалі, виводить попередження про помилку при введені не чисел, а при введені числа яке не попадає в задані межі просить повторити введення числа Х
Також цей клас  включає метод outputting, який виводить числа які програма вирахувала при обрахуванні виразів за допомогою підстановки X
