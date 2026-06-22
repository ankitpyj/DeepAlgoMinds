class Solution(object):
    def calPoints(self, operations):
        record = []
        # num
        for i in operations:

            if i == "+":
                num = record[-1] + record[-2]
                record.append(num)
               

            elif i == "C":
                record.pop()


            elif i == "D":
                num = 2 * record[-1]
                record.append(num)


            else:  # 
                
                record.append(int(i))

        return sum(record)


        #C

        #D = prev *2

        #+ = prev +