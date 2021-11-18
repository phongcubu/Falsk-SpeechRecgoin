from flask import Flask, render_template, request, redirect
import speech_recognition as sr
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    text = ""
    if request.method == "POST":
        print("Data đã nhận !")
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()  # ghi lai
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(data, key=None, language='vi-VN')
                print(text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


    return render_template("index.html", text=text)

if __name__ =="__main__":
    app.run(debug=True)