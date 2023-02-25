# Grid challenge
# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

# Check if an array is in alphabetical order - could check if elements are ascending, or just sort the row.
# For columns, need to cycle through and check if all row[i] elements are in order.
grid = ['mpxz', 'abcd', 'wlmf']
def gridChallenge(grid):
    # create a new grid that has the rows sorted
#     s_grid = []
#     # sort all the rows and add to s_grid
#     for row in grid:
#         l_row = list(row)
#         if l_row == sorted(l_row):
#             s_grid.append(l_row)
#         else:
#             s_grid.append(sorted(l_row))
# #   check if the columns are sorted vertically if yes, return YES, if no, return NO:
#
#     for i in range(len(s_grid)):
#         col_list = []
#         for j in range(len(s_grid[0])):
#             col_list.append(s_grid[j][i])
#         if col_list != sorted(col_list):
#             return "NO"
#     return "YES"

# Alternative method:
# check if string is the same as a joined sorted string of the letters:
# create a new grid that has the rows sorted
    s_grid = []
    # sort all the rows and add to s_grid
    for i in range(len(grid)):
        if grid[i] == "".join(sorted(grid[i])):
            s_grid.append(grid[i])
        else:
            s_grid.append("".join(sorted(grid[i])))
#   check if the columns are sorted vertically if yes, return YES, if no, return NO:
    for i in range(len(s_grid[0])):
        basis = ""
        for j in range(len(s_grid)):
            if s_grid[j][i] < basis:
                return "NO"
            else:
                basis = s_grid[j][i]
    return "YES"

gridChallenge(grid)