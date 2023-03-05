def camel_case(s):
#     split the string into separate words
    split_string_list = s.split()
    camelCasedWord = ""
    camelCasedWord += split_string_list[0]
# cycle through the string, capitalising the first letter of 2nd word onwards
    camelCasedWord += "".join([split_string_list[i][0].upper() + split_string_list[i][1:] for i in range(1, (len(split_string_list)))])
    
#     for i in range(1, (len(split_string_list))):
#         capitalised = split_string_list[i][0].upper() + split_string_list[i][1:]
#         camelCasedWord += capitalised
# # join the words together
# return camelCased word
    return camelCasedWord
    
    
print(camel_case("test case"))
print(camel_case("camel case method"))

# @test.describe("Basic Tests")
# def basic_tests():
    
#     @test.it("Basic Tests")
#     def basic_tests():
#         test.assert_equals(camel_case("test case"), "TestCase")
#         test.assert_equals(camel_case("camel case method"), "CamelCaseMethod") 
    