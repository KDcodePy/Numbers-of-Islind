# Numbers-of-Islind
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


class Solition:
    def Number_of_island(self,grid:[list[list]]) -> int:
        # first initiate your grid rows and columns, row= the amount of list inside the grid, cols = the amount of indices within a single list
        rows = len(grid)
        cols = len(grid[0])
        
        #add counter so we can keep track of how many islands
        counter = 0
        
        # we're going to be using Depth-first-search algorithm to keep searching all the way to the very last "1" connected to each other on every iteration
        # this dfs function will be taking row and col as parameter and will be a recurrsive call
        def dfs(row,col):
            # we need to the search if we're at the edge of the grid so we don't get an IndexError
            if row < 0 or row == rows or col < 0 or col == cols:
                return
                
            # we need to also stop the search of there are no other "1" left around the current location
            if grid[row][col] != "1":
                return
                
            # before we do another recurrsive call we need to change our current location to any value other than "1" so we dont accidentally go back to it.
            grid[row][col] = "x"
            
            # now call your dfs function on all direction left,right,up and down
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            
            
            #now iterate to your grid on all axis
        for row in range(rows):
            for col in range(col):
                #if the value of that element is == "1" run your dfs algorith and update the counter
                if grid[row][col] == "1":
                    dfs(row,col)
                    counter += 1
                    
        #once the loop is complete return the counter
        return counter
