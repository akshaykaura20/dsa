# NUMBER OF APPROACHES: TWO (Same complexity)

# TC: O(n), SC: O(n)
############################################################################
'''
Algorithm explanation

We take the array, reverse(swap) the two extreme ends of it.
Now, we take the inside subarray (excluding the ends we just swapped),
and perform same operation again.
We keep doing this until the two extreme ends cross (or equal) each other,
i.e. in the middle. 
This will modify the original data directly.

Now as we are doing the same operations but on smaller version => recursion.

Visualise in complexity explanation
'''
def rec_reverse_array(array, left_pointer, right_pointer):
    if(left_pointer >= right_pointer):
        return
    tmp_element = array[left_pointer]
    array[left_pointer] = array[right_pointer]
    array[right_pointer] = tmp_element
    return rec_reverse_array(array, left_pointer + 1, right_pointer - 1)

def optimal_rec():
    n = int(input(""))
    array = list(map(int, input("").split(" ")))
    rec_reverse_array(array, 0, n - 1)
    print(array)
optimal_rec()
############################################################################
'''
Complexity explanation

We are moving our two extreme ends inwards until they cross, that would mean,
it takes n/2 fn calls to reverse the whole array.
Since we are calling a function n times (well we know n/2 but for asymptotic purposes, its n)
- TC: O(n)
Also the max depth of call stack is n/2 => SC: O(n)

Visualize call stack for n = 5

                          fn(2, 2) -> return
            fn(1, 3)      fn(1, 3)
fn(0, 4)    fn(0, 4)      fn(0, 4)

'''

# APPROACH #2: ITERATIVE
# TC: O(n), SC: O(1)
############################################################################
'''
Algorithm explanation

We take the array, use two pointers (vars) on extreme ends of the array,
reverse(swap) the two extreme ends of it.
Now, we take the inside subarray (excluding the ends we just swapped), so we move the
pointers to insdie by 1 and perform same operation again.
We keep doing this until the two pointers cross (or equal) each other,
i.e. in the middle. 
This will modify the original data directly.
'''
