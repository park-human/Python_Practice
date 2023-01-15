#!C:\\Python3.11.1\\python.exe
print("content-type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageId = form.getvalue('id')

print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OtakuWorld</title>
</head>
<body>
    <h1><a href="index.py?id=Monster Trio">Monster Trio</a></h1>
    <ol>
        <li><a href="index.py?id=Monkey D. Luffy">Monkey D. Luffy</a></li>
        <li><a href="index.py?id=Roronoa Zoro">Roronoa Zoro</a></li>
        <li><a href="index.py?id=Sanji">Sanji</a></li>
    </ol>
    <image src="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2021/07/Featured-One-Piece-Better-Manga.jpg?q=50&fit=crop&w=1500&dpr=1.5" alt="" width="800"></image>
    <h2>{title}</h2>
    <div style="text-indent:15px">
    <p><b>The Monster Trio</b> refers to the team of the three strongest fighters of the Straw Hat Pirates and includes Luffy and his two wings, Zoro and Sanji. Out of all the members of the crew, they're by far the strongest which is why they handle the most dangerous situations that the crew faces on the high seas on their own. Surprisingly, there exists a myth among One Piece fans that the Monster Trio is a fan-made name and, thus, isn't official. This couldn't be further from the truth. The Monster Trio is a term that Eiichiro Oda himself came up with. The first time the term "Monster Trio" was used was in the Thriller Bark arc, when Nami was hiding inside Kumacy's body, upset about the fact that the Monster Trio was taken down.</div>

    <div style="text-indent:15px">
    Later, on the way to Fishman Island, Oda once again made sure to use the term "Monster Trio" for Luffy, Zoro, and Sanji through Caribou when the three decided to face Tsurume, the Kraken. As such, the idea that the Monster Trio doesn't exist is simply incorrect, and this dynamic very much exists in the Straw Hat Pirates. </div> </p>

</body>
</html>)
'''.format(title=pageId))