n = ['Test Dummy', 'Jack Flanigan', 'Alexandra Wierzbiak', 'Leslie Acevedo', 'Faith Foster',
    'Harsha Nambri', 'Wan Ruan', 'Eric Xue', 'Prakashini Govindasamy',
    'Adam Armstead', 'Thomas Janas', 'Adamaris Nunez', 'Subhi Chandrasekaran',
    'David Lasota', 'Felicia Tan', 'Jeremy Starzec', 'Rishabh Sanghavi',
    'Izabella Lach']
n = ['Test Dummy', 'Zain Usman', 'Yikun Lee', 'Jeff Galiotto', 'Megan Ray', 
    'Alexis Waite', 'Rahil Barar', 'Berkelee Asare', 'Sofia Takki', 'Allen Partin', 
    'Dominika Piczura', 'Amogh Bhoopalam', 'Bethany Shiang', 'Katie Huynh', 
    'Yuna Lee', 'Erisa Farimani', 'Morgan Bentel', 'Zoe Nelson', 
    'Sana Khadilkar', 'Liam Herrebout']

'''
<tr>
    <td>Ali Hasan</td>
    <td id="a0"> - </td>
    <td id="a1"> - </td>
    <td id="a2"> - </td>
    <td id="a3"> - </td>
    <td id="a4"> - </td>
    <td id="a5"> - </td>
    <td id="a6"> - </td>
    <td id="a7"> - </td>
    <td id="a8"> - </td>
    <td id="a9"> - </td>
</tr>
'''

with open('index_html.txt', 'w+') as f:
    for i,name in enumerate(n,ord('a')):
        f.write('<tr>\n')
        f.write('    <td>{}</td>\n'.format(name))
        for ct in range(10):
            f.write('    <td style="text-align:center" id="{}"></td>\n'.format("_".join(name.split())+"_"+str(ct)))
        f.write('</tr>\n')
