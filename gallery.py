from os import walk

_, _, filenames = next(walk('img'))

print(filenames)

html = """
<html>
<head>
<title>Hello Python</title>
<style>
img {
width: 350px;
height: 125px
object-fit: cover;
}
</style>
</head>
<body>
"""

for f in filenames:
    html+= '<img src="img/' + f + '">'

html += """
<h1>Bildergalerie</h1>

</body>
</html>
"""

print(html)

# Write HTML String to file.html
with open("index.html", "w") as file:
    file.write(html)
