input1="went for a run"
input2="go for a run"
tuple_size = 3
=begin
input1.each.with_index do |element, index|
  words = input1[index..index+2]
  break if words.length < tuple_size

  puts words.to_s
end
=end

def convert_to_tuples(string, tuple_size)
  words = string.split(" ")
  tuples = []

  (0..words.length-1).each do |index|
    index_range = index + tuple_size - 1
    tuple = words[index..index_range]

    break if tuple.length < tuple_size

    tuples << tuple.to_s
  end

  tuples
end

puts convert_to_tuples(input1, tuple_size)
puts convert_to_tuples(input2, tuple_size)


