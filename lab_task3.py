print("Vlad Novitskyi 8 variant, K-10")


def _info():
    """function to present general information"""
    print("The program to solve algorithmic problem about packing boxes according to the matryoshka principle."
          "\nYou can place one box in another if the side lengths differ by at least 5 units and these boxes have "
          "\ndifferent colors. It is necessary to find the maximum number of boxes that can be used for packing and "
          "\nwith  for this number, the length of the largest possible side of the initial box."
          "\n*****Enter all the boxes. The size and color of the box are specified by a space.*****"
          "\n*****The condition guarantees that there is at least one box***** ")


def input_data():
    """a function for input and check data"""
    boxes = []
    colors = ["R", "G", "B", "Y"]
    while True:
        box = input()
        if len(box.strip()) == 0:
            break
        size_of_box, color_of_box = box.split()
        if (not size_of_box.isdigit()) or float(size_of_box) <= 0 or color_of_box not in colors:
            raise ValueError
        if len(size_of_box) == 0 or len(color_of_box) == 0 or box.count(' ') > 1:
            raise ValueError

        boxes.append((size_of_box, color_of_box))
    return boxes


def _box_in_box(box1, box2):
    """a function to check if one box can be placed inside another """
    return (float(box1[0]) + 5 <= float(box2[0])) and (box1[1] != box2[1])


def _sorting(x):
    """a function for sorting boxes in order of increasing length of the side of the box"""
    y = sorted(x, key=lambda i: float(i[0]))
    return y


def max_packing(boxes):
    """a function for finding the largest packing and
        the side of the largest initial box"""
    n = len(boxes)
    pack_len = [0] * n

    for i in range(n-1, -1, -1):
        max_pack_local = 0
        for j in range(n):
            if _box_in_box(boxes[i], boxes[j]):
                max_pack_local = max(max_pack_local, pack_len[j])
        pack_len[i] = max_pack_local + 1

    max_pack = max(pack_len)
    start_boxes = [i for i, dist in enumerate(pack_len) if dist == max_pack]
    k = max(start_boxes)

    return max_pack, float(boxes[k][0])


def main():
    """the main function, the function that collects everything"""
    _info()
    try:
        boxes = input_data()
        sorted_boxes = _sorting(boxes)
        result = max_packing(sorted_boxes)
        print("THE WORK IS DONE")
        print(f"Кількість наявних коробок : {len(boxes)}")
        print(f"Найбільша к-сть коробок які можна використати для пакування подарунку : {result[0]}")
        print(f"За {result[0]} коробок максимально можлива довжина найменшої сторони : {result[1]}")

    except ValueError:
        print(f"***** error \nPlease, enter the length(>0)"
              f" and color(R, G, B, Y) of the box through the single space...")


try:
    main()
except KeyboardInterrupt:
    print("\n program aborted")
except EOFError:
    print("invalid format")
