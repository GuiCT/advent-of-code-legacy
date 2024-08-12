# Thx to this guy
# https://github.com/trizen/julia-scripts/blob/master/Math/sigma_function.jl
# and this guy
# https://github.com/trizen/julia-scripts/blob/master/Math/divisors.jl
using Primes
import LinearAlgebra.dot

function divisor_sum(n, x=1)
  if x == 0
    tau = 1
    for (p, e) in factor(n)
      tau *= (e + 1)
    end
    return tau
  end

  sigma = 1
  for (p, e) in factor(n)
    s = 1
    q = p^x
    for j in 1:e
      s += q^j
    end
    sigma *= s
  end

  return sigma
end

# Trizen
# 28 August 2020
# https://github.com/trizen
# Generate all the positive divisors of n.
function divisors(n)
  d = Int64[1]
  for (p, e) in factor(n)
    t = Int64[]
    r = 1
    for i in 1:e
      r *= p
      for u in d
        push!(t, u * r)
      end
    end
    append!(d, t)
  end
  return sort(d)
end

# curr_house_number = 10000 # Starting from a higher value is smart
# curr_upper_bound_given_by_aoc = 900900 # AOC gives tips, so why not use them?
# while curr_house_number < curr_upper_bound_given_by_aoc
#   present_count = divisor_sum(curr_house_number) * 10
#   @info present_count
#   if present_count >= 34000000
#     @info "Part 1 result is" curr_house_number
#     break
#   end
#   global curr_house_number += 1
# end

curr_upper_bound_given_by_aoc = 952920

for house_i ∈ 1:curr_upper_bound_given_by_aoc
  presents = 0
  elf_this_house = divisors(house_i)
  valid_elfs = filter(elf -> elf * 50 >= house_i, elf_this_house)
  presents = sum(valid_elfs) * 11
  if presents >= 34000000
    @info "Part 2 result is" house_i
    break
  end
end