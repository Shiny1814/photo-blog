from flask import Flask, request, render_template, redirect
from os import listdir, path
from math import ceil

app = Flask(__name__)

def getImages(inView):                 
    imageList = []
    staticDir = listdir(f"{path.dirname(path.abspath(__file__))}/static/")
    for fileName in staticDir:
            imageList.append(fileName)
    imageList.sort(reverse=True)

    imageListList = []
    for i in range(ceil(len(imageList)/inView)):
        indexFrom = i * inView
        indexTo = (i+1) * inView
        imageListList.append(imageList[indexFrom:indexTo])

    return imageListList

@app.route("/")
def mainPage():
    return redirect("/1")


@app.route("/<index>")
def getPage(index):
    images = getImages(12)

    try:
        index = int(index) - 1
        images[index]
    except Exception as e:
        return str(e)

    return render_template("main_page.html",
                        photos=images[index],
                        pages=len(images),
                        currentIndex=index+1)


@app.route("/image/<img>")
def getImage(img):
    return app.send_static_file(img)


if __name__ == "__main__":
    app.run(debug=True)
