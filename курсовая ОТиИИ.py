import heapq
from collections import Counter

class Node:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.left = None
        self.right = None



def build_huffman_tree(text):
    my_set=set()
    
    for i in text:
        my_set.add(i)
    nodes=[Node(symbol) for symbol in my_set]
    while len(nodes) > 1:
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        parent = Node(left_node.symbol + right_node.symbol)
        parent.left = left_node
        parent.right = right_node
        nodes.append(parent)
    return nodes[0]


while True:
    text = input("Введите текст")

    # Создаем словарь symbol_frequency для данного текста
   

    # Строим дерево Хаффмана
    root = build_huffman_tree(text)

    # Создаем словарь символов и их кодов
    symbol_codes = {}
    def build_codes(node, code):
        if node is None:
            return
        if node.symbol is not None:
            symbol_codes[node.symbol] = code
            return
        build_codes(node.left, code+'0')
        build_codes(node.right, code+'1')
    build_codes(root, '')

    while True:
        print("Выберите опцию:")
        print("1. Закодировать текст в файле")
        print("2. Декадировать текст в файле")
        print("3. Удалить текст в файле")
        print("4. Выйти")

        choice = input("Введите номер опции: ")

        if choice == "1":
            # Выводим словарь символов и их кодов
            print('Symbol codes:', symbol_codes)
           
            for i in range (text.len()+1):
                encoded_text = ''.join(symbol_codes[i] for i in text)

            # Записываем закодированный текст в файл
            print(encoded_text)

        elif choice == "2":
            # Декодируем закодированный текст
            encoded_text= input("Введите закодированный текст этого дерева")
            
            decoded_text = ""
            current_node = root

            # Декодируем закодированный текст в исходный текст с помощью дерева Хаффмана
            for bit in encoded_text:
                if bit == '0':
                    current_node = current_node.left
                else:
                    current_node = current_node.right

                if current_node.symbol is not None:
                    decoded_text += current_node.symbol
                    current_node = root

            # Записываем декодированный текст в файл
            print (decoded_text)
      
        elif choice == "4":
        # Выход из программы
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите опцию снова.")

    if choice == "4":
        break
