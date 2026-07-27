class Solution:

    def encode(self, strs: List[str]) -> str:
        string_list=[]
        for word in strs:
            string_list.append(str(len(word)) + "#" + word)
            print(string_list)
        return "".join(string_list)


    def decode(self, s: str) -> List[str]:
        output_list=[]
        i=0
        while i < len(s):
            j=i
            while s[j] !="#":
                j+=1
            code_str=s[i:j]
            length=int(code_str)
            output_list.append(s[i+1+len(code_str):i+1+len(code_str)+length])
            i=i+length+1+len(code_str)
        return output_list


