using MD5

global tried_value = Int64(0)
global found_five = Int64(-1)
global found_six = Int64(-1)
hash_prefix = read("../input.txt", String)
hash_prefix = replace(hash_prefix, "\n" => "")
while true
    global tried_value, found_five, found_six
    hash_full = hash_prefix * string(tried_value)
    hash_value = bytes2hex(md5(hash_full))
    if found_five == -1
        if startswith(hash_value, "00000")
            found_five = tried_value
        end
    end
    if found_six == -1
        if startswith(hash_value, "000000")
            found_six = tried_value
        end
    end
    if found_five != -1 && found_six != -1
        break
    end
    global tried_value
    tried_value += 1
end
println("First with 5 zeros is " * string(found_five))
println("First with 6 zeros is " * string(found_six))
