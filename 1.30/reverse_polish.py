class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        operators = ["+", "-", "*", "/"]
        def perform_operations(current_index, list):
            if len(list)==1:
                return int(list[0])
            
            elif list[current_index] in operators:
                if list[current_index] == "/":
                    result = int(int(list[current_index-2])/int(list[current_index-1]))
                else:
                    result = eval(f"{int(list[current_index-2])} {list[current_index]} {int(list[current_index-1])}")
                list[current_index-2:current_index+1] = [str(result)]
                return perform_operations(current_index-2,list)
            
            else:
                return perform_operations(current_index+1, list)

        result = perform_operations(0, tokens)
        return result

            
