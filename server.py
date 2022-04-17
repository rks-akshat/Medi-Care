from prediction_model import predict_covid

parameters = {
    "patient_name": "John Doeeeeeeeee",
    "procedure_date": "12/00/21 1400hrs",
    "age": 22,
    "sex": "M",
    "doctor_name": "Jane Doeeeeeeeee",
    "institution": "AIIMS",
    "reported_time": "12/03/21 1430hrs",
}

if __name__ == "__main__":
    img_path = r"C:\Users\akshat\Desktop\BIMCV(COVIDQU)\BIMCV(COVID-QU-Ex)\images\sub-S09340_ses-E20837_run-1_bp-chest_vp-ap_cr.png"
    pdf = predict_covid(parameters, img_path)
    pdf.output(f"pdf-{img_path[-8:-4]}.pdf")
