function load_matrix()
  open("input.txt", "r") do f
    parseInt = s -> parse(Int, String(s))
    lines = readlines(f)
    n_lines = length(lines)
    n_columns = 3
    matrix = zeros(Int, n_lines, n_columns)
    for (i, line) in enumerate(lines)
      line_stripped = strip(line)
      line_simplified = replace(line_stripped, r"\s+" => " ")
      values_as_string = split(line_simplified)
      values = map(parseInt, values_as_string)
      matrix[i, :] = values
    end

    return matrix
  end
end

matrix = load_matrix()
possible_triangles = 0
for row in eachrow(matrix)
  sorted_row = sort(row)
  if sorted_row[1] + sorted_row[2] > sorted_row[3]
    global possible_triangles += 1
  end
end

@info "Part 1 answer is" possible_triangles

n_elements = length(matrix)
n_triangles = n_elements ÷ 3
reordered_matrix = transpose(reshape(matrix, (3, n_triangles)))
possible_triangles = 0
for row in eachrow(reordered_matrix)
  sorted_row = sort(row)
  if sorted_row[1] + sorted_row[2] > sorted_row[3]
    global possible_triangles += 1
  end
end

@info "Part 2 answer is" possible_triangles
