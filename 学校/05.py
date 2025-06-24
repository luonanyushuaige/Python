def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return None

if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("排序前的数组:", test_array)
    bubble_sort(test_array)
    print("排序后的数组:", test_array)


    def find_max_and_neighbors(nums):
        if len(nums) < 3:
            raise ValueError("列表中的元素数量必须至少为3")

        # 找到最大值及其索引
        max_value = max(nums)
        max_index = nums.index(max_value)

        # 确定相邻元素
        neighbors = []
        if max_index > 0:
            neighbors.append(nums[max_index - 1])
        if max_index < len(nums) - 1:
            neighbors.append(nums[max_index + 1])

        return max_value, neighbors


    def main():
        # 从键盘输入整数，直到用户停止输入（例如通过输入非数字或空行）
        nums = []
        print("请输入至少3个整数，每输入一个整数后按回车，完成后按Ctrl+D（EOF）结束输入：")
        try:
            while True:
                num = int(input())
                nums.append(num)
                if len(nums) >= 3:  # 一旦有3个或更多元素，可以开始处理（但用户可能还想继续输入）
                    break  # 这里也可以不break，让用户输入所有数后再处理
        except EOFError:
            pass  # 用户通过Ctrl+D结束输入

        if len(nums) < 3:
            print("输入的整数数量不足3个，请重新运行程序并输入至少3个整数。")
        else:
            max_value, neighbors = find_max_and_neighbors(nums)
            print(f"最大值是 {max_value}，其相邻元素是 {neighbors}")


    if __name__ == "__main__":
        main()