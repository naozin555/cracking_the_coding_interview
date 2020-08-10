class Box:
    def __init__(self, wi, hi, di):
        self.wi = wi
        self.hi = hi
        self.di = di


def solve(boxes):
    boxes_list = []
    for i, box in enumerate(boxes):
        if i == 0:
            box1_wi = box.wi
            box1_hi = box.hi
            box1_di = box.di
        if i > 0:
            box2_wi = box1_wi
            box2_hi = box1_hi
            box2_di = box1_di
            box1_wi = box.wi
            box1_hi = box.hi
            box1_di = box.di
            if box2_wi > box1_wi and box2_hi > box1_hi and box2_di > box1_di:
                larger_box = Box(box2_wi, box2_hi, box2_di)
                smaller_box = Box(box1_wi, box1_hi, box1_di)
                boxes_list.append(larger_box)
                boxes_list.append(smaller_box)
                return boxes_list
            elif box2_wi < box1_wi and box2_hi < box1_hi and box2_di < box1_di:
                smaller_box = Box(box2_wi, box2_hi, box2_di)
                larger_box = Box(box1_wi, box1_hi, box1_di)
                boxes_list.append(larger_box)
                boxes_list.append(smaller_box)
                return boxes_list
            else:
                pass
                # 同じ大きさの箱の時、どういう処理すべきかよく分からない。

