class Solution {

  int visitedP  = 0b0001;
  int pacificF  = 0b0010;
  int visitedA  = 0b0100;
  int atlanticF = 0b1000;

  public static void main(String[] args) {

    int[][] matrix = {{1,2,2,3,5},
                      {3,2,3,4,4},
                      {2,4,5,3,1},
                      {6,7,1,4,5},
                      {5,1,1,2,4}};

    int[][] matrix2 = {{1,1},
                       {1,1},
                       {1,1}};

    System.out.println(new Solution().pacificAtlantic(matrix2));
  }

  public List<List<Integer>> pacificAtlantic(int[][] matrix) {

    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
      return new ArrayList<>();
    }

    short[][] visit= new short[matrix.length][matrix[0].length];
    for (int row = 0; row < matrix.length; row++) {
      for (int col = 0; col < matrix[0].length; col++) {
        this.vpacific(matrix, row, col, visit);
        this.vatlantic(matrix, row, col, visit);
      }
    }

    List<List<Integer>> toReturn = new ArrayList<List<Integer>>();
    int bothOcean = this.pacificF | this.atlanticF;
    for (int row = 0; row < matrix.length; row++) {
      for (int col = 0; col < matrix[0].length; col++) {
        if ((visit[row][col] & bothOcean) == bothOcean) {
          toReturn.add(Arrays.asList(row, col));
        }
      }
    }

    return toReturn;
  }

  public Boolean vpacific(int[][] matrix, int row, int col, short[][] visit) {

    //out of grid pacific
    if (row < 0 || col < 0) {
      return true;
    }

    //out of grid atlantic
    if (row >= matrix.length || col >= matrix[0].length) {
      return false;
    }

    //already visited
    if (visitedP == (visit[row][col] & visitedP)) {
      return this.pacificF == (visit[row][col] & this.pacificF);
    }

    //marking as visited
    visit[row][col] |= this.visitedP;

    //On the top shore, thus is pacific
    if (row - 1 < 0 && col >= 0 && col < matrix[0].length) {
      visit[row][col] |= this.pacificF;
      return true;
    }

    //Not at the shore, check if we can move to top
    if (matrix[row][col] >= matrix[row - 1][col]
        && vpacific(matrix, row - 1, col, visit)) {
      visit[row][col] |= this.pacificF;
      return true;
    }

    //On the left shore, thus is pacific
    if (col - 1 < 0 && row >= 0 && row < matrix.length) {
      visit[row][col] |= this.pacificF;
      return true;
    }

    //Not at the shore, check if we can move to left
    if (matrix[row][col] >= matrix[row][col - 1]
        && vpacific(matrix, row, col - 1, visit)) {
      visit[row][col] |= this.pacificF;
      return true;
    }

    //Check if we can go down and come back to pacific
    if (row + 1 < matrix.length
        && matrix[row][col] >= matrix[row + 1][col]
        && vpacific(matrix, row + 1, col, visit)) {
      visit[row][col] |= this.pacificF;
      return true;
    }

    //Check if we can go right and come back to pacific
    if (col + 1 < matrix[0].length
        && matrix[row][col] >= matrix[row][col + 1]
        && vpacific(matrix, row, col + 1, visit)) {
      visit[row][col] |= this.pacificF;
      return true;
    }

    return false;
  }

  public Boolean vatlantic(int[][] matrix, int row, int col, short[][] visit) {

    //out of grid atlantic
    if (row >= matrix.length || col >= matrix[0].length) {
      return true;
    }

    //out of grid pacific
    if (row < 0 || col < 0) {
      return false;
    }

    //already visited
    if (visitedA == (visit[row][col] & visitedA)) {
      return this.atlanticF == (visit[row][col] & this.atlanticF);
    }

    //marking as visited
    visit[row][col] |= this.visitedA;

    //On the bottom shore, thus is atlantic
    if (row + 1 >= matrix.length && col >= 0 && col < matrix[0].length) {
      visit[row][col] |= this.atlanticF;
      return true;
    }

    //Not at the shore, check if we can move to bottom
    if (matrix[row][col] >= matrix[row + 1][col]
        && vatlantic(matrix, row + 1, col, visit)) {
      visit[row][col] |= this.atlanticF;
      return true;
    }

    //On the right shore, thus is atlantic
    if (col + 1 >= matrix[0].length && row >= 0 && row < matrix.length) {
      visit[row][col] |= this.atlanticF;
      return true;
    }

    //Not at the shore, check if we can move to right
    if (matrix[row][col] >= matrix[row][col + 1]
        && vatlantic(matrix, row, col + 1, visit)) {
      visit[row][col] |= this.atlanticF;
      return true;
    }

    //Check if we can go up and come back to atlantic
    if (row - 1 >= 0
        && matrix[row][col] >= matrix[row - 1][col]
        && vatlantic(matrix, row - 1, col, visit)) {
      visit[row][col] |= this.atlanticF;
      return true;
    }

    //Check if we can go left and come back to atlantic
    if (col - 1 >= 0
        && matrix[row][col] >= matrix[row][col - 1]
        && vatlantic(matrix, row, col - 1, visit)) {
      visit[row][col] |= this.atlanticF;
      return true;
    }

    return false;
  }
}

