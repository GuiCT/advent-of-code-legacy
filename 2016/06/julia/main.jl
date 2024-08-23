import StatsBase: mode
import DataStructures: counter

function read_file()
  open("input.txt") do file
    lines = readlines(file)
    n_rows = length(lines)
    n_cols = length(lines[1])
    matrix = fill(' ', n_rows, n_cols)
    for i in 1:n_rows
      for j in 1:n_cols
        matrix[i, j] = lines[i][j]
      end
    end

    return matrix
  end
end

matrix = read_file()
chars = [mode(col) for col in eachcol(matrix)]
res_part1 = join(chars, "")
println(res_part1)

function get_least_common(column::AbstractVector{Char})
  c = counter(column)
  return first(sort(collect(c), by=x->x[2]))
end

chars_part2 = [get_least_common(col)[1] for col in eachcol(matrix)]
res_part2 = join(chars_part2, "")
println(res_part2)