


"""
    :param array: Array with integer values.
    :returns index: The index of the position where the lower value of the array are saved. If array is empty, value will be -1.
    :returns value: The lower value saved in the array. If array is empty, value will be -1
"""
def selectLowerValue(array):

    index=-1
    value=-1

    if len(array)>0:
        index=0
        value=array[0]
        for i in range(1, len(array)):
            if array[i]<value:
                value=array[i]
                index=i
    return index, value