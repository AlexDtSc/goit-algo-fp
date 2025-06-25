# ########### Фінальний проєкт. Course 'Basic Algorithms and Data Structures'


### Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

'''
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

Критерії прийняття завдання 1:
- Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.
- Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.
- Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.
'''

# ОдноЗв'язний список


class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def insert_before(self, next_node_data, data):
        if self.head is None:
            print("Список порожній.")
            return
        # Якщо вставка перед головою
        if self.head.data == next_node_data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        # Пошук next_node у середині списку
        prev = None
        current = self.head
        while current and current.data != next_node_data:
            prev = current
            current = current.next
        if current is None:
            print("Вузол, перед яким треба вставити, не знайдено.")
            return

        # Вставка нового вузла між prev і current
        new_node = Node(data)
        new_node.next = current
        prev.next = new_node 
     

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next


## 1.1) Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами

  def reverse_list(self):
    if self.head is None:
            print("Список порожній.")
            return
    prev = None          # Початково попередній вузол — None
    current = self.head  # Поточний вузол — з голови списку

    while current:
        next_node = current.next  # Зберігаємо посилання на наступний вузол
        current.next = prev       # Перевертаємо посилання current → prev
        prev = current            # Зсуваємо prev вперед
        current = next_node       # Зсуваємо current вперед

    self.head = prev  # Нова голова списку — останній вузол, який був current
    '''
    prev = None
    current = Node(1)

    1-й оберт:
    next_node = 2

    current.next = None (тобто посилання "1 →" розривається і стає "1 → None")

    prev = 1

    current = 2

    2-й оберт:
    next_node = 3

    current.next = 1 (тепер "2 → 1 → None")

    prev = 2

    current = 3

    3-й оберт:
    next_node = None

    current.next = 2 (тепер "3 → 2 → 1 → None")

    prev = 3

    current = None

    Завершення:
    self.head = prev → тобто head тепер вказує на 3
    '''

## 1.2) Алгоритм сортування для однозв'язного списку, наприклад, сортування вставками

  def insertion_sort_list(self):
      # Початок відсортованого списку — порожній
      sorted_head = None

      # Поточний вузол для вставки
      current = self.head

      # Проходимо всі вузли один за одним
      while current:
          next_node = current.next  # Зберігаємо наступний вузол
          # Вставляємо current у відсортований список
          if sorted_head is None or current.data < sorted_head.data:
              # Вставка на початок відсортованого списку
              current.next = sorted_head
              sorted_head = current
          else:
              # Пошук позиції вставки в середині відсортованого списку
              sorted_current = sorted_head
              # Шукаємо місце, де current.data >= sorted_current.data
              while (sorted_current.next is not None and 
                    sorted_current.next.data < current.data):
                  sorted_current = sorted_current.next
              # Вставка current після sorted_current
              current.next = sorted_current.next
              sorted_current.next = current
          # Переходимо до наступного вузла у вихідному списку
          current = next_node

      # Оновлюємо голову списку на відсортований список
      self.head = sorted_head
'''
      # Алгоритм сортування вставками у звичайному вигляді для наочності
      def insertion_sort(lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j >=0 and key < lst[j] :
                    lst[j+1] = lst[j]
                    j -= 1
            lst[j+1] = key 
        return lst
        '''

##############################
# Створення однозв'зязного списку №1
##############################
llist1 = LinkedList()

# Вставляємо вузли в початок
llist1.insert_at_beginning(5)
llist1.insert_at_beginning(10)
llist1.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist1.insert_at_end(20)
llist1.insert_at_end(25)

# Друк зв'язного списку 1
print("Зв'язний список 1:")
llist1.print_list()

# Видаляємо вузол
llist1.delete_node(10)

print("\nЗв'язний список 1 після видалення вузла з даними 10:")
llist1.print_list()


''' 
# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
  print(element.data)
'''

#========================
# Тестування
#========================

## 1.1) Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами
llist1.reverse_list()
print("\nЗв'язний список 1 після реверсування")
llist1.print_list()


## 1.2) Алгоритм сортування для однозв'язного списку, наприклад, сортування вставками

