require 'set'

def set_zeroes(matrix)
  rowIndexes = Set[]
  colIndexes = Set[]


  matrix.each_with_index do |row, i|
    row.each_with_index do |el, j|
      matrix[i].map! { |el| el = 0} if el == 0
      # rowIndexes.add(i) and colIndexes.add(j) if el == 0
    end
  end

  p matrix
  p matrix.transpose

  matrix.each_with_index do |row, i|
    row.each_with_index do |el, j|
      matrix[i][j] = 0 if rowIndexes.include?(i) || colIndexes.include?(j)
    end
  end

end

set_zeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
