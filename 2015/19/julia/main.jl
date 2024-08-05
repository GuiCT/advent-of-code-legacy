PRODUCTION_REGEX = r"([a-zA-Z]+) => ([a-zA-Z]+)"

function read_file()
  open("input.txt", "r") do file
    lines = readlines(file)
    productions = Array{Tuple{String, String}}(undef, 0)
    for curr_line ∈ 1:length(lines) - 2
      found_match = match(PRODUCTION_REGEX, lines[curr_line])
      new_production = map(String, (found_match.captures[1], found_match.captures[2]))
      push!(productions, new_production)
    end
    return productions, lines[end]
  end
end

productions, molecule = read_file()
set_of_possibles = Set{String}()

for (base, target) ∈ productions
  base_length = length(base)
  for k_letter ∈ eachindex(molecule)
    do_not_surpass_molecule_length = k_letter + base_length - 1 <= length(molecule)
    if do_not_surpass_molecule_length && molecule[k_letter:k_letter + base_length - 1] == base
      new_molecule = molecule[1:k_letter - 1] * target * molecule[k_letter + base_length:end]
      push!(set_of_possibles, new_molecule)
    end
  end
end
@info "Part 1 answer is" length(set_of_possibles)