llist1.insertion_sort_list()
print("\nЗв'язний список 1 після сортування")
llist1.print_list()


## 1.3) Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    dummy = Node()  # 1. Пустий вузол-«заглушка» для зручності
    tail = dummy    # 2. Вказівник на останній елемент у новому списку

    current1 = list1.head  # 3. current1, current2 — вказівники на голови обох списків.
    current2 = list2.head

    # 4. Поки обидва списки мають елементи - Додаємо менший вузол до tail.next, зсуваємо tail та відповідний current.
    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next  # Перемістити кінець нового списку. 

    # 5. Додаємо залишки одного з двох списків
    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    # 6. Повертаємо новий список без dummy
    merged_list = LinkedList()        # Створюємо новий LinkedList-об’єкт.
    merged_list.head = dummy.next     # Головою буде dummy.next — тобто перший реальний вузол списку.
    return merged_list

'''
Покроковий опис функції

# 1. dummy = Node() — створюємо фіктивний вузол (він не містить значення), щоб уникнути перевірок на порожній список при додаванні.
# 2. tail = dummy — tail вказує на останній елемент нового списку (спочатку dummy).
# 3. current1, current2 — вказівники на голови обох списків.
# 4. Поки обидва списки не закінчилися, порівнюємо поточні значення:
#     - Додаємо менший вузол до tail.next, зсуваємо tail та відповідний current.
# 5. Якщо один список закінчився — підв’язуємо залишки іншого.
# 6. Створюємо новий список, head = dummy.next — бо dummy сам не несе даних.
# '''

##############################
# Створення однозв'зязного списку №2
##############################

llist2 = LinkedList()
# Вставляємо вузли в початок
llist2.insert_at_end(1)
llist2.insert_at_end(2)
llist2.insert_at_end(3)


# Друк зв'язного списку 1
print("Зв'язний список 1:")
llist1.print_list()

# Друк зв'язного списку 2
print("Зв'язний список 2:")
llist2.print_list()

## 1.3) Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

print("Об'єднаний відсортований список:")
merged = merge_sorted_lists(llist1, llist2)
merged.print_list()







### Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

'''

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. 
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

Критерії прийняття завдання 2:
- Код виконується. Програма візуалізує фрактал “дерево Піфагора”.
- Користувач має можливість вказати рівень рекурсії.
'''
import turtle
import math

def draw_tree(t, length, depth):
    if depth == 0:                # Якщо глибина дорівнює нулю, зупиняємо малювання — це кінцева точка дерева.
        return

    # Малюємо гілку
    t.forward(length)             # Черепашка рухається вперед на length пікселів — це одна гілка дерева.
    t.speed(0)                    # t.speed(0) — максимальна швидкість малювання.

    # Зберігаємо позицію та напрям - це потрібно, щоб повернутись назад, коли закінчимо малювати гілку.
    x, y = t.pos()                # t.pos() — координати черепашки (x, y).
    angle = t.heading()           # t.heading() — напрямок, куди вона "дивиться" (в градусах).

    # Ліва гілка                                         (Малювання лівої гілки)
    t.left(45)                                         # t.left(45) — повертаємо на 45° вліво.
    draw_tree(t, length * math.sqrt(2)/2, depth - 1)   # draw_tree(...) — викликаємо функцію ще раз, з меншою довжиною гілки (√2 / 2 ≈ 0.707) і меншою глибиною (depth - 1). Це рекурсивний виклик — основа фракталу.

    # Повертаємось назад з піднятим олівцем (не малюємо) після завершення лівої гілки
    t.penup()             # Піднімаємо "олівець", щоб не малювати лінії.
    t.goto(x, y)          # Повертаємось у збережену позицію x, y.
    t.setheading(angle)   # Встановлюємо збережений напрямок.
    t.pendown()           # Опускаємо "олівець", готові малювати наступну гілку.


    # Права гілка
    t.right(45)   # те саме, що і для лівої гілки, але повертаємо направо.
    draw_tree(t, length * math.sqrt(2)/2, depth - 1)

    # Повертаємось                             Завершуємо праву гілку і повертаємось до попереднього стану для наступного кроку.
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

