import numpy as np
from flask import send_file, Flask, request, render_template, jsonify
import pickle
import base64
import extcolors
import pandas as pd
from werkzeug.utils import secure_filename
from Geo import GeometricPatterns, color_to_df, generate_custom_path
import io
from rapidfuzz import process, fuzz
from PIL import Image
import os

app = Flask(__name__)
GeomtricModel = pickle.load(open("GeometricModel.pkl", "rb"))
FloralModel = pickle.load(open("FloralModel.pkl", "rb"))
SummerModel = pickle.load(open("SummerModel.pkl", "rb"))
TribalModel = pickle.load(open("TribalModel.pkl", "rb"))
df = pd.read_csv("dataPrediction2.csv")

app.config['UPLOAD_FOLDER'] = "ICT/Semester 5 (Stage)/Project/static/Images"


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("DesignPatterns.html")


def ColorCodePicker(Color):
    s_array = df[['ColorCode(1)', 'ColorCode(2)', 'ColorCode(3)']].values.T.ravel()
    Color = process.extractOne(Color, s_array, scorer=fuzz.WRatio)
    Color = Color[0]
    for i in df['ColorCode(1)']:
        if Color in i:
            ColorCode = df.loc[df['ColorCode(1)'] == i]
            ColorCode = ColorCode['ColorCodeNumber(1)'].iat[0]
            return ColorCode
        else:
            for i in df['ColorCode(2)']:
                if Color in i:
                    ColorCode = df.loc[df['ColorCode(2)'] == i]
                    ColorCode = ColorCode['ColorCodeNumber(2)'].iat[0]
                    return ColorCode
            else:
                for i in df['ColorCode(3)']:
                    if Color in i:
                        ColorCode = df.loc[df['ColorCode(3)'] == i]
                        ColorCode = ColorCode['ColorCodeNumber(3)'].iat[0]
                        return ColorCode


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        checked = 'checkbox' in request.form
        color1 = request.form['color1']
        color2 = request.form['color2']
        color3 = request.form['color3']

        company = request.form['company']
        Sector = request.form['sector']
        industry = request.form['industry']
        f = request.files.get('file')
        if checked != True:
            f.save(secure_filename(f.filename))
            colors_x = extcolors.extract_from_path(f, tolerance=12, limit=12)
            colors_x
            df_color = color_to_df(colors_x)
            df_color['occurence'] = df_color['occurence'].astype('int')
            colors = df_color.nlargest(3, 'occurence')
            FirstColor = colors['c_code'][0]
            SecondColor = colors['c_code'][1]
            ThirdColor = colors['c_code'][2]
            Colors = [FirstColor, SecondColor, ThirdColor]
        else:
            Colors = [color1, color2, color3]

        industry = df.loc[df['industry'] == industry]
        Sector = df.loc[df['sector'] == Sector]
        FirstColor = ColorCodePicker(Colors[0])
        SecondColor = ColorCodePicker(Colors[1])
        ThirdColor = ColorCodePicker(Colors[2])

        industry = industry['industryNumber'].iat[0]
        Sector = Sector['sectorNumber'].iat[0]
        pred = np.array([[industry, Sector, FirstColor, SecondColor, ThirdColor]])

    SummerPredict = SummerModel.predict(pred)
    GeometricPredict = GeomtricModel.predict(pred)
    FloralPredict = FloralModel.predict(pred)
    Triable = TribalModel.predict(pred)

    data = io.BytesIO()
    data2 = io.BytesIO()
    data3 = io.BytesIO()

    array = []

    designpatterns1 = GeometricPatterns(Colors, array)

    imhotep_spike_no = designpatterns1[1]
    imhotep_row_no = designpatterns1[2] * 2
    imhotep_row_margin_percent = designpatterns1[3]
    imhotep_middle_buffer_percent = designpatterns1[4]
    imhotep_row_buffer = designpatterns1[5]
    imhotep_downward_length = designpatterns1[6]
    imhotep_downward_no = designpatterns1[7]
    imhotep_downward_cols = designpatterns1[8] * 2

    imhotep_row_pensize = designpatterns1[9]
    imhotep_row_color = designpatterns1[10]
    imhotep_downward_pensize = designpatterns1[11]
    imhotep_downward_color = designpatterns1[12]
    imhotep_bounding_pensize = designpatterns1[13]
    imhotep_bounding_color = designpatterns1[14]

    designpatterns2 = GeometricPatterns(Colors, array)

    imhotep_spike_no_2 = designpatterns2[1]
    imhotep_row_no_2 = designpatterns2[2] * 2
    imhotep_row_margin_percent_2 = designpatterns2[3]
    imhotep_middle_buffer_percent_2 = designpatterns2[4]
    imhotep_row_buffer_2 = designpatterns2[5]
    imhotep_downward_length_2 = designpatterns2[6]
    imhotep_downward_no_2 = designpatterns2[7]
    imhotep_downward_cols_2 = designpatterns2[8] * 2

    imhotep_row_pensize_2 = designpatterns2[9]
    imhotep_row_color_2 = designpatterns2[10]
    imhotep_downward_pensize_2 = designpatterns2[11]
    imhotep_downward_color_2 = designpatterns2[12]
    imhotep_bounding_pensize_2 = designpatterns2[13]
    imhotep_bounding_color_2 = designpatterns2[14]



    designpatterns3 = GeometricPatterns(Colors, array)

    imhotep_spike_no_3 = designpatterns3[1]
    imhotep_row_no_3 = designpatterns3[2] * 2
    imhotep_row_margin_percent_3 = designpatterns3[3]
    imhotep_middle_buffer_percent_3 = designpatterns3[4]
    imhotep_row_buffer_3 = designpatterns3[5]
    imhotep_downward_length_3 = designpatterns3[6]
    imhotep_downward_no_3 = designpatterns3[7]
    imhotep_downward_cols_3 = designpatterns3[8] * 2

    imhotep_row_pensize_3 = designpatterns3[9]
    imhotep_row_color_3 = designpatterns3[10]
    imhotep_downward_pensize_3 = designpatterns3[11]
    imhotep_downward_color_3 = designpatterns3[12]
    imhotep_bounding_pensize_3 = designpatterns3[13]
    imhotep_bounding_color_3 = designpatterns3[14]



    img = designpatterns1[0]
    img2 = designpatterns2[0]
    img3 = designpatterns3[0]

    img.save(data, "JPEG")
    img2.save(data2, "JPEG")
    img3.save(data3, "JPEG")

    encoded_img_data = base64.b64encode(data.getvalue())
    encoded_img_data2 = base64.b64encode(data2.getvalue())
    encoded_img_data3 = base64.b64encode(data3.getvalue())

    return jsonify({'htmlresponse': render_template("response.html", img_data=encoded_img_data.decode('utf-8'),
                                                    img_data2=encoded_img_data2.decode('utf-8'),
                                                    img_data3=encoded_img_data3.decode('utf-8'),
                                                    imhotep_spike_no=imhotep_spike_no,
                                                    imhotep_row_no=imhotep_row_no,
                                                    imhotep_row_margin_percent=imhotep_row_margin_percent,
                                                    imhotep_middle_buffer_percent=imhotep_middle_buffer_percent,
                                                    imhotep_row_buffer=imhotep_row_buffer,
                                                    imhotep_downward_length=imhotep_downward_length,
                                                    imhotep_downward_no=imhotep_downward_no,
                                                    imhotep_downward_cols=imhotep_downward_cols,
                                                    imhotep_row_pensize=imhotep_row_pensize,
                                                    imhotep_row_color=imhotep_row_color,
                                                    imhotep_downward_pensize=imhotep_downward_pensize,
                                                    imhotep_downward_color=imhotep_downward_color,
                                                    imhotep_bounding_pensize=imhotep_bounding_pensize,
                                                    imhotep_bounding_color=imhotep_bounding_color,

                                                    imhotep_spike_no_2=imhotep_spike_no_2,
                                                    imhotep_row_no_2=imhotep_row_no_2,
                                                    imhotep_row_margin_percent_2=imhotep_row_margin_percent_2,
                                                    imhotep_middle_buffer_percent_2=imhotep_middle_buffer_percent_2,
                                                    imhotep_row_buffer_2=imhotep_row_buffer_2,
                                                    imhotep_downward_length_2=imhotep_downward_length_2,
                                                    imhotep_downward_no_2=imhotep_downward_no_2,
                                                    imhotep_downward_cols_2=imhotep_downward_cols_2,
                                                    imhotep_row_pensize_2=imhotep_row_pensize_2,
                                                    imhotep_row_color_2=imhotep_row_color_2,
                                                    imhotep_downward_pensize_2=imhotep_downward_pensize_2,
                                                    imhotep_downward_color_2=imhotep_downward_color_2,
                                                    imhotep_bounding_pensize_2=imhotep_bounding_pensize_2,
                                                    imhotep_bounding_color_2=imhotep_bounding_color_2,


                                                    imhotep_spike_no_3=imhotep_spike_no_3,
                                                    imhotep_row_no_3=imhotep_row_no_3,
                                                    imhotep_row_margin_percent_3=imhotep_row_margin_percent_3,
                                                    imhotep_middle_buffer_percent_3=imhotep_middle_buffer_percent_3,
                                                    imhotep_row_buffer_3=imhotep_row_buffer_3,
                                                    imhotep_downward_length_3=imhotep_downward_length_3,
                                                    imhotep_downward_no_3=imhotep_downward_no_3,
                                                    imhotep_downward_cols_3=imhotep_downward_cols_3,
                                                    imhotep_row_pensize_3=imhotep_row_pensize_3,
                                                    imhotep_row_color_3=imhotep_row_color_3,
                                                    imhotep_downward_pensize_3=imhotep_downward_pensize_3,
                                                    imhotep_downward_color_3=imhotep_downward_color_3,
                                                    imhotep_bounding_pensize_3=imhotep_bounding_pensize_3,
                                                    imhotep_bounding_color_3=imhotep_bounding_color_3
                                                    )})


