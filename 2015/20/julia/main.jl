# Thx to this guy
# https://github.com/trizen/julia-scripts/blob/master/Math/sigma_function.jl
using Primes

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

curr_house_number = 10000 # Starting from a higher value is smart
curr_upper_bound_given_by_aoc = 900900 # AOC gives tips, so why not use them?
while curr_house_number < curr_upper_bound_given_by_aoc
  present_count = divisor_sum(curr_house_number) * 10
  @info present_count
  if present_count >= 34000000
    @info "Part 1 result is" curr_house_number
    break
  end
  global curr_house_number += 1
end
# Don't know how to do part 2 yet.