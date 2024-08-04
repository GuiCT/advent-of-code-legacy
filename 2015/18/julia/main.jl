PART_2 = true

function read_light_matrix()
  open("input.txt") do file
    lines = readlines(file)
    num_rows = length(lines)
    num_cols = length(lines[1])
    light_matrix = zeros(Bool, num_rows, num_cols)
    for (i, line) in enumerate(lines)
      for (j, char) in enumerate(line)
        light_matrix[i, j] = char == '#'
      end
    end

    if PART_2
      light_matrix[1, 1] = true
      light_matrix[1, num_cols] = true
      light_matrix[num_rows, 1] = true
      light_matrix[num_rows, num_cols] = true
    end

    return light_matrix
  end
end

function get_neighbor_count(matrix::Matrix{Bool}, i::Int, j::Int)
  row_count, col_count = size(matrix)
  neighbor_count = 0
  for Δi ∈ -1:1
    for Δy ∈ -1:1
      if Δi == 0 && Δy == 0
        continue
      end
      curr_i = i + Δi
      curr_j = j + Δy
      i_valid = curr_i >= 1 && curr_i <= row_count
      j_valid = curr_j >= 1 && curr_j <= col_count
      pos_valid = i_valid && j_valid
      if pos_valid
        neighbor_count += matrix[curr_i, curr_j]
      end
    end
  end
  return neighbor_count
end

function iterate_lights(current_light_matrix::Matrix{Bool})
  row_count, col_count = size(current_light_matrix)
  new_light_matrix = copy(current_light_matrix) 
  for i ∈ 1:row_count
    for j ∈ 1:col_count
      neighbor_count = get_neighbor_count(current_light_matrix, i, j)
      is_lit = current_light_matrix[i, j]      
      if is_lit
        new_light_matrix[i, j] = neighbor_count == 2 || neighbor_count == 3
      else
        new_light_matrix[i, j] = neighbor_count == 3
      end
    end
  end

  if PART_2
    new_light_matrix[1, 1] = true
    new_light_matrix[1, col_count] = true
    new_light_matrix[row_count, 1] = true
    new_light_matrix[row_count, col_count] = true
  end

  return new_light_matrix
end

light_matrix = read_light_matrix()
for _ ∈ 1:100
  light_matrix = iterate_lights(light_matrix)
end
println(sum(light_matrix))