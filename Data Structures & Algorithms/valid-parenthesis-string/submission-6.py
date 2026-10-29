class Solution:
    def checkValidString(self, s: str) -> bool:
        open, close, wild = 0, 0, 0
        for c in s:
            if c == '(': open += 1
            elif c == ')': close += 1
            else: wild += 1
        
        # decide wild to open
        def add_open() -> int:
            if open < close:
                gap = close - open
                if wild <= gap: return wild
                else: return gap + (wild - gap)//2
            else:
                gap = open - close
                if wild <= gap: return 0
                else: return (wild - gap)//2

        wildToOpen = add_open()

        stack = []
        for c in s: 
            if c == '(': stack.append(c)
            elif c == ')': 
                if stack and stack[-1] == '(': stack.pop()
                else: return False
            else: # c is *
                if wildToOpen > 0:
                    stack.append('(')
                    wildToOpen -= 1
                    open += 1
                    continue

                if open == close or not stack: 
                    continue
                elif stack[-1] == '(': 
                    stack.pop()
                    close += 1
                else: return False   
                
        return not stack
"""
incremental steps
logic 
test 
refactor
"""