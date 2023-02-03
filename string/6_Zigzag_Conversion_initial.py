class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        O(N) Time and Space
        # Step 1: label
        PAYPALISHIRING
        01232101232101

        # Step 2: Put into respective array
        0:[PIN]
        1:[ALSIG]
        2:[YAHR]
        3:[PI]

        # Step 3: concat the all the table values
        '''
        order_mapping = collections.defaultdict(list)
        counter, opt = 0, '+'
        for i, char in enumerate(s):
            # flip the sign
            # 3 == 3
            if counter == numRows -1:
                opt = '-'
            elif counter == 0:
                opt = '+'
            order_mapping[counter].append(char)
            if opt == '+':
                counter += 1
            else:
                counter -= 1
        res = ''
        for i, values in order_mapping.items():
            res += ''.join(values)
        return res