def build_pifagor_tree(recursion_depth):       # Головна функція, яка запускає малювання дерева.
    screen = turtle.Screen()                   # Створюємо вікно для малювання. Налаштування вікна
    screen.setup(width=800, height=800)        # Встановлюємо розміри вікна.
    screen.bgcolor("white")                    # Встановлюємо білий фон вікна 

    t = turtle.Turtle()                        # Створюємо об’єкт черепашки.
    t.hideturtle()                             # Приховуємо її, щоб не заважала візуально.
    t.color("brown")                           # Встановлюємо коричневий колір для гілок.
    t.speed(0)                                 # Встановлюємо максимальну швидкість.

    t.penup()
    t.goto(0, -300)                            # Черепашка стає в центр по горизонталі, але вниз по вертикалі (y = -300).
    t.setheading(90)                           # setheading(90) — дивиться вгору (90°).
    t.pendown()                                # Починаємо малювати - опускаємо олівець вниз, щоб почати малювати

  # Починаємо малювати.
    draw_tree(t, 100, recursion_depth)         # Стартуємо з гілки довжиною 100 пікселів.
    screen.mainloop()                          # Запускаємо нескінченний цикл, щоб вікно не закривалось одразу після малювання.

# Запитуємо глибину у користувача
depth = int(input("Введіть рівень рекурсії (0–8): "))
build_pifagor_tree(depth)

'''
Це приклад рекурсивної програми для побудови фракталу:
В кожному кроці вона малює гілку.
І двічі викликає себе, щоб намалювати менші гілки — зліва і справа.
Це і є суть рекурсії: функція викликає саму себе з меншими параметрами.
'''





### Завдання 3. Дерева, алгоритм Дейкстри

'''

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

Критерії прийняття завдання 3:
- Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з використанням бінарної купи (піраміди).
- У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору вершин та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.
'''


'''
Питання: - Чому саме піраміда (мінімальна купа) ?
Відповідь: - Замість того, щоб кожного разу шукати "найдешевшу" вершину вручну серед усіх — ми кладемо всі вершини у піраміду, яка завжди дозволяє взяти найменший елемент за O(log N). 

Алгоритм крок за кроком:

1. Стартує з A (шлях до себе = 0)
2. Дивиться на сусідів A (B та C), і записує їх поточні найкоротші відстані.
3. Потім переходить до тієї вершини, куди найшвидше дістатися (наприклад, B).
4. Оновлює відстані для її сусідів, якщо новий шлях коротший.
5. І так далі, поки не перевірить усі вершини.

A: 0
B: ∞
C: ∞
D: ∞
E: ∞

Крок 1: Виймаємо 'A'
- current_vertex = A, current_distance = 0
- Сусіди: B (вага 5), C (вага 10)

→ Оновлюємо:
- B = min(∞, 0+5) = 5
- C = min(∞, 0+10) = 10
- Черга: [(5, 'B'), (10, 'C')]

Крок 2: Виймаємо 'B'
- current_vertex = B, current_distance = 5
- Сусіди: A (5), D (3)
  -- A вже оброблено
  -- D: ∞ → min(∞, 5+3) = 8
- Черга: [(8, 'D'), (10, 'C')]

Крок 3: Виймаємо 'D'
- current_vertex = D, current_distance = 8
- Сусіди: B (3), C (2), E (4)
  -- B — вже коротший шлях є
  -- C: 10 → min(10, 8+2) = 10 (нічого не змінюється)
  -- E: ∞ → min(∞, 8+4) = 12
- Черга: [(10, 'C'), (12, 'E')]

Крок 4: Виймаємо 'C'
- current_vertex = C, current_distance = 10
- Сусіди: A, D — оброблено

Крок 5: Виймаємо 'E'
- Сусід D — оброблено

'''
import heapq

import networkx as nx
import matplotlib.pyplot as plt

## Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

## Реалізація алгоритму Дейкстри використанням бінарної купи (піраміди)

