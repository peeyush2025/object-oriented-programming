class Solution:
    def intToRoman(self, num):
        vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ""
        for i, v in enumerate(vals):
            while num >= v:
                res += syms[i]
                num -= v
        return res
s = Solution()
print(s.intToRoman(3549))
