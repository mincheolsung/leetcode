class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }

        i = 1
        result = []
        while num > 0:
            digit = num%10
            temp = ""
            while digit > 0:
                if digit == 9:
                    temp += roman[9*i]
                    digit -= 9

                elif digit >= 5:
                    temp += roman[5*i]
                    digit -= 5

                elif digit >= 4:
                    temp += roman[4*i]
                    digit -= 4

                else:
                    temp += roman[1*i]
                    digit -= 1

            num /= 10
            i *= 10
            result.insert(0, temp)
            
        return "".join(result)