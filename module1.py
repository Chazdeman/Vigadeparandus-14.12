from random import *

def arvud_loendis(): #компьютерные списки
    s=[]
    pos=[]
    neg=[]
    null=[]
    kesk=[]
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:#mini=100 ,maxi=5 => mini=5 , maxi=100
        vahetus(mini,maxi)
    generator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """Преравнивае переменных к одному значению
    :param int a: минимальное значение min,  которое больше чем max
    :param int b: максимальное значение max,  которое меньше чем min
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generator(n:int,loend:list,a:int,b:int):
    """Генерирует рандомные целые числа
    :param int n: общее количество чисел
    :param list loend: список чисел
    :param int a: Минимальное число для генерации
    :param int b: Максимальное число для генерации
    :rtype: int
    """
    for i in range(n):
        loend.append(randint(a,b))
    
def jagamine(loend:list,p:list,n:list,null:list): #Деление
    """Делит значение в список
    :param list loend: список чисел
    :param list p: 数字
    :param list n: общее количество чисел
    :param list null: список нулевых элементов
    :rtype: list
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            null.append(el)

def keskmine(loend:list): #средяя
    """Находит средние число положительных чисел
    :param list loend: Список чисел 
    :rtype: int
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Добавляет элемент и сортирует список
    :param list loend: список чисел
    :param float el: список дробных чисел
    :rtype: float
    """
    loend.append(el)
    loend.sort()

arvud_loendis()