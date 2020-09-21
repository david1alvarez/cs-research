array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, "done!", 1]

# array.each {|variable| puts variable}
# array.each_with_index {|variable, index| puts "#{variable} => #{index}"}

is_repeat = {}
ret_array = []
array.each do |item| # recommended syntax for multiline operations
    if is_repeat.has_key?(item)
        puts "#{item} is a repeat"
        next
    end
    ret_array.append(item)
    is_repeat[item] = true
end
# puts(ret_array)


# filter array with .select
print [1,2,3,4,5].select {|num| num.even? }   #=> [2, 4]
print "\n"

a = %w[ a b c d e f ] # %w[array] converts an array like [val1 val2 val3 val4] to ["val1", "val2", "val3", "val4"]
puts a.select {|v| v =~ /[aeiou]/ }    #=> ["a", "e"]