def dijkstra(graph, start):
    # Ініціалізуємо найкоротші шляхи: нескінченність для всіх, крім стартової вершини
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0

    # Черга з пріоритетом: (вага, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо ми вже знайшли коротший шлях — пропускаємо
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Перевірка сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайшли коротший шлях
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

## Використання алгоритму Дейкстри використанням бінарної купи (піраміди)

shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)



## Візуалізація графа

G = nx.Graph()
# Додавання ребер з вагами
for u in graph:
    for v, weight in graph[u].items():
        G.add_edge(u, v, weight=weight)

pos = nx.spring_layout(G, seed = 42)
nx.draw_networkx_nodes(G, pos, node_size = 700)
nx.draw_networkx_edges(G, pos, width = 2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
nx.draw_networkx_labels(G, pos, font_size = 20, font_family = 'sans-serif')

plt.axis('off')
plt.show()


'''
G = nx.Graph(graph) — створює граф із словника graph.
pos = nx.spring_layout(G) — визначає, де будуть розташовані вузли (алгоритм пружинного макету).
nx.draw_networkx_nodes(...) — малює вершини (вузли).
nx.draw_networkx_edges(...) — малює ребра.
nx.get_edge_attributes(...) — дістає ваги ребер (якщо вони задані).
nx.draw_networkx_edge_labels(...) — показує ваги на ребрах.
nx.draw_networkx_labels(...) — підписує вузли.

plt.axis('off') — ховає координатну сітку.
plt.show() — показує результат.
'''


####### Додатково
### ✅ Деталізований покроковий код для розуміння: Дейкстра + пояснення + маршрут + візуалізація

# import heapq
# import networkx as nx
# import matplotlib.pyplot as plt

# # === Граф ===
# graph = {
#     'A': {'B': 5, 'C': 10},
#     'B': {'A': 5, 'D': 3},
#     'C': {'A': 10, 'D': 2},
#     'D': {'B': 3, 'C': 2, 'E': 4},
#     'E': {'D': 4}
# }

# # === Алгоритм Дейкстри з поясненням ===
# def dijkstra_verbose(graph, start):
#     shortest_paths = {vertex: float('inf') for vertex in graph}
#     shortest_paths[start] = 0

#     previous_nodes = {vertex: None for vertex in graph}

#     priority_queue = [(0, start)]

#     while priority_queue:
#         current_distance, current_vertex = heapq.heappop(priority_queue)
#         print(f"\n🟢 Розглядаємо вершину: {current_vertex} (поточна відстань: {current_distance})")

#         if current_distance > shortest_paths[current_vertex]:
#             continue

#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight

#             print(f"  🔹 Перевіряємо сусіда {neighbor} з вагою {weight}: нова відстань {distance}", end='')

#             if distance < shortest_paths[neighbor]:
#                 shortest_paths[neighbor] = distance
#                 previous_nodes[neighbor] = current_vertex
#                 heapq.heappush(priority_queue, (distance, neighbor))
#                 print(f" — ✅ оновлено (кращий шлях)")
#             else:
#                 print(f" — ❌ залишаємо як є")

#     return shortest_paths, previous_nodes

# # === Відновлення шляху ===
# def reconstruct_path(previous_nodes, target):
#     path = []
#     while target is not None:
#         path.append(target)
#         target = previous_nodes[target]
#     return list(reversed(path))

# # === Виконання ===
# shortest_paths, previous_nodes = dijkstra_verbose(graph, 'A')

# print("\n📊 Найкоротші відстані від A:")
# for node in shortest_paths:
#     print(f"A → {node}: {shortest_paths[node]}")

# print("\n🧭 Найкоротші маршрути:")
# for node in graph:
#     path = reconstruct_path(previous_nodes, node)
#     print(f"A → {node}: {' → '.join(path)}")

# # === Візуалізація ===
# G = nx.Graph()
# for u in graph:
#     for v, weight in graph[u].items():
#         G.add_edge(u, v, weight=weight)

# pos = nx.spring_layout(G, seed=42)

# # Виділяємо шляхи від 'A' до всіх
# edge_colors = []
# edge_widths = []

# # Отримуємо всі шляхи
# all_paths = []
# for node in graph:
#     if node == 'A':
#         continue
#     path = reconstruct_path(previous_nodes, node)
#     all_paths.append(path)

# highlight_edges = set()
# for path in all_paths:
#     for i in range(len(path) - 1):
#         edge = tuple(sorted((path[i], path[i+1])))
#         highlight_edges.add(edge)

# for u, v in G.edges():
#     edge = tuple(sorted((u, v)))
#     if edge in highlight_edges:
#         edge_colors.append("red")
#         edge_widths.append(3)
#     else:
#         edge_colors.append("gray")
#         edge_widths.append(1)

# # Візуалізація
# plt.figure(figsize=(8, 6))
# nx.draw_networkx_nodes(G, pos, node_size=700)
# nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_colors)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
# plt.title("🔴 Найкоротші шляхи від A")
# plt.axis('off')
# plt.show()







### Завдання 4. Візуалізація піраміди


'''
Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.

import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
 👉🏻 Примітка. Суть завдання полягає у створенні дерева із купи.

 
Критерії прийняття завдання 4:
- Код виконується. Функція візуалізує бінарну купу.
'''


import uuid            # генерує унікальні ідентифікатори для кожного вузла дерева.

import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None        # left, right — посилання на лівого та правого нащадків.
    self.right = None        
    self.val = key     # key — значення вузла.
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла, необхідний, оскільки два вузли можуть мати однакові значення val, але мають бути різними об'єктами в графі.

# graph — об’єкт типу networkx.DiGraph() (напрямлений граф), node — поточний вузол дерева, pos — словник позицій (для побудови), x, y — координати вузла на площині, layer — рівень глибини (для визначення розташування вузлів)
def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла. Додає вузол до графу з вказаним кольором та міткою.
    if node.left:       # Якщо у вузла є лівий нащадок,  
      graph.add_edge(node.id, node.left.id) # створює ребро node → left,
      l = x - 1 / 2 ** layer  # Позиції x ± 1 / 2**layer зменшують відстань між вузлами на кожному новому рівні — це створює правильну "ялинкоподібну" форму дерева.
      pos[node.left.id] = (l, y - 1)  # обчислює позицію та викликає функцію рекурсивно.
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # рекурсивний виклик
    if node.right:      # Те саме для правого нащадка.
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):     # Ця функція викликає add_edges(...), щоб заповнити граф, і малює дерево.
  tree = nx.DiGraph() 
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)   # Створює порожній граф і словник позицій, після чого заповнює дерево з кореня tree_root.

  colors = [node[1]['color'] for node in tree.nodes(data=True)] # Отримує список кольорів вузлів та їхні мітки для відображення.
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))  # Малює граф за координатами pos, без стрілок, з мітками та кольорами.
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


