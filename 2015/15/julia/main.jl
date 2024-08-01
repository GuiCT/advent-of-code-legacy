import Base.ImmutableDict
import LinearAlgebra.dot

# Open file input.txt and read ingredient line by line
f = open("input.txt", "r")
lines = readlines(f)
println(lines)

function parse_string(s)
  return String((split(strip(s)))[2])
end


function parseLine(line)
  ingredient, first_tail = split(line, ":")
  capacity, durability, flavor, texture, calories = map(x -> parse(Int, String(split(x, " ")[3])), split(first_tail, ","))
  return ImmutableDict(
    "capacity" => capacity,
    "durability" => durability,
    "flavor" => flavor,
    "texture" => texture,
    "calories" => calories
  )
end

ingredients = []
for line in lines
  push!(ingredients, parseLine(line))
end

amount_of_ingredients = size(ingredients)[1]
# All possible combinations of n numbers (n being the amount_of_ingredients) that sums up to 100
max_value = 0
SECOND_PART = true
for i1 ∈ 0:100
  for i2 ∈ 0:100
    for i3 ∈ 0:100
      for i4 ∈ 0:100
        if (i1 + i2 + i3 + i4) != 100
          continue
        end
        calorie_sum = dot(
          [ingredient["calories"] for ingredient in ingredients],
          [i1, i2, i3, i4]
        )
        if SECOND_PART && calorie_sum != 500
          continue
        end
        capacity_sum = dot(
          [ingredient["capacity"] for ingredient in ingredients],
          [i1, i2, i3, i4]
        )
        durability_sum = dot(
          [ingredient["durability"] for ingredient in ingredients],
          [i1, i2, i3, i4]
        )
        flavor_sum = dot(
          [ingredient["flavor"] for ingredient in ingredients],
          [i1, i2, i3, i4]
        )
        texture_sum = dot(
          [ingredient["texture"] for ingredient in ingredients],
          [i1, i2, i3, i4]
        )
        has_negative = minimum([capacity_sum, durability_sum, flavor_sum, texture_sum]) < 0
        product = if has_negative
          0
        else
          capacity_sum * durability_sum * flavor_sum * texture_sum
        end
        if product > max_value
          max_value = product
        end    
      end
    end
  end
end

println("Maximized! ", max_value)
