from flask import Flask, Response
import json

app = Flask(__name__)

#http://127.0.0.1:3000/alkuluku/<luku>
@app.route('/alkuluku/<luku>')
def on_alkuluku(luku):
    try:
        luku = int(luku)
        onko = None
        if luku < 2:
            onko = False
        else:
            onko = True
            for n in range(2, int(luku / 2) + 1):
                if luku % n == 0:
                    onko = False
                    break
        tilakoodi = 200
        vastaus = {
            "Number": luku,
            "isPrime": onko
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    json_vast = json.dumps(vastaus)
    return Response(response=json_vast, status=tilakoodi, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)