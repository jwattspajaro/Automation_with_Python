Dictionaries Defined
Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections. However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples.

When creating a dictionary, you use curly brackets: {}. When storing values in a dictionary, the key is specified first, followed by the corresponding value, separated by a colon. For example, animals = { "bears":10, "lions":1, "tigers":2 } creates a dictionary with three key value pairs, stored in the variable animals. The key "bears" points to the integer value 10, while the key "lions" points to the integer value 1, and "tigers" points to the integer 2. You can access the values by referencing the key, like this: animals["bears"]. This would return the integer 10, since that’s the corresponding value for this key.

You can also check if a key is contained in a dictionary using the in keyword. Just like other uses of this keyword, it will return True if the key is found in the dictionary; otherwise it will return False.

Dictionaries are mutable, meaning they can be modified by adding, removing, and replacing elements in a dictionary, similar to lists. You can add a new key value pair to a dictionary by assigning a value to the key, like this: animals["zebras"] = 2. This creates the new key in the animal dictionary called zebras, and stores the value 2. You can modify the value of an existing key by doing the same thing. So animals["bears"] = 11 would change the value stored in the bears key from 10 to 11. Lastly, you can remove elements from a dictionary by using the del keyword. By doing del animals["lions"] you would remove the key value pair from the animals dictionary.

----
Diccionarios definidos Los diccionarios son otra estructura de datos en Python. Son similares a una lista en el sentido de que se pueden usar para organizar datos en colecciones. Sin embargo, no se accede a los datos de un diccionario en función de su posición. Los datos en un diccionario están organizados en pares de claves y valores. Utiliza la tecla para acceder al valor correspondiente. Donde un índice de lista es siempre un número, una clave de diccionario puede ser un tipo de datos diferente, como una cadena, un número entero, un flotante o incluso tuplas.

Al crear un diccionario, utiliza corchetes: {}. Al almacenar valores en un diccionario, primero se especifica la clave, seguida del valor correspondiente, separados por dos puntos. Por ejemplo, animales = { "osos":10, "leones":1, "tigres":2 } crea un diccionario con tres pares de valores clave, almacenados en la variable animales. La clave "osos" apunta al valor entero 10, mientras que la clave "leones" apunta al valor entero 1 y "tigres" apunta al número entero 2. Puede acceder a los valores haciendo referencia a la clave, así: animales[ "osos"]. Esto devolvería el número entero 10, ya que ese es el valor correspondiente para esta clave.

También puede verificar si una clave está contenida en un diccionario usando la palabra clave in. Al igual que otros usos de esta palabra clave, devolverá True si la clave se encuentra en el diccionario; de lo contrario, devolverá False.

Los diccionarios son mutables, lo que significa que se pueden modificar agregando, eliminando y reemplazando elementos en un diccionario, de forma similar a las listas. Puede agregar un nuevo par de valores clave a un diccionario asignando un valor a la clave, así: animales["cebras"] = 2. Esto crea la nueva clave en el diccionario de animales llamado cebras y almacena el valor 2. puede modificar el valor de una clave existente haciendo lo mismo. Entonces animales["osos"] = 11 cambiaría el valor almacenado en la clave de osos de 10 a 11. Por último, puede eliminar elementos de un diccionario usando la palabra clave del. Al hacer del animals["lions"], eliminaría el par de valores clave del diccionario de animales.diccionario.valores().