def rotate(matrix)
  rotated = matrix.transpose
  reversed = rotated.map { |row| row.reverse }
  reversed.each_with_index do |row, i|
    matrix[i] = row
  end
end