'''
Побудова дерева такого вигляду:

         0
       /   \
      4     1
     / \    /
    5  10  3

📌 Підсумок

Цей код:

- створює дерево з об'єктів класу Node
- використовує networkx для побудови графа на основі цього дерева
- викликає рекурсію, щоб пройти всі гілки дерева
- малює візуальне представлення дерева

Хочеш — можу змінити кольори вузлів або додати можливість введення дерева вручну.
    
'''


##### Розв'язок. Реалізація функції побудови дерева бінарної купи


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])  # створюємо вузол з відповідним значенням.

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)

    return node

'''
Бінарна купа в масиві з індексацією 0-based має наступну структуру:

heap[index] — це поточний елемент
left = 2 * index + 1
right = 2 * index + 2

- Ця функція рекурсивно обходить список і створює об'єкти Node, формуючи з них дерево:
кожен елемент — новий вузол
- Його діти — рекурсивний виклик на відповідні індекси
'''


if __name__ == '__main__':
    # Припустимо, що у нас є бінарна купа у вигляді списку
    heap_list = [1, 3, 5, 7, 9, 2]
    
    heapq.heapify(heap_list)
    print(type(heap_list))
    print(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)

    # Візуалізація дерева бінарної купи
    draw_tree(heap_tree_root)








### Завдання 5. Візуалізація обходу бінарного дерева

