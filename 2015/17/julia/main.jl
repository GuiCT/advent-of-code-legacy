function get_containers()
  open("input.txt", "r") do file
    containers = [parse(Int, line) for line in eachline(file)]
    containers = sort(containers, rev=true)
    return containers
  end
end

containers = get_containers()
amount_of_containers = length(containers)
amount_to_equal = 150

function calculate_sum(containers, combination_string)
  sum = 0
  for (i, container) in enumerate(containers)
    if combination_string[i] == '1'
      sum += container
    end
  end
  return sum
end

combination_value = 2^amount_of_containers - 1
global used_containers_per_valid_combination = Dict()
while combination_value >= 0
  global used_containers_per_valid_combination
  combination_string = string(combination_value, base=2, pad=amount_of_containers)
  sum = calculate_sum(containers, combination_string)
  if sum == amount_to_equal
    used_containers = count(x -> x == '1', combination_string)
    println("Valid combination: ", combination_string, " with ", used_containers, " containers")
    current_value = get(used_containers_per_valid_combination, used_containers, 0)
    used_containers_per_valid_combination[used_containers] = current_value + 1
  end
  combination_value -= 1
end
acceptable_combinations = sum(values(used_containers_per_valid_combination))
println("[Part 1] Acceptable combinations: ", acceptable_combinations)
# Get minimum value in Dict keys
minimum_containers = minimum(collect(keys(used_containers_per_valid_combination)))
println("[Part 2] Minimum containers: ", minimum_containers, " with ", used_containers_per_valid_combination[minimum_containers], " combinations")