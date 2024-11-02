# NUMBER OF APPROACHES: TWO 

# THIS PROBLEM ASSUMES THERE ARE ONLY ALPHA CHARS IN STRING

# TC: O(n), SC: O(n)
############################################################################
'''
Algorithm explanation

We take the string, check the two extreme ends of it for match.
Now, we take the inside subarray (excluding the ends we just matched),
and perform same operation again.
We keep doing this until the two extreme ends cross (or equal) each other,
i.e. in the middle. 

Now as we are doing the same operations but on smaller version => recursion.

Visualise in complexity explanation
'''
def rec_reverse_array(array, left_pointer, right_pointer):
    if(left_pointer >= right_pointer):
        return True
    if (array[right_pointer] != array[left_pointer]):
        return False
    return rec_reverse_array(array, left_pointer + 1, right_pointer - 1)

def optimal_rec():
    array = input("")
    ans = rec_reverse_array(array, 0, len(array) - 1)
    print(ans)
optimal_rec()
############################################################################
'''
Complexity explanation

Since we are calling a function n times- TC: O(n)

We are moving our two extreme ends inwards until they cross, that would mean,
it takes n/2 fn calls to reverse the whole array.
Since we are calling a function n times (well we know n/2 but for asymptotic purposes, its n)
- TC: O(n)

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
check the two extreme ends of it for match.
Now, we take the inside subarray (excluding the ends we just matched), so we move the
pointers to insdie by 1 and perform same operation again.
We keep doing this until the two pointers cross (or equal) each other,
i.e. in the middle. 
'''