'''

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.


👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

Критерії прийняття завдання 5:
- Програмно реалізовано алгоритми DFS і BFS для візуалізації обходу дерева в глибину та в ширину. Використано стек та чергу.
- Кольори вузлів змінюються від темних до світлих відтінків залежно від порядку обходу.

'''


import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ID для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def generate_color(step, total_steps):
    """Генерує колір від темного до світлого залежно від кроку."""
    # Від синього (0, 0, 255) до червоного (255, 0, 0)
    start_color = (0, 0, 255)     # Синій
    end_color = (255, 0, 0)       # Червоний

    ratio = step / max(total_steps - 1, 1)

    r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)

    return f'#{r:02x}{g:02x}{b:02x}'


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            color = generate_color(step, total_steps)
            colors[node.id] = color
            step += 1
            stack.append(node.right)
            stack.append(node.left)

    return colors


def bfs_visualize(root, total_steps):
    visited = set()
    queue = [root]
    colors = {}
    step = 0

    while queue:
        node = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            color = generate_color(step, total_steps)
            colors[node.id] = color
            step += 1
            queue.append(node.left)
            queue.append(node.right)

    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    # Бінарна купа як список
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)

    # Побудова дерева
    heap_tree_root = build_heap_tree(heap_list)

    # Підрахунок вузлів для градієнта
    total_steps = count_nodes(heap_tree_root)

    # DFS обход
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    # BFS обход
    # Щоб мати нові вузли без кольорів, перебудовуємо дерево
    heap_tree_root = build_heap_tree(heap_list)
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)







### Завдання 6. Жадібні алгоритми та динамічне програмування

'''
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування 
для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. 
Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

- Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
- Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

Критерії прийняття завдання 6:
- Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. Код виконується і повертає назви страв, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
- Програмно реалізовано функцію, яка використовує принцип динамічного програмування. Код виконується і повертає оптимальний набір страв для максимізації калорійності при заданому бюджеті.
'''

class Item:
    
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost 
        self.calories = calories
        self.ratio = calories / cost 
    
    def __repr__(self):
        return f'{self.name} ({self.cost} грн, {self.calories} кал, {self.ratio} кал / грн.)'

items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}

## Жадібний алгоритм

def greedy_algorithm(items: dict, budget: int):
    
    # Перетворюємо словник продуктів та їхніх вартостей з калоріями у список об'єктів класу Item
    items_list = []
    for name, product in items.items():
        items_class = Item(name, product["cost"], product["calories"])
        items_list.append(items_class)
    
    items_list.sort(key = lambda x: x.ratio, reverse = True) # сортуємо продукти по ratio від більшого до меншого
    
    total_utility = 0
    final_list = []
    
    for itemm in items_list:
        if budget >= itemm.cost:
            total_utility += itemm.calories
            budget -= itemm.cost
            final_list.append(itemm)
    return final_list, total_utility, budget
  

budget = 100

final_list, total_utility, budget = greedy_algorithm(items, budget)
print(f'При бюджеті = {budget} грн Жадібний алгоритм, максимізуючи співвідношення калорій до вартості - Максимальна кількість калорій {total_utility}, обирає наступні страви: ')
for itemm in final_list:
    print(f'   - Назва {itemm.name}, вартість {itemm.cost}, калорії {itemm.calories}, коефіцієнт калорії/вартість {itemm.ratio:.2f}') 




## Алгоритм Динамічного програмування

items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    # Створення DP-таблиці: dp[i][b] — максимум калорій, які можна отримати з перших i предметів при бюджеті b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                # максимум з (чи взяти страву, чи не взяти страву)
                dp[i][b] = max(dp[i - 1][b - cost] + cal,  
                               dp[i - 1][b])
            else:
                # не можемо взяти страву
                dp[i][b] = dp[i - 1][b]

    # Відновлення вибраних предметів
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = item_names[i - 1]
            chosen_items.append(name)
            b -= items[name]["cost"]

    total_calories = dp[n][budget]
    total_cost = budget - b
    chosen_items.reverse()  # Щоб виводити в правильному порядку

    return total_calories, total_cost, chosen_items


