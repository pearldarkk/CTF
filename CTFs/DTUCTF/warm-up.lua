require 'bit'
function check(input)
	local key = "tuanlinh"
	local arr = {61, 38, 40, 58, 40, 61, 59, 19, 30, 0, 18, 26, 51, 8, 49, 10, 27, 7, 8, 0, 11, 54, 25, 9, 6, 24, 76, 27, 28, 54, 13, 0, 21, 25, 13, 11, 2, 14, 11, 55, 19, 26, 14, 10, 51, 5, 27, 11, 31, 42, 9, 15, 26, 12, 49, 14, 1, 27, 28}
	if table.getn(arr) ~= input:len() then
		return false
	end

	j = 1
	for i = 1, input:len(), 1 do
		if j == key:len() + 1 then
			j = 1
		end

		if bit.bxor(string.byte(string.sub(input, i, i)),string.byte(string.sub(key, j, j))) ~= arr[i] then
			return false
		end
		j = j + 1
	end

	return true
end

local input = io.read()
if check(input) then
	print("Congrats!\n")
else
	print("Nope!\n")
end