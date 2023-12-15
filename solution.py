import re

class Solution:
    
    def day_one(self):
        try:
            with open('input.txt', 'r') as file:
                int_list = [int(re.sub(r'[a-zA-Z]', '', line.strip())) for line in file]
            filtered_numbers = [num for num in int_list if num < 10]
            duplicate = [int(f"{x}{y}") for x, y in zip(filtered_numbers, filtered_numbers)]
            
            processed_numbers = []
            for num in int_list:
                if num >= 10:
                    num_str = str(num)
                    new_num = int(num_str[0] + num_str[-1]) if len(num_str) > 2 else num
                    processed_numbers.append(new_num)

            result = sum(processed_numbers) + sum(duplicate)
            print(result)
        except FileNotFoundError:
            print("File not found.")
        except ValueError:
            print("Invalid data in file.")

sol = Solution()
sol.day_one()