budget = 100
calories, cost, chosen = dynamic_programming(items, budget)

print(f"Максимальні калорії: {calories}")
print(f"Загальна вартість: {cost}")
print(f"Обрані страви: {chosen}")









### Завдання 7. Використання методу Монте-Карло

'''

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. 
Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Сума   Ймовірність
2      2.78  % (1/36)
3      5.56  % (2/36)
4      8.33  % (3/36)
5      11.11 % (4/36)
6      13.89 % (5/36)
7      16.67 % (6/36)
8      13.89 % (5/36)
9      11.11 % (4/36)
10     8.33  % (3/36)
11     5.56  % (2/36)
12     2.78  % (1/36)

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.


Критерії прийняття завдання 7:
- Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і побудови таблиці сум та їх імовірностей за допомогою методу Монте-Карло.
- Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, 
підраховує, скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.
- Створено таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
- Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих за допомогою методу Монте-Карло результатів та результатів аналітичних розрахунків. 
Висновки оформлено у вигляді файлу readme.md фінального завдання.

'''

import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Симуляція кидків
    results = []
    for _ in range(num_rolls):
        result = random.randint(1,6) + random.randint(1,6)
        results.append(result)
    
    possible_results = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    unique = {}
    for i, digit in enumerate(possible_results):
        unique[digit] = results.count(digit) 

    unique_probabilities = {}
    number_of_digits = sum(list(unique.values()))
    for digit, value in unique.items():
            unique_probabilities[digit] =  value / number_of_digits
    return unique_probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірність суми чисел на двох кубиках для {accuracy} експериментів')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1_000, 10_000, 100_000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)

        # Друк значень та їхніх ймовірностей
        print(f'Друк значень та їхніх ймовірностей при {accuracy} експериментах: {probabilities}')



#==============================================#
#### Висновки до завдання 7. Метод Монте-Карло
#==============================================#

'''
Завдяки використанню методу Монте-Карло бачимо, що зі збільшенням кількості експериментів (від 100 до 100_000) значення ймовірностей випадання сум від 2 до 12, 
порахованих за методом Монте-Карло, максимально наближається до табличних значень (аналітичних розрахунків), що свідчить про високу точність обрахунків методу Монте-Карло при великій кількості експериментів.


Друк значень та їхніх ймовірностей при 100 експериментах:    {2: 0.03, 3: 0.08, 4: 0.11, 5: 0.08, 6: 0.1, 7: 0.22, 8: 0.15, 9: 0.13, 10: 0.03, 11: 0.05, 12: 0.02}
Друк значень та їхніх ймовірностей при 1000 експериментах:   {2: 0.015, 3: 0.061, 4: 0.075, 5: 0.118, 6: 0.143, 7: 0.161, 8: 0.121, 9: 0.126, 10: 0.092, 11: 0.046, 12: 0.042}
Друк значень та їхніх ймовірностей при 10000 експериментах:  {2: 0.0287, 3: 0.0544, 4: 0.0842, 5: 0.1119, 6: 0.1393, 7: 0.1646, 8: 0.14, 9: 0.1094, 10: 0.0865, 11: 0.0549, 12: 0.0261}
Друк значень та їхніх ймовірностей при 100000 експериментах: {2: 0.02753, 3: 0.05647, 4: 0.0828, 5: 0.11251, 6: 0.13818, 7: 0.16775, 8: 0.13959, 9: 0.1103, 10: 0.08278, 11: 0.05484, 12: 0.02725}


Аналітичні розрахунки для порівняння точності розрахунків (Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином)

Сума   Ймовірність
2      2.78  % (1/36)
3      5.56  % (2/36)
4      8.33  % (3/36)
5      11.11 % (4/36)
6      13.89 % (5/36)
7      16.67 % (6/36)
8      13.89 % (5/36)
9      11.11 % (4/36)
10     8.33  % (3/36)
11     5.56  % (2/36)
12     2.78  % (1/36)
'''