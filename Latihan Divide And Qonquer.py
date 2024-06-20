def merge_sort(arr):
    # jika array memiliki 1 atau tidak ada elemen, array sudah terurut
    if len(arr) <= 1:
        return arr

    # (Divide) Membagi array menjadi dua bagian
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # (Conquer) Mengurutkan kedua bagian secara rekursif
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # (Combine) Merge kedua bagian yang sudah terurut
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge 2 array yang sudah terurut menjadi satu array terurut
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # append elemen yang tersisa dari array kiri dan kanan
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

if __name__ == "__main__":
    arr = [1, 3, 5, 4, 6, 9, 2, 7, 10, 8]
    sorted_array = merge_sort(arr)
    print("Mengurutkan arr yang berantakan menjadi :", sorted_array)
