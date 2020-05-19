# SOLID PRINCIPLES
## LETTER 'D' - Dependency Inversion Principle

«Классы верхних уровней не должны зависеть от классов нижних уровней. 
Оба должны зависеть от абстракций. Абстракции не должны зависеть от 
деталей. Детали должны зависеть от абстракций»

Принцип инверсии зависимостей предлагает изменить направление, в 
котором происходит проектирование.
1. Для начала вам нужно описать интерфейс низкоуровневых операций, 
которые нужны классу бизнес-логики.
2. Это позволит вам убрать зависимость класса бизнес-логики от 
конкретного низкоуровневого класса, заменив её «мягкой» зависимостью 
от интерфейса.
3. Низкоуровневый класс, в свою очередь, станет зависимый от интерфейса, 
определённого бизнес-логикой.

D - Детали зависят от абстракций, абстракции не должны зависеть от деталей

Страница 49 / GoF book