@app.route('/downloadImage1', methods=['POST'])
def downloadFile():
    basedir = os.path.abspath(os.path.dirname(__file__))
    uploads_path = os.path.join(basedir, 'uploads')
    img = request.form.get('img')
    image_data = bytes(img, encoding="ascii")
    imag = Image.open(io.BytesIO(base64.b64decode(image_data)))
    path = generate_custom_path(uploads_path)
    imag.save(path)
    filename = imag.filename

    return send_file(path, as_attachment=True, download_name='image.jpg')
    # For windows you need to use drive name [ex: F:/Example.pdf]


@app.route('/regenerate', methods=['POST'])
def regenerate():
    form_data = request.form
    imhotep_spike_no = int(form_data["imhotep_spike_no"])
    imhotep_row_no = int(form_data["imhotep_row_no"])
    imhotep_row_margin_percent = int(form_data["imhotep_row_margin_percent"])
    imhotep_middle_buffer_percent = int(form_data["imhotep_middle_buffer_percent"])
    imhotep_row_buffer = int(form_data["imhotep_row_buffer"])
    imhotep_downward_length = int(form_data["imhotep_downward_length"])
    imhotep_downward_no = int(form_data["imhotep_downward_no"])
    imhotep_downward_cols = int(form_data["imhotep_downward_cols"])
    imhotep_row_pensize = int(form_data["imhotep_row_pensize"])
    imhotep_downward_pensize = int(form_data["imhotep_downward_pensize"])
    imhotep_bounding_pensize = int(form_data["imhotep_bounding_pensize"])
    imhotep_row_color = form_data["row_color"]
    imhotep_downward_color = form_data["downward_color"]
    imhotep_bounding_color = form_data["bounding_color "]
    imhotep_row_no = int(imhotep_row_no / 2)
    imhotep_downward_cols = int(imhotep_downward_cols / 2)

    Finalresult = [imhotep_spike_no, imhotep_row_no, imhotep_row_margin_percent, imhotep_middle_buffer_percent,
                   imhotep_row_buffer, imhotep_downward_length, imhotep_downward_no, imhotep_downward_cols,
                   imhotep_row_pensize, imhotep_row_color, imhotep_downward_pensize, imhotep_downward_color,
                   imhotep_bounding_pensize, imhotep_bounding_color]
    colors = [imhotep_row_color, imhotep_bounding_color]
    Designpattern = GeometricPatterns(colors, Finalresult)
    resultt = Designpattern[0]
    data = io.BytesIO()
    resultt.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template("regenerate.html", img_data=encoded_img_data.decode('utf-8'))
    # For windows you need to use drive name [ex: F:/Example.pdf]


if __name__ == '__main__':
    app.run(debug=True)
