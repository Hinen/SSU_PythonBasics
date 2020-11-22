def print_baggage_items(*items, **item_with_count):
    print("# 단일 품목")
    if len(items) == 0:
        print("존재하지 않습니다.")
    else:
        for item in items:
            print(item)

    print("\n# 다중 품목")
    if len(item_with_count) == 0:
        print("존재하지 않습니다.")
    else:
        for key in item_with_count.keys():
            print("%s %d 개" % (key, item_with_count[key]))

print_baggage_items('laptop', 'camera', 'charger', socks = 8, patns = 2, shirts = 4)